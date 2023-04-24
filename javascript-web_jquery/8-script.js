$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
    $.each(data.results, function(results){
        $('UL#list_movies').append($("<li>").$text(results.title))
    });
});
