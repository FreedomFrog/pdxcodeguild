function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        $('#temp-text').text("Geolocation is not supported by this browser.");
        $('#cond-text').text("Geolocation is not supported by this browser.");
    }
}

let APIKEY = '13a106022d63ffd4ff4668b6cad93dc1';

function showPosition(position) {
    $.ajax({
            url: 'https://api.openweathermap.org/data/2.5/weather?',
            type: 'GET',
            data: {
                APPID: APIKEY,
                lat: position.coords.latitude,
                lon: position.coords.longitude,
                units: 'metric',
            },
            //dataType: "json",
            success: function (result, status, xhr) {
                $('#temp').text(result.main.temp);
                $('#conditions').text(result.weather[0].description);
                let icon = result.weather[0].icon;
                $('body').css({'background-image': `url(http://openweathermap.org/img/w/${icon}.png)`})
                console.log(result);
                console.log(status);
                console.log(xhr);
            },
            error: function (xhr, status, error) {
                alert("Result: " + status + " " + error + " " + xhr.status + " " + xhr.statusText)
            }
        }
    );
    $('#coordinates').html("Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude);
}

$(document).ready(function () {
    getLocation()

});


