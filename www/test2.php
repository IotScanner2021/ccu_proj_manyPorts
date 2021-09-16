<!DOCTYPE html>
<html>
<body>
  <div>
    <h3>ip</h3>
	<div>
	<script>
		/*window.onload = function(){
			xhttp = new XMLHttpRequest();
			url = "get_db.php";
			xhttp.open("GET",url,false);
			xhttp.send();
			alert(xhttp.responseText);
		}*/

		xhttp = new XMLHttpRequest();
		url = "device_num.php";
		xhttp.open("GET",url,false);
		xhttp.send();
		res = JSON.parse(xhttp.responseText);
		console.log(res["printer"]);
	</script>
  </div>

  <div>
    <h4>cve</h4>
	<?php 
       		#var_dump(get_loaded_extensions());

	//phpinfo(INFO_MODULES);
	?>
  </div>
</body>
</html>
