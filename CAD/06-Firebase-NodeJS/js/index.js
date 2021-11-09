// Import CDN para ir buscar biblioteca da firebase
import { getDatabase, ref, onValue} from "https://www.gstatic.com/firebasejs/9.4.0/firebase-database.js";
const db = getDatabase();

$(document).ready(function () {
    // Método utilizado para ler dados da firebase -> Ver documentaçãp
    const starCountRef = ref(db, 'mensagens');
    onValue(starCountRef, (snapshot) => {
        const data = snapshot.val();
        // updateStarCount(postElement, data);
        $('<div />').appendTo('body').attr('class', 'alert alert-'.concat(data.type)).text(data.mensagens)
        console.log(data)
    });
    
});

