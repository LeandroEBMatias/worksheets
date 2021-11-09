
var admin = require("firebase-admin");
var faker = require("faker");
var serviceAccount = require("./cad2122-2202579-firebase-adminsdk-3kmsc-74bcfa89db.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://cad2122-2202579-default-rtdb.europe-west1.firebasedatabase.app"
});

