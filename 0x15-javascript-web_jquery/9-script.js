$.when(
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr'),
  $.ready
).done((data) => {
  $('#hello').append(data[0].hello);
});
