from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

# 필요 라이브러리 호출
import numpy
import tensorflow as tf

# 데이터 셋 호출
from keras.datasets import mnist

# 실행 시마다 같은 결과값 도출을 위한 시드 설정
numpy.random.seed(0)
tf.random.set_seed(0)

# 데이터를 불러와서 각 변수에 저장
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 학습에 적합한 형태로 데이터 가공
X_train = X_train.reshape(X_train.shape[0], 784).astype("float32") / 255
X_test = X_test.reshape(X_test.shape[0], 784).astype("float32") / 255

# 클래스를 학습에 이용하기 위해 데이터 가공
Y_train = np_utils.to_categorical(Y_train, 10)
Y_test = np_utils.to_categorical(Y_test, 10)

# 딥러닝 모델 구조 설정(2개층, 512개의 뉴런 연결, 10개 클래스 출력 뉴런, 784개 픽셀 input 값, relu와 softmax 활성화 함수 이용)
model = Sequential()
model.add(Dense(512, input_dim=784, activation="relu"))
model.add(Dense(10, activation="softmax"))

# 딥러닝 구조 설정(loss 옵션을 다중 클래스에 적합한 categorical_crossentropy, 옵티마이저는 adam 설정)
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 모델 실행(X_test, Y_test로 검증, 200개씩 30번 학습)
model.fit(
    X_train,
    Y_train,
    validation_data=(X_test, Y_test),
    epochs=30,
    batch_size=200,
    verbose=2,
)

# 학습 정확도, 검증 정확도 출력
print("\nAccuracy: {:.4f}".format(model.evaluate(X_train, Y_train)[1]))
print("\nVal_Accuracy: {:.4f}".format(model.evaluate(X_test, Y_test)[1]))

# 모델 저장
model.save("Predict_Model.h5")
