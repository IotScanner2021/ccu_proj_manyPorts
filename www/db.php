<?php

	function insert_db($conn,$sql){
		if($conn->query($sql) == true){
			echo "insert successfully";
		}else{
			echo "Error:".$sql.$conn->error;
		}
	
	}
	$severname = "localhost";
	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306;

	echo $port;

	//connect
	
	$conn = new mysqli($severname,$username,$password,$database,$port);
	if($conn->connect_error){
		die("Connection failed:".$conn->connect_error);
	}
	echo "Connected successfully";
	 
/*	
	//operation - insert
	$sql = "insert into ip (ip,os,site) values ('256.256.256.256','windows','會資系')";
	//$sql = "insert into ip (ip,os,site) values ('256.256.256.257','ubuntu','中文系')";
	insert_db($conn,$sql);	

	$sql = "insert into cvee (cvee_id,description,cvss,cvee_ip) values ('default','default',8.7,'256.256.256.256')";
	insert_db($conn,$sql);	
	
	$sql = "insert into port (port,port_ip) values (80,'256.256.256.256')";
	insert_db($conn,$sql);	
 */	
	/*
	//operation - select data
	$query = "select * from cvee";
	$result = $conn->query($query);
	if($result->num_rows>0){
		while($row = $result->fetch_assoc()){
			var_dump($row);
		}
		$result->free();
	}
	 */

	//close
	//$conn->close();
	
?>
