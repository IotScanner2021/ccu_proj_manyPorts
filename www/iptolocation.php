<?php
	$ip = $_GET["ip"];
	//$ip = '140.123.230.32';
	$url = 'http://api.ipstack.com/'.$ip.'?access_key=2f1ffc09d352e1d2f49d800d6090bfa5';
	$ch = curl_init($url);
	$res = curl_exec($ch);
	curl_close($ch);
	//echo $res;
?>
