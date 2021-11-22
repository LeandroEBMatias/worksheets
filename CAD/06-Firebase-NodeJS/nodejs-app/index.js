
var admin = require("firebase-admin");
var faker = require("faker");
var serviceAccount = require("./cad2122-2202579-firebase-adminsdk-3kmsc-74bcfa89db.json");
var ArrayType = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://cad2122-2202579-default-rtdb.europe-west1.firebasedatabase.app"
});

function writeUserData(mensagem, type) {
  admin.database().ref('mensagens').push({
    mensagens: mensagem,
    type: type
  });
}
setInterval(function () {
  writeUserData(faker.lorem.sentence(15), faker.helpers.randomize(ArrayType))
}, 5000)