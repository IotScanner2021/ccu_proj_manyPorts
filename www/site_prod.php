<?php

	$severname = "localhost";
	$username = "root";
	$password = "a407410040";
	$database = "iot";
	$port = 3306; 
	$conn = mysqli_connect($severname,$username,$password,$database);
	$device = $_GET["device"];
	$table_id = $_GET["table_id"];
	$query = "select * from ip_".$table_id." where device_type='" . $device."'";
	$result = $conn->query($query);
	if($result->num_rows>0){
		$row = $result->fetch_assoc();
		$txt = '[{"ip":"' .$row['ip']. '"}';
		echo $txt;
		while($row = $result->fetch_assoc()){
			$txt = ',{"ip":"' .$row['ip']. '"}';
			echo $txt;
		}
		$result->free();
	}
	$txt = ']';
	echo $txt;
  ?>

