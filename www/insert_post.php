<?php
    	$severname = "localhost";
    	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;
	$conn = mysqli_connect($severname,$username,$password,$database);

	$ip = $_POST["ip"];
	$devicetype = $_POST["devicetype"];
	$productmodel = $_POST["productmodel"];
	$os = $_POST["os"];
	$site = $_POST["site"];

	$table_id = $_GET["table_id"];
	$query = "insert into ip_" .$table_id. " (ip , device_type , product_model , os , site) values ('" .$ip. "' , '" .$devicetype. "' , '" .$productmodel. "' , '" .$os. "' , '" .$site. "')";
	$result = $conn->query($query);
	//echo $query;
?>
