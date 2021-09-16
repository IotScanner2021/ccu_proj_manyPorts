<?php

	$ip = $_GET["ip"];
	$cve = $_GET["cve_id"];
	$port = $_GET["port"];
/*	
	$ip = "140.123.230.32";
	$cve = "CVE-2017-17562";
	$port = "8080";
 */
	$data = shell_exec('python3 ../api/exploit/exploit_unit.py '.$ip.' '.$cve.' '.$port);

	$f = fopen("cve/".$cve.".txt","w");
	fwrite($f,$data);
	fclose($f);
?>
