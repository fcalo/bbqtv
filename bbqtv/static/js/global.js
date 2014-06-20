$(function () {
	/* 
	get snap amount programmatically or just set it directly (e.g. "273") 
	in this example, the snap amount is list item's (li) outer-width (width+margins)
	*/
	var amount=10;
	
	$("#content-1").mCustomScrollbar({
		axis:"x",
		theme:"inset",
		advanced:{
			autoExpandHorizontalScroll:true
		},
		scrollButtons:{
			enable:true,
			scrollType:"stepped"
		},
		keyboard:{scrollType:"stepped"},
		snapAmount:10,
		mouseWheel:{scrollAmount:10}
	});
	//~ var div_html = '<div class="mCSB_scrollTools mCSB_1_scrollbar mCS-inset mCSB_scrollTools_horizontal" id="mCSB_1_scrollbar_horizontal" style="display: block;"><a oncontextmenu="return false;" class="mCSB_buttonLeft" href="#" style="display: block;"></a><div class="mCSB_draggerContainer"><div oncontextmenu="return false;" style="position: absolute; min-width: 30px; display: block; width: 115px; max-width: 1242px;" class="mCSB_dragger" id="mCSB_1_dragger_horizontal"><div class="mCSB_dragger_bar"></div></div><div class="mCSB_draggerRail"></div></div><a oncontextmenu="return false;" class="mCSB_buttonRight" href="#" style="display: block;"></a></div>'
	//~ $("#content-1").children().children().before(div_html +  $("#mCSB_1_scrollbar_horizontal").html() +"</div>");
	
}()); 
