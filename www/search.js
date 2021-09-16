function search(){


	table_id = document.getElementById("table_id").innerHTML;
	device_type = document.forms["filter"]["devicetype"].value;
	product_model = document.forms["filter"]["productmodel"].value;
	os = document.forms["filter"]["os"].value;

	xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if( xhttp.readyState==4 && xhttp.status==200 ){
  			res = JSON.parse(xhttp.responseText);
			console.log(res);

//			result = document.getElementById("result");
//			tr = document.createElement("tr");
//			td = document.createElement("td");
//			td.setAttribute("align" , "center");
//			a = document.createElement("a");
//			td.appendChild(a);
//			tr.appendChild(td);
//			result.appendChild(tr);

			for(i = 0 ; i<Object.keys(res["ip"]).length ; i+=5){
				tr = document.createElement("tr");
				for(j=0;j<5;j++){
					td = document.createElement("td");
					//td.setAttribute("align" , "center");
					a = document.createElement("a");
					a.innerHTML = res["ip"][i+j];
					td.appendChild(a);
					tr.appendChild(td);
				}
				result.appendChild(tr);
			}
		}
	};

	url = "./get_db/device_ip.php"; 
	params = "table_id=" + table_id + "&device_type=" + device_type + "&product_model=" + product_model + "&os=" + os;

	xhttp.open("POST" , url , true);
	xhttp.setRequestHeader('Content-Type',  'application/x-www-form-urlencoded');
	xhttp.send(params);
	res = xhttp.responseText;

}
