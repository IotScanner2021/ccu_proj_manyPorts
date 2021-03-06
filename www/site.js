// users can seperate the ip by the ip table
function createTable(device){

	var xhttp = new XMLHttpRequest();
	//var url = "../api/log/device/" + device + ".json";
	var device = document.getElementById('device').innerHTML;
	var table_id = document.getElementById('table_id').innerHTML;
	var url = "./site_prod.php?device="+device+"&table_id="+table_id;
	console.log(url);
	xhttp.open("GET",url,false);
	xhttp.send();
	obj = JSON.parse(xhttp.responseText);
	
	// if users does not have the ip table 
	if(table_id != 1){
		var row = document.getElementById(device);
		var col = document.createElement('div');
		var card = document.createElement('div');
		card.setAttribute('class','card');
		card.setAttribute('style','width:1000px;margin:auto')
		var tab = document.createElement('table');
		tab.setAttribute('class','table');
			
		//thead
		var thead = document.createElement('thead');
		var tr = document.createElement('tr');
		var th1 = document.createElement('th');
		tr.appendChild(th1);
		var th2 = document.createElement('th');
		tr.appendChild(th2);
		var th = document.createElement('th');
		th.setAttribute('class','fs-3');
		th.innerHTML = "Uncategorized";
		tr.appendChild(th)
		var th3 = document.createElement('th');
		tr.appendChild(th3);
		var th4 = document.createElement('th');
		tr.appendChild(th4);
		thead.appendChild(tr);
		tab.appendChild(thead);
					
		//tbody
		var tbody = document.createElement('tbody');
		for(var i = 0 ; i < obj.length ; i+=5){
			tr = document.createElement('tr');
			for(var j=0;j<5 && i+j < obj.length;j++){
				td = document.createElement('td');
				td.setAttribute('class','fs-5');
				var a = document.createElement('a');
				a.setAttribute('class','text-decoration-none');
				var table_id = document.getElementById("table_id").innerHTML;
				a.href = "ip.php?ip=" + obj[i+j].ip + "&&location=" + "Undefined" + "&&table_id=" + table_id;
				a.innerHTML = obj[i+j].ip;
				td.appendChild(a);
				tr.appendChild(td);
			}
			tbody.appendChild(tr);
		}	
		tab.appendChild(tbody);
		card.appendChild(tab);
		col.appendChild(card);
		row.appendChild(col);
		
		return;
	}
	
	// if users have the ip table 
	
// table in third part
var dict1 = {
		'?????????' : [0 , 1 , 2 , 3 , 4 , 5 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 ,18 , 19 , 20 , 23 , 25 , 26 , 28 , 29 , 30 , 32 , 33 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 129 , 130 , 131 , 132 , 133 , 134 , 135 ,136 , 137 , 138 , 139 , 140 , 141 , 142 , 143 , 144 , 145 , 146 ,147 , 148 , 149 , 150 , 151 , 152 , 153 , 154 , 155 , 156 , 157 , 158 , 159 , 160 , 161 , 168 , 211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220 , 221 , 222 , 223 , 224 , 225 , 231 , 232 , 233 , 234 , 235 , 236 , 237 , 238 , 239 , 240 , 241 , 242 , 243 , 245 , 246 , 247 , 248 , 249 , 250 , 251 , 252 , 253 , 254 , 255],
		'?????????' : [6 , 7 , 8 , 27],
		'?????????' : [21 , 22 , 24],
		'?????????' : [31 , 37],
		'?????????' : [31],
		'?????????' : [31],
		'?????????' : [31],
		'?????????' : [31 , 33 , 35],
		'?????????' : [32 , 33 , 35 , 37],
		'?????????' : [33 , 40 , 51],
		'?????????' : [33],
		'?????????' : [33],
		'?????????' : [34],
		'???????????????' : [35],
		'???????????????' : [35],
		'????????????' : [35],
		'?????????' : [36],
		'????????????' : [38],
		'???????????????' : [38],
		'????????????' : [39],
		'????????????' : [40],
		'????????????' : [40],
		'????????????' : [40],
		'?????????' : [41],
		'?????????' : [42],
		'?????????' : [43],
		'?????????' : [44 , 45],
		'????????? ' : [46],
		'????????????' : [47],
		'?????????' : [48],
		'????????????' : [49 , 50],
		'?????????' : [61 , 62],
		'?????????' : [63 , 64 , 65 , 66 , 67 , 68 , 69 , 70],
		'?????????' : [71 , 72 , 73 , 74 , 75 , 76],
		'?????????' : [77 , 78 , 79 , 80 , 81 , 82]
};
var dict2 = {
		'?????????' : [83 , 84 , 85 , 86 , 87 , 88],
		'?????????' : [89 , 90 , 91 , 92],
		'?????????' : [91 , 92 , 106 , 107 , 108 , 109 , 110 , 111 , 112],
		'?????????' : [93 , 94],
		'?????????' : [95],
		'?????????' : [96 , 121 , 122 , 123 , 124 , 125],
		'?????????' : [97 , 101 , 102 , 103 , 104 , 105 , 230],
		'????????????' : [98 , 99 , 100],
		'?????????' : [113 , 114 , 115 , 116 , 117 , 118 , 119 , 120],
		'?????????' : [126 , 127 , 128],
		'?????????' : [162 , 163 , 164],
		'?????????' : [165 , 166 , 167],
		'?????????' : [169 , 170 , 171 , 172],
		'?????????' : [173 , 174 , 175],
		'????????????' : [176 , 177 , 178 , 179 , 180],
		'?????????' : [181 , 182 , 183 , 184],
		'?????????' : [185],
		'???????????????????????????????????????' : [186 , 187],
		'?????????' : [188 , 189],
		'?????????' : [190],
		'???????????????' : [191 , 192],
		'?????????' : [193],
		'?????????' : [194 , 195 , 196],
		'?????????' : [197],
		'?????????' : [198 , 199 , 200],
		'?????????' : [201],
		'?????????' : [202 , 208],
		'?????????' : [203 , 207],
		'?????????' : [204 , 209 , 210],
		'????????????' : [205],
		'????????????' : [206],
		'????????????' : [226 , 227 , 228 ,229],
		'?????????' : [226],
		'????????????' : [244]
};

// table in fourth part
var dict_31 = {
		'?????????' : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50],
		'?????????' : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220],
		'?????????' : [51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 100] ,
		'?????????' : [121 , 122 , 123 , 124 , 125 , 126 , 127 , 128 , 129 , 130 , 131 , 132 , 133 , 134 , 135 , 136 , 137 , 138 , 139 , 140 , 141 , 142143 , 144 , 145 , 146 , 147 , 148 , 149 , 150 , 151 , 152 , 153 , 154 , 155 , 156 , 157 , 158 , 159 , 160 , 161 , 162 , 163 , 164 , 165 , 166 , 167 , 168 , 169 , 170 , 249]
};

