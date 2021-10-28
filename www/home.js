function update(){
	table_id = document.getElementById("table_id").innerHTML;
	xhttp = new XMLHttpRequest();
	xhttp.open('GET','./update.php?table_id=' + table_id,true);
	xhttp.send();
	Swal.fire({
	  title: 'Start Updating',
	  text: 'We will have done as soon as possible',
	  confirmButtonText: 'confirm'
	})
}

//create the pie chart
function chart(){
	table_id = document.getElementById("table_id").innerHTML;
	xhttp = new XMLHttpRequest();
	url = "./get_db/device_num.php?table_id=" + table_id;
	xhttp.open("GET" , url , false);
	xhttp.send();
	res = JSON.parse(xhttp.responseText);
	console.log(res);

	total = res["router"] + res["printer"] + res["camera"] + res["nas"];
	router_ratio = res["router"] / total * 100;
	printer_ratio = res["printer"] / total * 100;
	camera_ratio = res["camera"] / total * 100;
	nas_ratio = res["nas"] / total * 100;

	router_ratio = router_ratio.toFixed(2);
	printer_ratio = printer_ratio.toFixed(2);
	camera_ratio = camera_ratio.toFixed(2);
	nas_ratio = nas_ratio.toFixed(2);

	var chart = new CanvasJS.Chart("chartContainer", {
		animationEnabled: true,
		title: {
			text: "IOT Device Type"
		},
		legend:{
			cursor: "pointer",
			itemclick: explodePie
		},
		data: [{
			type: "pie",
			showInLegend: true,
			toolTipContent: "{name}: <strong>{y}%</strong>",
			indexLabel: "{name} - {y}%",
			dataPoints: [
				{y: nas_ratio, name: "NAS" ,color: "#ff0000"},
				{y: router_ratio, name: "Router" ,color: "#ff4000"},
				{y: printer_ratio, name: "Printer" ,color: "#ff8000"},
				{y: camera_ratio, name: "Camera" ,color: "#ffbf00"},
			]
		}]
	});
	chart.render();

	var x = document.getElementById("search_result");
	if(x.style.display == "none") x.style.display = "block";

	//print the deivce number of different divice type
	document.getElementById("camera_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='camera_num'>" + res["camera"] + "</p>";
	document.getElementById("router_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='router_num'>" + res["router"] + "</p>";
	document.getElementById("printer_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='printer_num'>" + res["printer"] + "</p>";
	document.getElementById("nas_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='nas_num'>" + res["nas"] + "</p>";
	


	/*
	url = "../api/log/device/count.json";

	$.get(url,function(obj){
			//jquery return obj datatype
			//count ratio
			total = obj["router"] + obj["printer"] + obj["camera"] + obj["nas"];
			rou_ratio = obj["router"]/total*100;
			pri_ratio = obj["printer"]/total*100;
			cam_ratio = obj["camera"]/total*100;
			nas_ratio = obj["nas"]/total*100;

			rou_ratio = rou_ratio.toFixed(2);
			pri_ratio = pri_ratio.toFixed(2);
			cam_ratio = cam_ratio.toFixed(2);
			nas_ratio = nas_ratio.toFixed(2);
			
			var chart = new CanvasJS.Chart("chartContainer", {
				animationEnabled: true,
				title: {
					text: "IOT Device Type"
				},
				legend:{
					cursor: "pointer",
					itemclick: explodePie
				},
				data: [{
					type: "pie",
					showInLegend: true,
					toolTipContent: "{name}: <strong>{y}%</strong>",
					indexLabel: "{name} - {y}%",
					dataPoints: [
						{y: nas_ratio, name: "NAS" ,color: "#ff0000"},
						{y: rou_ratio, name: "Router" ,color: "#ff4000"},
						{y: pri_ratio, name: "Printer" ,color: "#ff8000"},
						{y: cam_ratio, name: "Camera" ,color: "#ffbf00"},
					]
				}]
			});
			chart.render();

			var x = document.getElementById("search_result");
			if(x.style.display == "none") x.style.display = "block";

			document.getElementById("camera_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='camera_num'>" + obj["camera"] + "</p>";
			document.getElementById("router_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='router_num'>" + obj["router"] + "</p>";
			document.getElementById("printer_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='printer_num'>" + obj["printer"] + "</p>";
			document.getElementById("nas_num").innerHTML = "<p class='card-text text-center fs-4 text-white' id='nas_num'>" + obj["nas"] + "</p>";
			
	})
	*/
}

function explodePie (e) {
	if(typeof (e.dataSeries.dataPoints[e.dataPointIndex].exploded) === "undefined" || !e.dataSeries.dataPoints[e.dataPointIndex].exploded) {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = true;
	} else {
		e.dataSeries.dataPoints[e.dataPointIndex].exploded = false;
	}
	e.chart.render();

}

function alertion(){
	table_id = document.getElementById("table_id").innerHTML;
	if(table_id==1){
		xhttp = new XMLHttpRequest();
		url = "./alert.json";
		xhttp.open('get',url,false);
		xhttp.send();
		alertObj = JSON.parse(xhttp.responseText);
		div = document.getElementById("alertion");
		table = document.createElement('table');
		tbody = document.createElement('tbody');
		for(i=0;i<alertObj.length;i++){
			tr = document.createElement('tr');
			td = document.createElement('td');
			button = document.createElement('button');
			button.setAttribute('class','btn btn-danger my-3');
			a = document.createElement('a');
			table_id = document.getElementById("table_id").innerHTML;
			ip = alertObj[i]["ip"];
			a.setAttribute('href','./ip.php?ip='+ip+'&&location=資工系&&table_id='+table_id);
			a.setAttribute('class','text-decoration-none');
			a.setAttribute('style','font-size:40px;color:#2B2B2B')
			a.innerHTML = ip;
			button.appendChild(a);
			td.appendChild(button);
			h5 = document.createElement('h5');
			h5.innerHTML = "<b>Port: </b>" + alertObj[i]["port"];
			td.appendChild(h5);
			h5 = document.createElement('h5');
			h5.innerHTML = "<b>CVE: </b>" + alertObj[i]["cve"];
			td.appendChild(h5);
			h5 = document.createElement('h5');
			h5.innerHTML = "<b>CVSS: </b>" + alertObj[i]["cvss"];
			td.appendChild(h5);
			h5 = document.createElement('h5');
			h5.innerHTML = "<b>Description:</b></br> " + alertObj[i]["description"];
			td.appendChild(h5);
			tr.appendChild(td);
		}
		tbody.appendChild(tr);
		table.appendChild(tbody);
		div.appendChild(table);
	}
}


window.onload = function(){
	chart();
	alertion();
}

