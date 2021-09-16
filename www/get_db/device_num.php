<?php
	$severname = "localhost";
	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;
	$table_id = $_GET["table_id"];
	//$table_id = "1";

	//connect
	$conn = new mysqli($severname , $username , $password , $database , $port);
	if($conn->connect_error){
		die("Connection failed:".$conn->connect_error);
	}

	//get device number
	$printer_num = 0;
	$router_num = 0;
	$nas_num = 0;
	$camera_num = 0;

	$query = "select * from ip_".$table_id;
	$result = $conn->query($query);
	if($result->num_rows>0){
		while($row = $result->fetch_assoc()){
			if($row["device_type"] == "printer") $printer_num++;
			if($row["device_type"] == "router") $router_num++;
			if($row["device_type"] == "nas") $nas_num++;
			if($row["device_type"] == "camera") $camera_num++;
		}
		$result->free();
	}

	$device_num = array(
		"printer" => $printer_num,
		"router" => $router_num,
		"nas" => $nas_num,
		"camera" => $camera_num
	);

	echo json_encode($device_num);
//	var_dump(json_encode($device_num));
?>

	
