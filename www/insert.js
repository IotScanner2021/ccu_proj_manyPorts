// users can insert ip and some information of the device by himself
function insertIP( table_id ){
	var ip = document.forms["ipForm"]["ip"].value;
	var devicetype = document.forms["ipForm"]["devicetype"].value;
	var productmodel = document.forms["ipForm"]["productmodel"].value;
	var os = document.forms["ipForm"]["os"].value;
	var site = document.forms["ipForm"]["site"].value;
	
	if(ip.length == 0 || devicetype == 0 || productmodel == 0 || os == 0 || site == 0){
		document.getElementById("form1Screen1").innerHTML = "Please input the information.";
	}
	else{	
		document.getElementById("form1Screen1").innerHTML = "<div class='loader'></div>";
		document.getElementById("form1Screen1").innerHTML = "Enter the new device.";
		/*
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.onreadystatechange = function(){
			if(this.readyState === 4 && this.status == 200){
				document.getElementById("form1Screen1").innerHTML = "????";
			}
			else{
				document.getElementById("form1Screen1").innerHTML = "!!!!";
				document.getElementById("form1Screen2").innerHTML = "<h3>Please wait a moment more<h3>";
			}
		};
		xmlhttp.open("GET","project.php?ip=" + str,true);
		xmlhttp.send();
		*/
		var data = new FormData();
		data.append('ip' , ip);
		data.append('devicetype' , devicetype);
		data.append('productmodel' , productmodel);
		data.append('os' , os);
		data.append('site' , site);

		var xmlhttp = new XMLHttpRequest();
		xmlhttp.open("POST" , "insert_post.php?table_id=" + table_id , false);
		xmlhttp.send(data);
	}
}
