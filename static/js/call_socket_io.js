if (typeof io !== 'undefined') {
    console.log('Socket.IO library loaded successfully');
} else {
    console.error('Socket.IO library failed to load');
}

var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    console.log('Connected to server');
});

function sendMessage() {
    var message = "Hello, server!";
    socket.emit('message_from_client', message);
    console.log('Sent message to server:', message);
}

socket.on('message_from_server', function(message) {
    console.log('Received message from server:', message);
});

socket.on('new_message', function(message) {
    var messagesList = document.getElementById('messages');
    var newMessage = document.createElement('li');
    newMessage.textContent = message;
    messagesList.appendChild(newMessage);
});

socket.on('initial_messages', function(messages) {
    var messagesList = document.getElementById('messages');
    messagesList.innerHTML = '';
    for (var i = 0; i < messages.length; i++) {
        var messageItem = document.createElement('li');
        messageItem.textContent = messages[i];
        messagesList.appendChild(messageItem);
    }
});