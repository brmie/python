$(function(){
	// location.pathname ==> /list/1/

	var nowPageNum = location.pathname.split('/')[2];
	var nowPage = $(".pageNum"+nowPageNum);

	nowPage.addClass('nowPage');

	var pagingWidth = $(".page").css('width');

	alert(pagingWidth.split('px')[0]);

	$(".paging").css('width', pagingWidth*2+'px');

	alert(pagingWidth*2+'px')
})