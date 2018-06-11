var image_g = undefined;
var tekst_g = undefined;

function render(){
	var image = document.getElementById("image").value;
	var tekst = document.getElementById("tekst").value;
	if(image && (tekst !== tekst_g || image !== image_g)){
		image_g = image;
		tekst_g = tekst;  
		document.getElementById("tekst").value;
		var http = new XMLHttpRequest();
		var url = '/generate/base64';
		var params = 'image=' + image + '&tekst=' + tekst;
		http.open('POST', url, true);

		//Send the proper header information along with the request
		http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

		http.onreadystatechange = function() {//Call a function when the state changes.
			if(http.readyState == 4 && http.status == 200) {
				var result = document.getElementById("result");
				var div = document.createElement("div");
				div.innerHTML = http.responseText;
				div.style.opacity = 0;
				result.appendChild(div);
				while (result.childElementCount > 2 && result.firstChild.style.opacity === 1) {
					result.removeChild(result.firstChild);
				}
				setTimeout(function(){
					div.style.opacity = 1;
				},5);
			}
		}
		http.send(params);
	}
}

if( document.readyState === 'complete' ) {
    startRender();
} else {
    document.addEventListener('DOMContentLoaded', startRender, false);
}

function startRender() {
	var image = document.getElementById("image");
	image.addEventListener("click", render);
	image.addEventListener("change", render);
	var tekst = document.getElementById("tekst");
	tekst.addEventListener("input", render);
	render();
}