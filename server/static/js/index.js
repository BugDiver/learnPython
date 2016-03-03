var postComment = function(){
	$.post('comment',{comment : $('#comment').val()},function(response){
		$('.input').html(response);
	})
}
var onReady = function(){
	$('#post').click(function(){
		postComment();
	})
}
$(document).ready(onReady);
