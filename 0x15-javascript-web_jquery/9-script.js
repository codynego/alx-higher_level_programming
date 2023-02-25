$(document).ready(function() {
	$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function(data) {
	  var hello = data.hello;
	  $("#hello").text(hello); // set the text content of the div with ID "hello"
	});
  });
  