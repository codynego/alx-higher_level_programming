$(document).ready(function() {
	$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
	  var movies = data.results;
	  var list = $("<ul></ul>"); // create the unordered list element
	  $.each(movies, function(index, movie) {
		var title = movie.title;
		var listItem = $("<li></li>").text(title); // create a list item for each movie title
		list.append(listItem); // append the list item to the list
	  });
	  $("#list_movies").replaceWith(list); // replace the existing unordered list with the new one
	});
  });
  