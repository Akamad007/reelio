$(function(){
	$("form").on("submit",function(event){
		event.preventDefault();		
		var formData = $(this).serialize();	
		var type = "POST";
		var url = "/login/api/user/create/";
		ajaxData(url,formData,type);		
	});
});