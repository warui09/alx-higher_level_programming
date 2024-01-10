$.when(
  $.getJSON( "https://swapi-api.alx-tools.com/api/films/?format=json" ),
  $.ready
).done(( data ) => {
  films = data[0]["results"];
  for (let i = 0; i < films.length; i++)
    $("#list_movies").append(`<li>${films[i]["title"]}</li>`);
});
