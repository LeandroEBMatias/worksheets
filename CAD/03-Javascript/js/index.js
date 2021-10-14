var app = (function () {
    'use strict';
    var timeRefresh = 5
    setTimeout(setTemp('kitchenTemp',
        getRandomArbitrary(10, 30).toFixed(2)), timeRefresh * 6 * Math.pow(10, 4));
    setTimeout(setTemp('livingRoomTemp',
        getRandomArbitrary(10, 30).toFixed(2)), timeRefresh * 6 * Math.pow(10, 4));
    change('kitchenLight', 'iconKitchenLight', 'iconKitchenBulb')
    change('CeilingLight', 'iconCeilingLight', 'iconCeilingBulb')
    change('AmbientLight', 'iconAmbientLight', 'iconAmbientBulb')
    setInterval(doDate, 1000);
    setInterval(doTime, 1000);


})();


function change(id_button, id_button_icon, id_bulb_icon) {
    // botão kitchen light
    var lightToggleButton =
        document.getElementById(id_button);

    // icon kitchen but
    var iconToggleButton =
        document.getElementById(id_button_icon);

    // icon kitchen lampada
    var iconBulb =
        document.getElementById(id_bulb_icon);

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

            classesIconLightBulb.remove('fas');
            classesIconLightBulb.add('far');

        } else {
            classesIconToggleButton.remove('fa-toggle-on');
            classesIconToggleButton.add('fa-toggle-off');

            classesIconLightBulb.remove('far');
            classesIconLightBulb.add('fas');
        }
    }
}



function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

function setTemp(id_TempDiv, randomValue) {
    document.getElementById(id_TempDiv).innerHTML = randomValue.concat(' ºC');
}

function doDate() {
    var now = new Date();
    var str = now.getDate() + "/" + (now.getMonth() + 1) + "/" + now.getFullYear()
    document.getElementById("todaysDate").innerHTML = str;
}

function doTime() {
    var now = new Date();
    var str = now.getHours() + ":" + (now.getMinutes()) + ":" + now.getSeconds();
    document.getElementById("nowTime").innerHTML = str;
}
now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();

// console.log(app.a);
// console.log(app.a)

// OU
// function main() {
// };
// main();
// console.log(app.a)