$(document).ready(() => {
  $('#btn_translate').on('click', () => {
    const languageCode = $('#language_code').val();

    $.when(
      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode),
      $.ready
    ).done((data) => {
      $('#hello').text(data.hello);
    });
  });
});
