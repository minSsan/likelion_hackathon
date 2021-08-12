const roomName = JSON.parse(document.getElementById('room-name').textContent);
const username = document.getElementById('user-name').innerText + " : ";

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);
const chatLog = document.getElementById('chat-log')

window.onload = function() {
    chatLog.scrollTop = chatLog.scrollHeight
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const text = username + document.getElementById('chat-message-input').value
    if (!text) return

    fetch("/chat/" + roomName + "/", { 
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            text,
        })
    })

    const messageInputDom = document.querySelector('#chat-message-input');
    const message = username + messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';

    chatLog.scrollTop = chatLog.scrollHeight
};