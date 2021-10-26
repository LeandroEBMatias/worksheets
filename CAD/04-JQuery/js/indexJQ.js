$(document).ready(function () {

  var $KitchenTemp = $("#kitchenTemp")
  var $LivingRoomTemp = $("#livingRoomTemp")
  var $clock = $("#nowTime")
  var $date = $("#todaysDate")

  change("#iconKitchenLight", "#iconKitchenBulb ")
  change("#iconCeilingLight", "#iconCeilingBulb ")
  change("#iconAmbientLight", "#iconAmbientBulb ")
  change("#iconAmbientMusic", "#iconAmbientMusicNote")
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


function change(sw, bulb) {
  var $switch = $(sw)
  var $bulb = $(bulb)
  $switch.click(function (e) {
    // console.log(e)
    if (e.target.id == "iconAmbientMusic") {
      $bulb.toggleClass("fa-volume-mute text-danger")
      $bulb.toggleClass("fa-music text-primary")
    }
    else {
      $switch.toggleClass("fa-toggle-off")
      $switch.toggleClass("fa-toggle-on")
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

