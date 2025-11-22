from waitress import serve
from flask import Flask, request, render_template, jsonify, make_response

import warnings
warnings.simplefilter('ignore')
import pandas as pd
import numpy as np
import sklearn.model_selection as ms
import sklearn.metrics as mt
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from joblib import dump, load

eplogic = load('./eplogic.joblib')

app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    try:
        # Extract parameters from the request
        eplet_locus = request.values.get('eplet_locus')
        panel_nc = request.values.get('panel_nc')
        panel_pc = request.values.get('panel_pc')
        eplet_allele_qtd = request.values.get('eplet_allele_qtd')
        eplet_min_mfi = request.values.get('eplet_min_mfi')
        eplet_max_mfi = request.values.get('eplet_max_mfi')

        # Check if all parameters are present
        if None in (eplet_locus, panel_nc, panel_pc, eplet_allele_qtd, eplet_min_mfi, eplet_max_mfi):
            return "Missing required parameters.", 400

        # Validate eplet_locus
        eplet_locus_map = {'abc': [1, 0, 0, 0],
                           'drb': [0, 1, 0, 0],
                           'dq':  [0, 0, 1, 0],
                           'dp':  [0, 0, 0, 1]}

        if eplet_locus not in eplet_locus_map:
            return "Invalid eplet_locus value.", 400

        eplet_locus_encoding = eplet_locus_map[eplet_locus]

        # Convert other parameters to integers
        try:
            panel_nc = int(panel_nc)
            panel_pc = int(panel_pc)
            eplet_allele_qtd = int(eplet_allele_qtd)
            eplet_min_mfi = int(eplet_min_mfi)
            eplet_max_mfi = int(eplet_max_mfi)
        except ValueError:
            return "Numeric parameters must be integers.", 400

        # Prepare data for prediction
        eplet_data = [eplet_locus_encoding + [panel_nc, panel_pc, eplet_allele_qtd, eplet_min_mfi, eplet_max_mfi]]

        # Make predictions using the model
        results = eplogic.predict(eplet_data)
        probabilities = eplogic.predict_proba(eplet_data)

        # Prepare the JSON response
        predictions = jsonify(label=str(results[0]),
                              score0=str(probabilities[0][0]),
                              score1=str(probabilities[0][1]))

        response = make_response(predictions)
        response.mimetype = 'application/json'
        return response
    
    except Exception as e:
        # Log the exception for debugging
        print(f"Exception in /predict: {e}")
        return "An error occurred during prediction.", 500

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, threads=4)
 