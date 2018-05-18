import sys, os
sys.path.append(os.pardir)

import numpy as np
import pickle
from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
	(x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)
	return x_test, t_test

...
normalize : 입력 이미지의 픽셀 값을 0.0 ~ 1.0 사이의 값으로 정규화할지를 정한다.
flatten : 입력 이미지를 평탄하게, 1차원 배열로 만들지 정한다
one_hot_label 예)[0, 0, 1, 0, 0]과 같이 정답을 뜻하는 원소만 1이고(hot) 나머지는 모두 0인 배열
...

def init_network():
	with open("sample_weight.pkl", 'rb') as f:
		network = pickle.load(f)                # 프로그램 실행 중 특정 객체를 파일로 저장하는 기능

	return network

def predict(network, x):
	W1, W2, W3 = network['W1'], network['W2'], network['W3']
	b1, b2, b3 = network['b1'], network['b2'], network['b3']

	a1 = np.dot(x, W1) + b1
	z1 = sigmoid(a1)
	a2 = np.dot(z1, W2) + b2
	z2 = sigmoid(a2)
	a3 = np.dot(z2, W3) + b3
	y = softmax(a3)

	return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
	y = predict(network, x[i])
	p = np.argmax(y)
	if p == t[i]:
		accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))