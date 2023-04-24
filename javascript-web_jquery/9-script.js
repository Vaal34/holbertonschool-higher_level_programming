$.getJSON("https://stefanbohacek.com/hellosalut/?lang=fr", function(data){
    $('div').text(data.hello)
});