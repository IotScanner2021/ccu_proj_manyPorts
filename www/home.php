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
		<script src="home.js"></script>
		<script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>
		<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
		<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
		<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
		<meta content="utf-8" http-equiv="encoding">

	</head>

	<body>
		<!-- Navbar (sit on top) -->
		<div class="w10yy3-top">
		  <div class="w3-bar w3-white w3-wide w3-padding w3-card">
		    <!--a href="#home" class="w3-bar-item w3-button"><b>IOT</b> Scanner</a-->
		    <a href="home.php?table_id=1" class="w3-bar-item w3-button"><b>IOT</b> Scanner</a>
			<div class="w3-right w3-hide-small">
		      	<button class="w3-bar-item w3-button" onclick=update()><i style="font-size:24px; color : gray" class="fa">&#xf021;</i></button>
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
		
		<div id="table_id" style="display:none"><?php echo $_GET["table_id"];?></div>

		  <div class="w3-container w3-padding-64" id="projects">
			<div class="card text-white bg-secondary my-5 py-5"> 
				<div class="card text-white bg-dark mb-3" style="max-width:24.5rem;margin:auto;"> 
					<h1 class="tt card-text">物聯網偵查引擎</h1>
				</div>
					<h3 class = "tt" style="max-width:60rem;margin:auto;" align="center">IoTScanner 是一套提供IoT資訊蒐集、弱點偵查與驗證的系統</h3>
					<h3 class = "tt" style="max-width:60rem;margin:auto;" align="center">此頁面為您的檢索區域 IP:<b><?php echo isset($_GET['ip']) ? $_GET['ip'] : 'xxxx'; ?></b>的資訊整理</h3>
					
			</div>

		  <div class="container" id="search_result">
			  <div class="row">
			    <div class="col">
				<div id="chartContainer" style="height: 390px; width: 100%;"></div>
			    </div>
			    <div class="col">

				<!--
				<div class="row">
				<div class="row my-5">
				    <div class="d-flex justify-content-around">
					<a href="site.php?device='camera'" class="btn btn-secondary btn-lg p-5" role="button">Camera</a>
					<a href="site.php?device='router'" class="btn btn-secondary btn-lg p-5" role="button">Router</a>
				    </div>
				</div>
				<div class="row my-5">
				    <div class="d-flex justify-content-around">
					<a href="site.php?device='printer'" class="btn btn-secondary btn-lg p-5" role="button">Printer</a>
					<a href="site.php?device='nas'" class="btn btn-secondary btn-lg p-5" role="button">NAS</a>
				    </div>
				</div>
				-->

				<!--device number-->
				<div class="row">
					<div class="col">
					 <div class="card text-center mb-3">
					  <div class="card-body" style="background-color:#ff0000">
					  <p class="card-text text-center fs-4 text-white" id="nas_num"><?php echo $nas_num;?></p>
					  </div>
					  <div class="card-header text-dark" style="font-size:10px">NAS</div>
					 </div>
					</div>
					<div class="col">
					 <div class="card text-center mb-3">
					  <div class="card-body" style="background-color:#ff4000">
					   <p class="card-text text-center fs-4 text-white" id="router_num">20</p>
					  </div>
					  <div class="card-header text-dark" style="font-size:10px">Router</div>
					 </div>
					</div>
					<div class="col">
					 <div class="card text-center mb-3">
					  <div class="card-body" style="background-color:#ff8000">
					   <p class="card-text text-center fs-4 text-white" id="printer_num">30</p>
					  </div>
					  <div class="card-header text-dark" style="font-size:10px">Printer</div>
					 </div>
					</div>
					<div class="col">
					 <div class="card text-center mb-3">
					  <div class="card-body" style="background-color:#ffbf00">
					   <p class="card-text text-center fs-4 text-white" id="camera_num">40</p>
					  </div>
					  <div class="card-header text-dark" style="font-size:10px">Camera</div>
					 </div>
					</div>
				</div>

				<div class="row mb-3">
				  <div class="col-sm-6">
				    <div class="card">
				      <div class="card-body">
					<h3 class="card-title">NAS</h3>
					<a href="site.php?device=nas&table_id=<?php echo $_GET["table_id"]?>" class="btn btn-primary">See more</a>
				      </div>
				    </div>
				  </div>
				  <div class="col-sm-6">
				    <div class="card">
				      <div class="card-body">
					<h3 class="card-title">Printer</h3>
					<a href="site.php?device=printer&table_id=<?php echo $_GET["table_id"]?>" class="btn btn-primary">See more</a>
				      </div>
				    </div>
				  </div>
				</div>
				
				
				<div class="row mb-3">
				  <div class="col-sm-6">
				    <div class="card">
				      <div class="card-body">
					<h3 class="card-title">Router</h3>
					<a href="site.php?device=router&table_id=<?php echo $_GET["table_id"]?>" class="btn btn-primary">See more</a>
				      </div>
				    </div>
				  </div>
				  <div class="col-sm-6">
				    <div class="card">
				      <div class="card-body">
					<h3 class="card-title">Camera</h3>
					<a href="site.php?device=camera&table_id=<?php echo $_GET["table_id"]?>" class="btn btn-primary">See more</a>
				      </div>
				    </div>
				  </div>
				</div>
			  </div>
		  </div>
		  </div>

		<div class="d-flex flex-row text-center" style="margin:10em 25em 0em;">
			<img src="./alert.jpg" style="width:5em;height:5em;">
			<h2 style="font-size:60px;">Alert</h2>
		</div>
		<div class="card bg-light" style="max-width:60rem;margin:0em 25em 0em;" id="alertion">
		</div>
	</body>
</html>
