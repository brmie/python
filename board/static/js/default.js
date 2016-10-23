$(function(){
	// location.pathname ==> /list/1/



	var nowPageNum = location.pathname.split('/')[2];
	var pages = $('.page');

	alert(pages);

	for(var i=0; i<pages.length; i++){
		alert(pages[i]);

		pages[i].addClass('nowPage')

		// if(pages[i].split('list/')[1] == nowPageNum+'/'){
		// 	alert("hohoho");
		// }

		// if($pages[i].hasClass("pageNum"+nowPageNum)){
		// 	$pages[i].addClass('nowPage');
		// 	alert('hoho1');
		// } else {
		// 	if($pages[i].hasClass('nowPage')){
		// 		$pages[i].removeClass('nowPage');
		// 		alert('hoho2');
		// 	}
		// }
	}
})