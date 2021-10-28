<!-- insert the data to the database for post -->
<?php
    	$severname = "localhost";
    	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;
	$conn = mysqli_connect($severname,$username,$password,$database);

	$ip = htmlentities($_POST["ip"]);
	$devicetype = htmlentities($_POST["devicetype"]);
	$productmodel = htmlentities($_POST["productmodel"]);
	$os = htmlentities($_POST["os"]);
	$site = htmlentities($_POST["site"]);	
	$table_id = htmlentities($_GET["table_id"]);
/*
	$ip = htmlentities('"aaaaa"');
	$devicetype = htmlentities('nas');
	$productmodel = htmlentities('test');
	$os = htmlentities('test');
	$site = htmlentities('test');	
	$table_id = htmlentities('2');
 	
	echo $ip.$devicetype.$productmodel.$os.$site.$table_id;
 */
	$query = "insert into ip_" .$table_id. " (ip , device_type , product_model , os , site) values ('" .$ip. "' , '" .$devicetype. "' , '" .$productmodel. "' , '" .$os. "' , '" .$site. "')";
	$result = $conn->query($query);
	//echo $query;
?>
