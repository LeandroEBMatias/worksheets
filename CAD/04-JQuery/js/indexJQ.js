$(document).ready(function () {
  function change(sw, bulb) {
    var $switch = $(sw)
    var $bulb = $(bulb)
    $switch.click(function () {
      $switch.toggleClass("fa-toggle-off")
      $switch.toggleClass("fa-toggle-on")
      $bulb.toggleClass("fas text-warning")
      $bulb.toggleClass("far")
    });
  }

  change("#iconKitchenLight", "#iconKitchenBulb ")
  change("#iconCeilingLight", "#iconCeilingBulb ")
  change("#iconAmbientLight", "#iconAmbientBulb ")
  change('AmbientLight', 'iconAmbientLight', 'iconAmbientBulb')

});

