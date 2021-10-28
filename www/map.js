function get_lat(ip){
  let url = 'https://ipapi.co/' + ip + '/latlong/'

  fetch(url)
  .then(function(response) {
    response.text().then(txt => {
      const strAry = txt.split(',');
      const lat = strAry[0];
      const lng = strAry[1];
      console.log(lat);
      console.log(lng);

      if(lat != 'None'){
        draw_map(lng, lat);
      }
      else{
        draw_map(120.472, 23.558);
      }
    });
  })
  .catch(function(error) {
    console.log(error);
  });
}

function lat(ip){
	url = "lat.php?ip="+ip;
	xhttp = new XMLHttpRequest();
	xhttp.open("GET",url,false);
	xhttp.send();
	console.log(JSON.parse(xhttp.responseText));
	res = JSON.parse(xhttp.responseText);
	console.log(res["latitude"]);
	console.log(res["longitude"]);
	ip1 = ip.split('.')[0];
	ip2 = ip.split('.')[1];
	if(ip1 == '140' && ip2 == '123'){
		draw_map(120.472,23.558);
	}else if(ip1 == '140' && ip2 == '115'){
		draw_map(121.190733,24.969367);
	}else{
		draw_map(res["longitude"],res["latitude"]);
	}
}

function draw_map(lng, lat){
  mapboxgl.accessToken = 'pk.eyJ1IjoiaW90c2Nhbm5lcmNjdSIsImEiOiJja3A3ODZ5dmUwMTZjMndwOXQxMnJzZXFyIn0.daz9mAb7Zzh9m-a7a4BINA';
    var map = new mapboxgl.Map({
      container: 'map', // container id
      style: 'mapbox://styles/mapbox/streets-v11', // style URL
      center: [lng, lat], // starting position [lng, lat]
      zoom: 14 // starting zoom
  });
}
