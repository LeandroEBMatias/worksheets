var app = (function () {
    'use strict';
    doTime()
    setTemp('kitchenTemp', 10, 30)
    setTemp('livingRoomTemp', 10, 30)
    // setInterval(setTemp('kitchenTemp',
    //     getRandomArbitrary(10, 30).toFixed(2)), 5000);
    setInterval(function () {
        setTemp('livingRoomTemp', 10, 30);
    }, 5000);
    setInterval(function () {
        setTemp('kitchenTemp', 10, 30);
    }, 5000);
    change('kitchenLight', 'iconKitchenLight', 'iconKitchenBulb')
    change('CeilingLight', 'iconCeilingLight', 'iconCeilingBulb')
    change('AmbientLight', 'iconAmbientLight', 'iconAmbientBulb')
    change('AmbientMusic', 'iconAmbientMusic', 'iconAmbientMusicNote')
    setInterval(doTime, 1000);
    doDate()



})();




function change(id_button, id_button_icon, id_bulb_icon) {
    // botão kitchen light
    var lightToggleButton =
        $(id_button);
    // document.getElementById(id_button);

    // icon kitchen but
    var iconToggleButton =
        $(id_button_icon)
    // document.getElementById(id_button_icon);

    // icon kitchen lampada
    var iconBulb =
        $(id_bulb_icon)
    // document.getElementById(id_bulb_icon);

    // obtem class list icon kitchen light
    var classesIconToggleButton =
        iconToggleButton.classList;

    // obtem class list icon kitchen lampada
    var classesIconLightBulb =
        iconBulb.classList;




    lightToggleButton.onclick = function () {


        if (classesIconToggleButton.contains('fa-toggle-off')) {

            classesIconToggleButton.remove('fa-toggle-off');
            classesIconToggleButton.add('fa-toggle-on');

            if (id_button == 'AmbientMusic') {
                classesIconLightBulb.remove('fa-volume-mute');
                classesIconLightBulb.add('fa-music');
                classesIconLightBulb.remove('text-danger')
                classesIconLightBulb.add('text-primary')
            }
            else {
                classesIconLightBulb.remove('far');
                classesIconLightBulb.add('fas');
                classesIconLightBulb.add('text-warning');
                // classesIconLightBulb.add('text');


            }


        } else {
            classesIconToggleButton.remove('fa-toggle-on');
            classesIconToggleButton.add('fa-toggle-off');

            if (id_button == 'AmbientMusic') {
                classesIconLightBulb.remove('fa-music');
                classesIconLightBulb.add('fa-volume-mute');
                classesIconLightBulb.remove('text-primary')
                classesIconLightBulb.add('text-danger')
            }
            else {
                classesIconLightBulb.remove('fas');
                classesIconLightBulb.add('far');
                classesIconLightBulb.remove('text-warning');


            }

        }
    }
}





function setTemp(id_TempDiv, min, max) {
    console.log("Number Changed")
    randomValue = (Math.random() * (max - min) + min).toFixed(2);
    document.getElementById(id_TempDiv).innerHTML = randomValue
        .toString().concat(' ºC');
}

function doDate() {
    var now = new Date();
    var str = now.getDate() + "/" + (now.getMonth() + 1) + "/" + now.getFullYear()
    document.getElementById("todaysDate").innerHTML = str;
}

function doTime() {
    console.log("Time Changed")
    var now = new Date();
    var str = now.getHours() + ":" + (now.getMinutes()) + ":" + now.getSeconds();
    document.getElementById("nowTime").innerHTML = str;
}

