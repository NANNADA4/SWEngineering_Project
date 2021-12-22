function CheckFileSize(file, Size) {
    maxSize = Size * 1024 * 1024;
    if (file.files[0].size > maxSize) {
        alert("5MB 미만의 이미지만 업로드 가능합니다.");
        return false;
    }
    return true;
}

var webSocket = new WebSocket("ws://127.0.0.1:9999");
var messageTextArea = document.getElementById("messageTextArea");

webSocket.onopen = function (message) {
    messageTextArea.value += "Server Connect";
};

webSocket.onmessage = function (message) {
    messageTextArea.value = message.data;
};

function sendMessage() {
    var message = document.getElementById("pictureMessage");
    webSocket.send(message.value);
    message.value = "";
}

function disconnect() {
    webSocket.close();
}
