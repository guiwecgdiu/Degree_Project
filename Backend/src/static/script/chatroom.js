
function send(){
        var x=document.getElementById("input").value
        document.getElementById("content").value=x
}


var chatQueue = [
    { username: "Arno", update: "Are you a idiot" },
    { username: "Trump", update: "Nobody Know..." },
    { username: "Arno", update: "Really?" },
    { username: "Trump", update: "Make China Great Again" }
];

  var currentChatIndex = 0;

// start the conversation
function start() {
    setTimeout(showNextMessage, 1500);
}


// show Messages
function showNextMessage() {

    //lazy check for need to continue to call.
    if(currentChatIndex < chatQueue.length) {
        //grab a tweet from the tweets array
        var currentChatObj = chatQueue[currentChatIndex];

        //makes a new div in computer memory
        var newElement = document.createElement("div");

        //write inside of the new element - the username and message
        newElement.innerHTML = "<span class='un'>" + currentChatObj.username + "</span>: " + currentChatObj.update;

        ///adds the element to the page - makes it visible.
        document.body.appendChild(newElement);

        currentChatIndex ++;

        //call this function again..
        setTimeout(showNextMessage, 700 + Math.random() * 3000);
    }
}
