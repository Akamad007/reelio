$(function(){
	$(".trash").on("click",function(event){
		
		event.preventDefault();
		var id = $(this).attr("href");
		
		var url = "/home/api/tasks/"+id;
		var data ={"is_active":"False"}; 
		ajaxData(url,data,"PATCH");
	
	});

});