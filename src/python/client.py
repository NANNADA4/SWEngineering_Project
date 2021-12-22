import socket

IP = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((IP, PORT))
    print("연결성공")
    file_name = "test_image.png"
    tempData = 0
    sendfile = open(file_name, "rb")
    i = sendfile.read(1024)
    while i:
        print("sending")
        clientSocket.send(i)
        i = sendfile.read(1024)
    sendfile.close()
    print("done")
    clientSocket.close()
