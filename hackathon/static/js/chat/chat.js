const roomName = JSON.parse(document.getElementById('room-name').textContent);
const username = document.getElementById('user-name').innerText;

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);
const chatLog = document.querySelector('.chat-log');

window.onload = function() {
    chatLog.scrollTop = chatLog.scrollHeight;

    
}

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('.chat-log').innerHTML += `                        <div class="right">
    <p class="chat-box">${data.message}</p>
    <div class="chat-box-tail"></div>
</div>`;
    chatLog.scrollTop = chatLog.scrollHeight;
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
    const text = document.getElementById('chat-message-input').value
    if (!(document.getElementById('chat-message-input').value)) return

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
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username,
    }));
    messageInputDom.value = '';

};