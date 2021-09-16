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

function draw_map(lng, lat){
  mapboxgl.accessToken = 'pk.eyJ1IjoiaW90c2Nhbm5lcmNjdSIsImEiOiJja3A3ODZ5dmUwMTZjMndwOXQxMnJzZXFyIn0.daz9mAb7Zzh9m-a7a4BINA';
    var map = new mapboxgl.Map({
      container: 'map', // container id
      style: 'mapbox://styles/mapbox/streets-v11', // style URL
      // center: [120.472, 23.558], // starting position [lng, lat]
      center: [lng, lat], // starting position [lng, lat]
      zoom: 16 // starting zoom
  });
}
