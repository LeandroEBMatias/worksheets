$(document).ready(function () {

  var now = new Date();
  var str = now.getHours() + ":" + (now.getMinutes()) + ":" + now.getSeconds();
  // $("nowTime").text(str);
  $("#iconAmbientMusic").click(function () {

    console.log("click")
  });
});

