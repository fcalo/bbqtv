function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
    return pattern.test(emailAddress);
};

$(function () {
    
    $("#send_contact").click(function(){
        
        mandatory_keys = ["email", "msg"]
		params_keys = ["name", "email", "subject", "msg"]
		
		var error = false;
		
		for(i in mandatory_keys){
			k = mandatory_keys[i];
			if ($("#" + k).val() == ""){
				$("#" + k).parent().parent().addClass("has-error");
				error = true;
			}else{
				$("#" + k).parent().parent().removeClass("has-error");
			}
		}
		if (!isValidEmailAddress($("#email").val())){
			$("#email").parent().parent().addClass("has-error");
			error = true;
		}
		
		if (!error){
			params = Object()
			for(i in params_keys){
				k = params_keys[i];
				params[k] = $("#" + k).val();
			}
        
        
             $.ajax({
                data:  params,
                url:   '/contact',
                type:  'post',
                dataType: 'json',
                beforeSend: function () {
                        $("#resultado").html("Procesando, espere por favor...");
                },
                success:  function (response) {
                    $("#contact-modal").modal('hide');
                    $("#alert").html('<div class="alert alert-success"><a href="#" class="close" data-dismiss="alert">&times;</a><span></span></div>');
                    $("#alert .alert span").html(response['info']);
                    $("#alert .alert").removeClass("alert-success");
                    $("#alert .alert").removeClass("alert-danger");
                    if (response['ok']){
                        $("#alert .alert").addClass("alert-success");
                    }else{
                        $("#alert .alert").addClass("alert-danger");
                    }
                    $("#alert").show();
                }
            });
        }
    });
    
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
