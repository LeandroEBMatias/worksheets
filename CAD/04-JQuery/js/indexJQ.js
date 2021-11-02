



$(document).ready(function () {

  var $KitchenTemp = $("#kitchenTemp")
  var $LivingRoomTemp = $("#livingRoomTemp")
  var $clock = $("#nowTime")
  var $date = $("#todaysDate")
  var $city = $("#city")
  var $weatherAPI = "https://api.openweathermap.org/data/2.5/weather?q="
  var $weatherAPIKey = "&units=metric&appid=6ff844fd15a7d0e741f91bdedf53ff13"
  var $currentTemp = $("#nowTemperature");
  var $maxTemp = $("#maxTemperature");
  var $minTemp = $("#minTemperature")
  var $Humidity = $("#humidity")
  var $sunRiseTime = $("#sunRiseTime")
  var $sunSetTime = $("#sunSetTime")
  var $Search = $("#SearchButton")

  getWeather($weatherAPI, $city, $weatherAPIKey, $currentTemp, $maxTemp, $minTemp, $Humidity, $sunRiseTime, $sunSetTime)
  change("#iconKitchenLight", "#iconKitchenBulb ")
  change("#iconCeilingLight", "#iconCeilingBulb ")
  change("#iconAmbientLight", "#iconAmbientBulb ")
  change("#iconAmbientMusic", "#iconAmbientMusicNote")
  updateCity($Search, $weatherAPI, $city, $weatherAPIKey, $currentTemp, $maxTemp, $minTemp, $Humidity, $sunRiseTime, $sunSetTime)
  setTemp($KitchenTemp);
  setTemp($LivingRoomTemp);
  setInterval(function () {
    setTemp($KitchenTemp);
  }, 5000);
  setInterval(function () {
    setTemp($LivingRoomTemp);
  }, 5000);
  setInterval(function () {
    doTime($clock)
  }, 1000);
  doDate($date);
});


function setTemp($param) {
  min = 10
  max = 30
  console.log("Number Changed")
  randomValue = (Math.random() * (max - min) + min).toFixed(2);
  $param.text(randomValue.toString().concat(' ºC'))
}

function updateCity($Search, $weatherAPI, $city, $weatherAPIKey, $currentTemp, $maxTemp, $minTemp, $Humidity, $sunRiseTime, $sunSetTime) {
  $Search.click(function (e) {
    getWeather($weatherAPI, $city, $weatherAPIKey, $currentTemp, $maxTemp, $minTemp, $Humidity, $sunRiseTime, $sunSetTime)
  })

}

function change(sw, bulb) {
  var $switch = $(sw)
  var $bulb = $(bulb)
  $switch.click(function (e) {
    $switch.toggleClass("fa-toggle-off")
    $switch.toggleClass("fa-toggle-on")
    // console.log(e)
    if (e.target.id == "iconAmbientMusic") {
      $bulb.toggleClass("fa-volume-mute text-danger")
      $bulb.toggleClass("fa-music text-primary")
    }
    else {
      $bulb.toggleClass("fas text-warning")
      $bulb.toggleClass("far")
    }
    // cenas
  });
}

function doDate($date) {
  var now = new Date();
  var str = now.getDate() + "/" + (now.getMonth() + 1) + "/" + now.getFullYear()
  $date.text(str);
}

function doTime($clock) {
  console.log("Time Changed")
  var now = new Date();
  var str = now.getHours() + ":" + (now.getMinutes()) + ":" + now.getSeconds();
  $clock.text(str);
}

function getWeather($weatherAPI, $city, $weatherAPIKey, $currentTemp, $maxTemp, $minTemp, $Humidity, $sunRiseTime, $sunSetTime) {
  $.get($weatherAPI + $city.val() + $weatherAPIKey,
    function (data) {
      $currentTemp.html(data.main.temp.toString().concat(' ºC'));
      $maxTemp.html(data.main.temp_max.toString().concat(' ºC'));
      $minTemp.html(data.main.temp_min.toString().concat(' ºC'));
      $Humidity.html(data.main.humidity.toString().concat('% RH'));
      unixToTime(data.sys.sunrise, $sunRiseTime)
      unixToTime(data.sys.sunset, $sunSetTime);
      console.log(data)
    });
}

function unixToTime(unixTimeStamp, $value) {
  var date = new Date(unixTimeStamp * 1000);
  var hours = date.getHours();
  // Minutes part from the timestamp
  var minutes = "0" + date.getMinutes();
  // Seconds part from the timestamp
  var seconds = "0" + date.getSeconds();
  var formatTime = (hours + ' : ' + minutes.substr(-2) + ' : ' + seconds.substr(-2)).toString().concat(' GMT');
  $value.html(formatTime);
}


