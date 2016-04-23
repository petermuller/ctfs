#!/usr/bin/env python

import SocketServer, threading, os, socket, StringIO
from hashlib import md5
import numpy as np

from keras.models import Sequential
from keras.layers import ZeroPadding2D
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D

m = Sequential()

width = 320
height = 240

m.add(ZeroPadding2D((1,1),input_shape=(3,height,width)))
m.add(Convolution2D(64, 6, 6, activation='relu'))
m.add(ZeroPadding2D((1,1)))
m.add(Convolution2D(64, 6, 6, activation='relu'))
m.add(MaxPooling2D((4,4), strides=(4,4)))

m.add(Convolution2D(64, 4, 4, activation='relu'))
m.add(ZeroPadding2D((1,1)))
m.add(Convolution2D(64, 4, 4, activation='relu'))
m.add(MaxPooling2D((3,3), strides=(3,3)))

m.add(Convolution2D(128, 3, 3, activation='relu'))
m.add(ZeroPadding2D((1,1)))
m.add(Convolution2D(128, 3, 3, activation='relu'))
m.add(MaxPooling2D((3,3), strides=(3,3)))

m.add(Convolution2D(192, 3, 3, activation='relu'))
m.add(ZeroPadding2D((1,1)))
m.add(Convolution2D(192, 3, 3, activation='relu'))
m.add(MaxPooling2D((3,3), strides=(3,3)))

m.add(Flatten())
m.add(Dropout(0.3))
m.add(Dense(256, activation='relu'))
m.add(Dropout(0.4))
m.add(Dense(256, activation='relu'))
m.add(Dropout(0.4))
m.add(Dense(2, activation='softmax'))

m.compile(optimizer='sgd', loss='binary_crossentropy')

m.load_weights("model")

bru = 100
brut = bru - 1
bests = {}
for b in xrange(bru):
	for g in xrange(bru):
		for r in xrange(bru):
			c1 = np.ones((240, 320), np.float32) * r
			c2 = np.ones((240, 320), np.float32) * g
			c3 = np.ones((240, 320), np.float32) * b
			img = np.array([c1, c2, c3])
			bad,good = list(m.predict(np.array([img]))[0])
			print((r,g,b), good)
			if good > 0.99:
				bests[(r,g,b)] = good
print bests
f = open("flags.txt",'w')
for key in bests.keys():
	f.write(key, bests[key])
f.close()