var dict_32 = {
		'?????????' : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91],
		'?????????' : [101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110 , 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118 , 119 , 120 , 121 , 122 , 123 , 124 , 125 , 126 , 127 , 128 , 129 , 130 , 131 , 132 , 133 , 134 , 135 , 136 , 137 , 138 , 139 , 140]
};

var dict_33 = {
		'?????????' : [21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 100 , 101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110 , 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118 , 119 , 120 , 121 , 122 , 123 , 124 , 125 , 126 , 127 , 128 , 129 , 130 , 131 , 132 , 133 , 134 , 135 , 136 , 137 , 138 , 139 , 140 , 181 , 182 , 183 , 184 , 185 , 186 , 187 , 188 , 189 , 190 , 191 , 192 , 193 , 194 , 195 , 196 , 197 , 198 , 199 , 200] , 
		'?????????' : [71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220],
		'?????????' : [141 , 142 , 143 , 144 , 145 , 146 , 147 , 148 , 149 , 150 , 151 , 152 , 153 , 154 , 155 , 156 , 157 , 158 , 159 , 160 , 161 , 162 , 163 , 164 , 165 , 166 , 167 , 168 , 169 , 170 , 171 , 172 , 173 , 174 , 175 , 176 , 177 , 178 , 179 , 180 , 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210],
		'?????????' : [211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220 , 221 , 222 , 223 , 224 , 225 , 226 , 227 , 228 , 229 , 230 , 231 , 232 , 233 , 234 , 235 , 236 , 237],
		'?????????' : [238 , 241 , 242 , 243 , 244 , 245 , 246 , 247 , 248 , 249],
		'?????????' : [252]
};

var dict_35 = {
		'?????????' : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 61 , 170 , 171 , 172 , 173 , 174 , 175 , 176 , 177 , 178 , 179 , 180 , 181 , 182 , 183 , 184 , 185 , 186 , 187 , 188 , 189 , 190 , 191 , 192 , 193 , 194 , 195 , 196 , 197 , 198 , 199 , 200 , 201 , 202 , 203 , 204 , 205 , 206 , 207 , 208 , 209 , 210 , 231],
		'???????????????' : [11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60],
		'???????????????' : [90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 100],
		'????????????' : [211 , 212 , 213 , 214 , 215 , 216 , 217 , 218 , 219 , 220 , 221 , 222 , 223 , 224 , 225 , 226 , 227 , 228 , 229 , 230],
		'?????????' : [252]
};

