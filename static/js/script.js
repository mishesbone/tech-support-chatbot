function sendMessage() {
    const message = document.getElementById('user-message').value;
    if (message.trim() !== "") {
        appendMessage(message, "user");
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'message=' + message
        })
        .then(response => response.json())
        .then(data => appendMessage(data.response, "bot"));
    }
}

function appendMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender);
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
