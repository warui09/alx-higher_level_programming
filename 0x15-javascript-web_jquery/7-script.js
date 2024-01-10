$.when(
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json'),
  $.ready
).done((data) => {
  $('#character').append(data[0].name);
});
