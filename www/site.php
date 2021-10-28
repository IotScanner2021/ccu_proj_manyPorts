<!-- seperate the ip -->
<!DOCTYPE>
<html>
	<head>
		<title>iotScanner</title>
		<meta chraset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script src="https://kit.fontawesome.com/b5c904ba42.js" crossorigin="anonymous"></script>
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		<link rel="stylesheet" href="./home.css">
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
		<script src="./site.js"></script>
		<link href="./site.css" rel="stylesheet" type="text/css">
		<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
		<meta content="utf-8" http-equiv="encoding">

	</head>
	<body>
		<!--navbar--!>
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

		<!--
		<div class="w3-content w3-padding-64" style="max-width:1564px">
			<div class="container">
				<div class="row" id=<?php echo $_GET["device"];?> name="device">
					<h1><?php echo "device : ".substr($_GET["device"],1,strlen($_GET["device"])-2);?></h1>
				</div>
			</div>
		</div>
		-->

		<div class="w3-content w3-padding-64" style="max-width:1564px">
			<div class="container">
				<div class="row">
					<div id="table_id" style="display:none;"><?php echo $_GET["table_id"];?></div>
					<div id="device" style="display:none;"><?php echo $_GET["device"];?></div>
					<div class="device-name">
		    				<h1 class="w3-border-bottom w3-border-light-grey w3-padding-16"><?php echo "Device : ".$_GET["device"];?></h1>
					</div>
				</div>
				<div id="all"></div>
				<div class="row" id=<?php echo $_GET["device"];?> name="device">
					
				</div>
			</div>
		</div>
	</body>
</html>
