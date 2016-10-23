window.onload = function(){
	// location.pathname ==> /list/1/
	var str = location.pathname;
	alert(str.split('/')[2]);
	// document.getElementsByClassName(location.pathname)
}