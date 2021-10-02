<?php
	$ip = $_GET['ip'];

	//update
	echo shell_exec("sh ../api/log/rm_sh.sh");		
	//running
	$command = "python3 /var/www/html/ccu_proj_manyPorts/api/main.py --ip ".$ip;
	echo shell_exec($command);
?>

