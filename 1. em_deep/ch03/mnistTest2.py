import sys, os
sys.path.append(os.pardir)

import numpy as np
import pickle
import matplotlib.pyplot as plt

from dataset.mnist import load_mnist
from common.functions import sigmoid, softmax


def get_data():
	(x_train, t_train), (x_test, t_test) = load_mnist(normalize = True, flatten = True, one_hot_label = False)
	return x_test, t_test


# √‚√≥ : https://blog.naver.com/kurishin/221222111519
def show_mnist(n):
    with open('train-images.idx3-ubyte', 'rb') as f1:    
        data = f1.read(16) # skip header
        data = f1.read()
 
    with open('train-labels.idx1-ubyte', 'rb') as f2:
        num = f2.read(8) # skip header
        num = f2.read()
 
    data = ((i%28, 28-i//28, int(d)) for i, d in enumerate(data[(28*28)*n:28*28*(n+1)]))
    data = np.array(list(data)).T
 
    plt.title('MNIST - label(%d), pos(%d)'%(num[n], n))
    plt.scatter(data[0], data[1], data[2], marker='.')
    plt.show()
    
show_mnist(8)
#

def init_network():
	with open("sample_weight.pkl", 'rb') as f3:
		network = pickle.load(f3)               

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