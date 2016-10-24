$(function(){
	// location.pathname ==> /list/1/

	var nowPageNum = location.pathname.split('/')[2];
	var nowPage = $(".pageNum"+nowPageNum);

	nowPage.addClass('nowPage');

	var pagingWidth = eval($(".page").css('width').split('px')[0]);

	alert(pagingWidth);

	$(".paging").css('width', pagingWidth*2+'px');

	alert(pagingWidth*2+'px')
})