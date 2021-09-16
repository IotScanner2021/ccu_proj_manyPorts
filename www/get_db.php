<?php
	$severname = "localhost";
	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;

	//connect
	$conn = new mysqli($severname,$username,$password,$database,$port);
	if($conn->connect_error){
		die("Connection failed:".$conn->connect_error);
	}
	echo "Connected successfully\n";

	//get data
	$query = "select * from ip_".$table_id;
	$result = $conn->query($query);
	if($result->num_rows>0){
		while($row = $result->fetch_assoc()){
			var_dump($row);
		}
		$result->free();
	}

	//get device number
	/*
	$printer_num = 0;
	$router_num = 0;
	$nas_num = 0;
	$camera_num = 0;

	$query = "select * from ip";
	$result = $conn->query($query);
	if($result->num_rows>0){
		while($row = $result->fetch_assoc()){
			//var_dump($row);
			if($row["device_type"] == "printer") $printer_num++;
			if($row["device_type"] == "router") $router_num++;
			if($row["device_type"] == "nas") $nas_num++;
			if($row["device_type"] == "camera") $camera_num++;
		}
		$result->free();
	}
	echo "printer_num : ".$printer_num."\n";
	echo "router_num : ".$router_num."\n";
	echo "nas_num : ".$nas_num."\n";
	echo "camera_num : ".$camera_num."\n";
	*/

	//close
	$conn->close();
?>
