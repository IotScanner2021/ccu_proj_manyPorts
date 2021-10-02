function loadDoc(){
	
	document.getElementById("form1Screen1").innerHTML = "<div class='loader'></div>";
	
	var str = document.forms["projectForm"]["ip"].value;
	
	if(str.length == 0){
		document.getElementById("form1Screen1").innerHTML = "EMPTY";
	}
	else{
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if(xmlhttp.readyState==4 && xmlhttp.status==200){
				var xhttp = new XMLHttpRequest();
				xhttp.open("GET","table.txt",false);
				xhttp.send();

				console.log(xhttp.responseText);
				table_id = xhttp.responseText;
				location.href = "home.php?table_id="+table_id+"&ip="+str;
			}
		}
		xmlhttp.open("GET","construct_db.php?ip=" + str,true);
		xmlhttp.send();
	}	
	
}
