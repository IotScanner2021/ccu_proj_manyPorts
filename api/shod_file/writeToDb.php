<?php

	function insertTodb($conn,$fname,$devicetype){
		$f = fopen($fname,"r");
		$data = fread($f,filesize($fname));
		$cur = 0;
		$prev = 0;
		$num = 0;
		$lines = array();
		while($cur < strlen($data)){
			if($data[$cur] != "\n"){
				$cur++;
				continue;
			}
			else{
				$lines[$num++] = substr($data,$prev,$cur-$prev);
				$cur++;
				$prev = $cur;
			}
		}
		echo $lines[0];	

		for($i=0;$i<count($lines);$i++){
			if($i%3==0){
				$ip = preg_split('/:/',$lines[$i]);
			}
			else if($i%3==1){
				$os = preg_split('/:/',$lines[$i]);
				$query = "insert into ip_1 (ip,os,device_type) values ('".$ip[1]."','".$os[1]."','".$devicetype."')";
				echo $query."\n";
				if($conn->query($query) == True){
					echo "insert successfully"."\n";
				}
				else{
					echo "fail"."\n";
				}
			}
			else{
				$port = preg_split('/:/',$lines[$i]);
				$query = "insert into port_1 (port_ip,port) values ('".$ip[1]."','".$port[1]."')";
				echo $query."\n";
				if($conn->query($query) == True){
					echo "insert successfully"."\n";
				}
				else{
					echo "fail"."\n";
				}
			}
		}

		$query = "select * from ip";
		$res = $conn->query($query);
		echo $res->num_rows;	
		
		fclose($f);
	}

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
	echo "Connected successfully";

	insertTodb($conn,"Printer.log","printer");
	insertTodb($conn,"Router.log","router");	
	insertTodb($conn,"Webcam.log","camera");	
	insertTodb($conn,"Nas.log","nas");	
	
	$conn->close();
?>
