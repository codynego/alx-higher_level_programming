$(document).ready(function(){
	$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
	  var characterName = data.name;
	  $("div#character").text(characterName);
	});
  });
  