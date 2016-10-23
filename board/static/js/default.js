$(function(){
	// location.pathname ==> /list/1/

	alert('hohoho');

	var nowPageNum = location.pathname.split('/')[2];
	var $pages = $('.pages');

	for(var i=0; i<$pages.length; i++){
		if($pages[i].hasClass("pageNum"+nowPageNum)){
			$pages[i].addClass('nowPage');
			alert('hoho1');
		} else {
			if($pages[i].hasClass('nowPage')){
				$pages[i].removeClass('nowPage');
				alert('hoho2');
			}
		}
	}
})