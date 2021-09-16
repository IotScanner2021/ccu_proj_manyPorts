<?php

	$servername = "localhost";
	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;
	$table_id = $_POST["table_id"];
//	$table_id = 1;

	$conn = new mysqli($servername , $username , $password , $database , $port);
	if($conn->connect_error){
		die("Connection failed:".$conn->connect_error);
	}

	
	$target_os = $_POST["os"];
	$target_device_type = $_POST["device_type"];
	$target_product_model = $_POST["product_model"];
	

//	$target_os = "";
//	$target_device_type = "nas";
//	$target_product_model = "";


	//array_push($match_res["ip"] , $ip);
	//array_push($match_res["site"] , $site);
	//count($match_res["ip"]);
	 

	$match_res = array(
		"ip" => array(),
		"site" => array()
	);

	$query = "select * from ip_".$table_id;
	$result = $conn->query($query);
	if($result->num_rows>0){
		while($row = $result->fetch_assoc()){
			if(($target_os=="" || $row["os"]==$target_os) && ($target_device_type=="" || $row["device_type"]==$target_device_type) && ($target_product_model=="" || $row["product_model"]==$target_product_model)){
				array_push($match_res["ip"] , $row["ip"]);
				array_push($match_res["site"] , $row["site"]);
			}
		}
		$result->free();
	}

	echo json_encode($match_res);
//	var_dump(json_encode($match_res));
?>
