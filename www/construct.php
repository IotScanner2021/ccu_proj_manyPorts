<!DOCTYPE html>
<html>
	<head>
		<title>iotScanner</title>
		<meta chraset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script src="https://kit.fontawesome.com/b5c904ba42.js" crossorigin="anonymous"></script>
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		<link rel="stylesheet" href="./home.css">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
		<script src="construct.js"></script>
		<script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
		<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
		<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
		<meta content="utf-8" http-equiv="encoding">

	</head>
	<body>
		<!-- Navbar (sit on top) -->
		<div class="w10yy3-top">
		  <div class="w3-bar w3-white w3-wide w3-padding w3-card">
			    <a href="home.php?table_id=<?php echo $_GET["table_id"];?>" class="w3-bar-item w3-button"><b>IOT</b> Scanner</a>
			    <div class="w3-right w3-hide-small">
		      		<a href="home.php?table_id=<?php echo $_GET["table_id"];?>" class="w3-bar-item w3-button">Home</a>
				<a href="search.php?table_id=<?php echo $_GET["table_id"];?>" class="w3-bar-item w3-button">Search</a>
		      		<a href="insert.php?table_id=<?php echo $_GET["table_id"];?>" class="w3-bar-item w3-button">Insert</a>
		    		<a href="construct.php?table_id=<?php echo $_GET["table_id"];?>" class="w3-bar-item w3-button">Construct</a>
		    	    </div>
		  </div>
		 </div>

		<!-- Header -->
		<header class="w3-display-container w3-content w3-wide" style="max-width:1500px;" id="home">
			<!--<img class="w3-image" src="/w3images/architect.jpg" alt="IotScanner" width="1500" height="800">-->
		  <div class="w3-display-middle w3-margin-top w3-center">
		    <h1 class="w3-xxlarge w3-text-white"><span class="w3-padding w3-black w3-opacity-min"><b>IOT</b></span> <span class="w3-hide-small w3-text-light-grey">Scanner</span></h1>
		  </div>
		</header>

		<!-- Page content -->
		<div class="w3-content w3-padding" style="max-width:1564px">

		  <!-- Project Section -->
		  <div class="w3-container w3-padding-64" id="projects">
		    <h3 class="w3-border-bottom w3-border-light-grey w3-padding-16">Projects</h3>
		    <p>
			Put your ip in the blank and we can find whether the IOT devices under your ip are safe or not!
		    </p>
		    <form name="projectForm">
			<input class="w3-input w3-section w3-border" type="text" placeholder="xxx.xxx.xxx.xxx" required name="ip">
			<button class="w3-button w3-light-grey w3-section" type="button" onclick="loadDoc()">
					SUBMIT
			</button>
		    </form>
			<p style="height:10rem;" class="w3-panel w3-border w3-hover-border-red" id="form1Screen1">
				<!--
	    				<a href='output.txt' style='display:block;margin:30px;' download>
						<i class='fas fa-file-alt' style='font-size:72px;'></i>
					</a>
				-->
			</p>
		  </div>
			<div id="form1Screen2"></div>

	</body>
</html>
