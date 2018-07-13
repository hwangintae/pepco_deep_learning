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



# origin : https://blog.naver.com/kurishin/221222111519
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