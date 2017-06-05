$(window).load(function(){
	//控制图片大小
	var $img = $(".main img");
	$img.each(function() {
		if($(this).width() > 540) {
			var imgowidth = $(this).width();
			var imgoheight = $(this).height();
			$(this).width(540).height(Math.round(540*(imgoheight/imgowidth)));
		}
	});
});