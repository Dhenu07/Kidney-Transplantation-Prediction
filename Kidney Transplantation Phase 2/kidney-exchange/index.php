<!DOCTYPE html>
<html lang="en">
<link rel="preconnect" href="https://fonts.gstatic.com">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Domine:wght@400;500&display=swap" rel="stylesheet">
<!-- for bootstrap css  -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
<style>
body {
    height: 100vh;
    background-image: radial-gradient(circle, #121d31, #181c30, #1d1c2e, #211b2d, #241b2b, #2f2034, #3c243b, #4a2842, #683152, #89395e, #ab4266, #cd4c6a);
}

p{
  text-align: justify;
}
img{
    align-items: center;
}
.intro{
  font-family: 'Domine', serif;
}
.kid-img{
    display: flex;
    justify-content: center;
    width: 100%;
    height: 90vh;

}

</style>

<?php include("templates/header.php") ?>

<div class="nav-container">
    <?php include("templates/navBar.php") ?>
</div>

<div class="container-fluid" >
    <div class="kid-img">
        <img src="./images/kidney-trans.png" alt="" width="100%">
    </div>
    
    </div>
</div>


<?php include("include/footer.inc.php") ?>