window.onload = function(){
	// location.pathname ==> /list/1/

	var nowPageNum = location.pathname.split('/')[2];
	var pages = document.getElementsByClassName('page');

	for(var i=0; i<pages.length; i++){
		if(pages[i]==nowPageNum){
			alert('hoho1');
			pages[i].addClass('nowPage');
		} else {
			if(pages[i].hasClass('nowPage')){
				alert('hoho2');
				pages[i].removeClass('nowPage');
			}
		}
	}
}