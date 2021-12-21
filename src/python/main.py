import socketserver
import threading
import random


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):

        # get socket request
        socket = self.request

        # set file name
        num = random.random() * 100000
        file_name = "image_temp/file_" + str(int(num)) + ".jpg"

        # get image file size from client
        file_size = socket.recv(1024)
        socket.sendall(file_size)
        print("set file size : " + file_size)

        # get image file byte stream from client
        # make empty image file
        with open(file_name, "wb") as image_file:
            data_tmp = None
            while True:
                # save image file from client stream
                data = socket.recv(1024)
                image_file.write(data)
                data_tmp += data
                if (data_tmp.__len__()) * 100 == int(file_size):
                    # check image file size
                    # print('received file size : {}'.format(data_tmp.__len__())*100)
                    break

        print("received & save image : " + file_name)
        img = cv2.imread("test_image.png", cv2.IMREAD_GRAYSCALE)

        # 이미지 리사이징
        img = cv2.resize(255 - img, (28, 28))
        test_data = img.flatten() / 255.0
        test_data = img.reshape((1, 28, 28, 1))

        # 모델 불러오기
        model = load_model("MNIST_CNN_model_epochs30.h5")

        # 클래스 예측 함수에 가공된 테스트 데이터 넣어 결과 도출
        predict_x = model.predict(test_data)
        res = np.argmax(predict_x, axis=1)

        socket.close()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 8000

    server = socketserver.TCPServer((HOST, PORT), RequestHandler)

    print("Socket is now listening ...")
    server_thread = threading.Thread(target=server.serve_forever())
    server_thread.setDaemon(True)
    server_thread.start()
