<?php

$severname = "localhost";
$username = "root";
$password = "a407410040";
$database = "iot";
$port = 3306;
$table_id = $_GET["table_id"];
//$table_id = 1;

$conn = mysqli_connect($severname,$username,$password,$database);

$ip = $_GET["ip"];
//$ip ="140.123.126.43";

$query = "select * from cve_".$table_id." where cve_ip=\"" . $ip . '"';
$result = $conn->query($query);
//echo $result;

$r = array();

if($result->num_rows>0){
	while($row = $result->fetch_assoc()){
		array_push($r,$row);
/*
		echo "<tr>";
			echo "<th>" . $row['cve_id'] . "</th>";
			echo "<td>";
			echo $row['description'];
			echo "</td>";
		echo "</tr>";
 */
	}
	$result->free();
}
echo json_encode($r);
$conn->close();

?>
