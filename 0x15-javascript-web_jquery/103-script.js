$(document).ready(() => {
  $('#btn_translate').on('click', () => {
    translateHello();
  });

  $('#language_code').on('keyup', (event) => {
    if (event.key === 'Enter') {
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('#language_code').val();

    $.when(
      $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + languageCode),
      $.ready
    ).done((data) => {
      $('#hello').text(data.hello);
    });
  }
});
