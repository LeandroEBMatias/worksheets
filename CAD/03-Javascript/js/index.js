var app = (function () {
    'use strict';

    // botão kitchen light
    var kitchenLight =
        document.getElementById('kitchenLight');

    // icon kitchen but
    var iconKitchenLight =
        document.getElementById('iconKitchenLight');

    // icon kitchen lampada
    var iconKitchenBulb =
        document.getElementById('iconKitchenBulb');

    // obtem class list icon kitchen light
    var classesIconKitchenLight =
        iconKitchenLight.classList;

    // obtem class list icon kitchen lampada
    var classesIconKitchenBulb =
        iconKitchenBulb.classList;


    kitchenLight.onclick = function () {

        if (classesIconKitchenLight.contains('fa-toggle-off')) {
            classesIconKitchenLight.remove('fa-toggle-off');
            classesIconKitchenLight.add('fa-toggle-on');

            classesIconKitchenBulb.remove('fas');
            classesIconKitchenBulb.add('far');

        } else {
            classesIconKitchenLight.remove('fa-toggle-on');
            classesIconKitchenLight.add('fa-toggle-off');

            classesIconKitchenBulb.remove('far');
            classesIconKitchenBulb.add('fas');
        }


    }


})();


// console.log(app.a);
// console.log(app.a)

// OU
// function main() {
// };
// main();
// console.log(app.a)