var dict_37 = {
		'?????????' : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 130 , 131 , 132 , 133 , 134 , 135 , 136 , 137 , 138 , 139 , 140 , 141 , 142 , 143 , 144 , 145 , 146 , 147 , 148 , 149 , 150 , 151 , 152 , 153 , 154 , 155 , 156 , 157 , 158 , 159 , 160 , 161 , 162 , 163 , 164 , 165 , 166 , 167 , 168 , 169 , 170 , 171 , 172 , 173 , 174 , 175 , 176 , 177 , 178 , 179 , 180 , 181 , 182 , 183 , 184 , 185 , 186 , 187 , 188 , 189 , 190 , 191 , 192 , 193 , 194],
		'?????????' : [100 , 101 , 102 , 103 , 104 , 105 , 106 , 107 , 108 , 109 , 110 , 111 , 112 , 113 , 114 , 115 , 116 , 117 , 118 , 119 , 120 , 121 , 122 , 123 , 124 , 125 , 126 , 127 , 128 , 129]
};

	var row = document.getElementById(device);
	for(i = 0 ; i < 2 ; i++){
		var col = document.createElement('div');
		col.setAttribute('class','two column');
		
		if(i == 0) dict = dict1;
		if(i == 1) dict = dict2;
		for(var site in dict){
			start = 0;
			//tbody
			for(j = 0 ; j < obj.length ; j++){
				for(k = 0 ; k < dict[site].length ; k++){
					insert = 0;
					//dict_31
					if(obj[j].ip.split('.')[2] == dict[site][k] && obj[j].ip.split('.')[2] == '31'){
						for(t = 0 ; t < dict_31[site].length ; t++){
							if(obj[j].ip.split('.')[3] == dict_31[site][t]){
								if(start == 0) start = 1;
								insert = 1;
							}
						}
					}
					//dict_32
					else if(obj[j].ip.split('.')[2] == dict[site][k] && obj[j].ip.split('.')[2] == '32'){
						for(t = 0 ; t < dict_32[site].length ; t++){
							if(obj[j].ip.split('.')[3] == dict_32[site][t]){
								if(start == 0) start = 1;
								insert = 1;
							}
						}
					}
					//dict_33
					else if(obj[j].ip.split('.')[2] == dict[site][k] && obj[j].ip.split('.')[2] == '33'){
						for(t = 0 ; t < dict_33[site].length ; t++){
							if(obj[j].ip.split('.')[3] == dict_33[site][t]){
								if(start == 0) start = 1;
								insert = 1;
							}
						}
					}
					//dict_35
					else if(obj[j].ip.split('.')[2] == dict[site][k] && obj[j].ip.split('.')[2] == '35'){
						for(t = 0 ; t < dict_35[site].length ; t++){
							if(obj[j].ip.split('.')[3] == dict_35[site][t]){
								if(start == 0) start = 1;
								insert = 1;
							}
						}
					}
					//dict_37
					else if(obj[j].ip.split('.')[2] == dict[site][k] && obj[j].ip.split('.')[2] == '37'){
						for(t = 0 ; t < dict_37[site].length ; t++){
							if(obj[j].ip.split('.')[3] == dict_37[site][t]){
								if(start == 0) start = 1;
								insert = 1;
							}
						}
					}
					else if(obj[j].ip.split('.')[2] == dict[site][k]){
						if(start == 0) start = 1;
						insert = 1;
					}

					// check the ip(it does NOT have already constructed the table)
					if(start == 1){
						start = 2;
						var card = document.createElement('div');
						card.setAttribute('class','card');
						var tab = document.createElement('table');
						tab.setAttribute('class','table');
				
						//thead
						var thead = document.createElement('thead');
						var tr = document.createElement('tr');
						var th = document.createElement('th');
						th.setAttribute('class','fs-3');
						th.innerHTML = site;
						tr.appendChild(th)
						thead.appendChild(tr);
						tab.appendChild(thead);
						
						//tbody
						var tbody = document.createElement('tbody');
					}
					// check the ip(it has already constructed the table, only need to insert)
					if(insert == 1){
						tr = document.createElement('tr');
						td = document.createElement('td');
						td.setAttribute('class','fs-5');
						var a = document.createElement('a');
						a.setAttribute('class','text-decoration-none');
						var table_id = document.getElementById("table_id").innerHTML;
						a.href = "ip.php?ip=" + obj[j].ip + "&&location=" + site + "&&table_id=" + table_id;
						a.innerHTML = obj[j].ip;
						td.appendChild(a);
						tr.appendChild(td);
						tbody.appendChild(tr);
					}		
				}
			}
			// the site does NOT have device, so NOT to construct the table.
			if(start != 0){
				tab.appendChild(tbody);
				card.appendChild(tab);
				col.appendChild(card);
			}
		}
		//insert into row
		row.appendChild(col);
	}	
}


window.onload = function(){
	device = document.getElementsByName("device")[0].id;
	createTable(device);
}
