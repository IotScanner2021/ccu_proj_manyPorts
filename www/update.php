<?php
	$table_id = $_GET['table_id'];
	echo shell_exec("python3 /var/www/html/ccu_proj_manyPorts/api/update.py --table_id ".$table_id);
?>
