import socketserver
import random
from keras.models import load_model
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
import cv2

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):

        print('connected')
        socket = self.request
        num = random.random() * 100000
        file_name = str(int(num)) + '.png'
        with open(file_name, 'wb') as image_file:
            tempData=None
            while True:
                data=socket.recv(1024)
                if not data:
                    break
                image_file.write(data)
        print('download complete')
        img = cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)


        # 이미지 리사이징
        img = cv2.resize(255-img, (28,28))
        test_data = img.flatten() / 255.0
        test_data = img.reshape((1, 28, 28, 1))

        # 모델 불러오기
        model = load_model('MNIST_CNN_model_epochs50.h5')

        # 클래스 예측 함수에 가공된 테스트 데이터 넣어 결과 도출
        predict_x = model.predict(test_data)
        res = np.argmax(predict_x,axis = 1)

        print(res)
        socket.close()



if __name__=="__main__":
    HOST, PORT = "192.168.0.2", 9999
    server = socketserver.TCPServer((HOST,PORT),RequestHandler)
    print('listen...')
            # 이미지 불러오기
    

    server.serve_forever()
