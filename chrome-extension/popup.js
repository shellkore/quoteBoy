$(document).ready(function () {
	$('.action-button').hide()


	function copyToClipboard(element) {
		console.log('func reached')
		var $temp = $("<input>");
		$("body").append($temp);
		$temp.val($(element).html()).select();
		document.execCommand("copy");
		$temp.remove();
	}

	$('.fetch').click(function () {
		$('#result').text("Loading.....");
		$('.action-button').hide()
		$('#copy').text('copy');
		var tagRequested = $("#tagInput").val();
		// console.log(tagRequested)
		var url = 'https://quoteboy.herokuapp.com/quote'
		$.get(url, { tag: tagRequested }, function (data) {
			$('.action-button').show();

			const qoute = data['quote'];
			const project_link="https://github.com/shellkore/quoteBoy";

			$('#result').text(qoute) // console.log(qoute)

			$("#twitter").attr("href", `https://twitter.com/intent/tweet?url=${project_link}&text=${qoute}`);
			$("#facebook").attr("href", `https://www.facebook.com/sharer/sharer.php?u=${project_link}&quote=${qoute}`);
			$("#reddit").attr("href", `https://www.reddit.com/submit?url=${qoute}`);
			$("#linkedin").attr("href", `https://www.linkedin.com/sharing/share-offsite/?url=${project_link}&summary=${qoute}`); //without authentic API you can only share URL on linkedin not text 

		});

	});

	$('#copy').click(function () {
		console.log('copy2clip')

		copyToClipboard("#result")
		$('#copy').text('copied');
	});
});
