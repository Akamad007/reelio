$(function(){
	$("#logout").on("click",function(){
		event.preventDefault();
		data = "";
		var type = "GET";
		var url = "/login/api/user/logout/";
		ajaxData(url,data,type);
	});
});

$( document ).ajaxError(function( event, jqxhr, settings, thrownError ) {
	  if ( jqxhr.status == 500 ) {
		  location.reload();
	  }else if ( jqxhr.status == 404 ) {
		  location.reload();
	  }
	  else if ( jqxhr.status == 401 ) {
		  location.reload();
	  }
	  else if ( jqxhr.status == 400 ) {
		  location.reload();
	  }
	});

function ajaxData(url,data,type){
		$.ajax({			
			type:type,
            url: url,
            data: data,
            dataType: "application/json",
            statusCode: {
            	200: function (response) {
                	$(window).attr("location","/home/");			                   
                },
                201: function (response) {
                	$(window).attr("location","/home/");			                   
                },	
                202: function (response) {
                	$(window).attr("location","/home/");			                   
                },
			}
		})	
		
	}