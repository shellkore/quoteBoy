$(document).ready(function () {
	$('#copy').hide()
	$('#another').hide()
	function copyToClipboard(element) {
		console.log('func reached')
 var $temp = $("<input>");
 $("body").append($temp);
 $temp.val($(element).html()).select();
 document.execCommand("copy");
 $temp.remove();
}

	$('.fetch').click(function(){
		$('#result').text("Loading.....")
		var tagRequested = $("#tagInput").val();
		console.log(tagRequested)
		var url = 'https://quoteboy.herokuapp.com/quote'
		$.get(url,{tag:tagRequested}, function(data){
		console.log(data['quote'])
		$('#result').text(data['quote'])
		$('#another').show()
		$('#copy').show()
		});

		});

	$('#copy').click(function(){
		console.log('copy2clip')
		copyToClipboard("#result")
	});
});