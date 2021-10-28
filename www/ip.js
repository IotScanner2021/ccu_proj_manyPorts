//以ip到資料庫load出相關資訊
window.onload = function(){
	var ip = document.getElementById('ip').innerHTML;
	var table_id = document.getElementById('table_id').innerHTML;
	var xhttp = new XMLHttpRequest();
	url = "ip_cve.php?table_id=" + table_id + "&ip=" + ip;
	xhttp.open("GET",url,false);
	xhttp.send();
	
	obj = JSON.parse(xhttp.responseText);
	for(var i=0;i<obj.length;i++){
		var tab = document.getElementById('vuln');
		var tr = document.createElement('tr');
		var th = document.createElement('th');
		var td = document.createElement('td');
		th.innerHTML = obj[i].cve_id + "<br>";
		td.innerHTML = obj[i].description + "<br>";
		var inp = document.createElement('input');
		inp.id = obj[i].cve_id;
		inp.type = "button";
		inp.onclick = function(){
			ip = document.getElementById('ip').innerHTML;
			port = "8080";
			url = "cve_validate.php?cve_id=" + this.id + "&ip=" + ip + "&port=" + port;
			var xhttp = new XMLHttpRequest();
			xhttp.open("GET",url,false);
			xhttp.send();
			icon = document.getElementById(this.id + "_icon");
			icon.style.display = 'inline';	
		};
		inp.value = "Validate CVE";	
		var f = document.createElement('div');
		f.innerHTML = '<a href="cve/'+obj[i].cve_id+'.txt" id="'+obj[i].cve_id+'_icon" style="margin:0 20px 0 0;display:none;" download><i style="font-size:24px" class="fa">&#xf15b;</i></a>'
		f.appendChild(inp);
		td.appendChild(f);
		tr.appendChild(th);
		tr.appendChild(td);
		tab.appendChild(tr);
	}
}


