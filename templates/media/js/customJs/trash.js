$(function(){
	$(".restore").on("click",function(event){
		event.preventDefault();
		var id = $(this).attr("href");		
		var url = "/home/api/tasks/"+id;
		var data ={"is_active":"True"}; 
		ajaxData(url,data,"PATCH");
	});
	$(".delete").on("click",function(event){			
		event.preventDefault();
		var id = $(this).attr("href");		
		var url = "/home/api/tasks/"+id;
		var data ={"is_deleted":"True"}; 
		ajaxData(url,data,"PATCH");
		
	});

});