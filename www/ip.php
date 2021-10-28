<!-- The page to present information about IP -->
<!DOCTYPE html>
<html>
    <head>
        <title>iotScanner</title>
	<meta chraset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
	
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
	<link rel="stylesheet" href="./ip.css">
	<link href="https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.css" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
	<script src="https://api.mapbox.com/mapbox-gl-js/v2.2.0/mapbox-gl.js"></script>
	<script src="ip.js"></script>
	<script src="map.js"></script>
	<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
	<meta content="utf-8" http-equiv="encoding">

</head>
    <body>
<div class="container-fluiid bg-white">
	<div class="row">
		<div class="col">
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
		</div>
	</div>
	<div class="row" style="height:70px;">
		<div class="col">
			<!-- Header -->
			<header class="w3-display-container w3-content w3-wide" style="max-width:1500px;" id="home">
				<!--<img class="w3-image" src="/w3images/architect.jpg" alt="IotScanner" width="1500" height="800">-->
			  <div class="w3-display-middle w3-margin-top w3-center">
			    <h1 class="w3-xxlarge w3-text-white"><span class="w3-padding w3-black w3-opacity-min"><b>IOT</b></span> <span class="w3-hide-small w3-text-light-grey">Scanner</span></h1>
			  </div>
			</header>
		</div>
	</div>
  <div class="row" style="height:250px;">
		<!-- container for present map -->
		<div class="col">
			<div id="table_id" style="display:none"><?php echo $_GET["table_id"];?></div>
			<div class="card" style="height:100%">
				<div id="map"></div>
					<script>
						const urlParams = new URLSearchParams(window.location.search);
						const myParam = urlParams.get('ip');
						let map_ip = myParam;
						//get_lat(map_ip);
						lat(map_ip);
					</script>
				</div>
			</div>
		</div>
		<h1 id=ip><?php echo $_GET["ip"];?></h1>
	<div class="row">
	<div class="col-sm-7 p-4">
            <div class="card card_shadow  p-3 m-2 border-warning">
                <div>
                    <h2><b>General</b> Information</h2>
                </div>
                <div class="row">
                    <table class="table table-striped">
			<tbody>
			<!-- load infromation from mysql -->
				<?php 
					$severname = "localhost";
					$username = "root";
					$password = "a407410040";
					$database = "iot";
					$port = 3306;
					$table_id = $_GET["table_id"];

					$conn = mysqli_connect($severname,$username,$password,$database);
					$ip = $_GET["ip"];
					$query = "select * from ip_".$table_id." where ip=\"" . $ip . '"';
					$result = $conn->query($query);
					if($result->num_rows>0){
						$row = $result->fetch_assoc();
						$result->free();
					}
				?>
			      <tr><td>Location</td><th id="location"><?php echo $_GET["location"]!=null?$_GET["location"]:"None";?></th></tr>
			      <tr><td>Device</td><th id="deviceType"><?php echo $row['device_type'] ?></th></tr>
			      <tr><td>Device Model</td><th id="deviceModel"><?php echo $row['product_model']!=null?$row['product_model']:"None"; ?></th></tr>
			      <tr><td>OS</td><th id="os"><?php echo $row['os']!=null?$row["os"]:"None"; ?></th></tr>
                        </tbody>
                    </table>
                </div>
            </div>
	</div>
				<?php
					$query = "select * from port_".$table_id." where port_ip=\"" . $ip . '"';
					$result = $conn->query($query);
				?>
        <div class="col-sm-4 p-4">
            <div class="card card_shadow p-3 m-2 border-info bg-light">
                <div>
                    <h2>Open <b>Ports</b></h2>
                </div>
                <div id="ports" style="margin: 10px;">
				<?php
					if($result->num_rows>0){
						while($row = $result->fetch_assoc()){
							echo '<h4 class="bg-info text-light">';
							echo $row['port'];
							echo "</h4>";
						}
						$result->free();
					}
				?>
                </div>
            </div>

	</div>
	</div>
	<?php
		$query = 'select * from cve_'.$table_id.' where cve_ip="' . $ip . '"';
		$result = $conn->query($query);
	?>
<div class="row">
	<div class="col-sm-7 p-4">
		<div class="card card_shadow p-3 m-2 border-warning">
			<h3><b>Vulnerabilities</b></h3>
				<table class="table table-striped">
					<tbody id="vuln">
					</tbody>
				</table>
		</div>
	</div>
</div>
    </body>
</html>
