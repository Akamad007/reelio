$(function(){
	$("#login").on("click",function(event){		
		event.preventDefault();
		var formData = $("#loginForm").serialize();	
		var type = "POST";
		var url = "/login/api/user/login/";
		ajaxData(url,formData,type);
	});
});