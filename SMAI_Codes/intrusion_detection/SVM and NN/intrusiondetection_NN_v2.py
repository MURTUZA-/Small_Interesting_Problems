import sys
import math
import random
import numpy as np

from keras.models import Model
from keras.layers import Input
from keras.utils import np_utils
from keras.layers.core import Dense

#from sklearn.utils import class_weight
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support

inputFilePath = sys.argv[1]
epos = int(sys.argv[2])
batchSize = int(sys.argv[3])

inputFile = open(inputFilePath)
percent = 0.8

classWeights = {0:0.1, 1:0.1, 2:0.2, 3:0.25, 4:0.35}

allLines = []
for line in inputFile:
	allLines.append(line.strip())
random.shuffle(allLines)

strX = []
strY = []
for line in allLines:
	lineParts = line.split()
	strX.append(lineParts[0:41])
	strY.append(lineParts[41])

X = np.array(strX)
X = X.astype('float')
print X.shape
Y = np.array(strY)
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
print str(encoder.classes_)
Y = np_utils.to_categorical(encoded_Y)
print Y.shape

split = int(math.ceil(percent * len(X)))
X_train = X[0: split]
Y_train = Y[0: split]

X_test = X[split:]
Y_test = Y[split:]

#Input layer with 41 nodes
inp = Input(shape=(41,))

#First Hidden layer with 40 nodes
hidden1 = Dense(40, activation='sigmoid')(inp)

#Second Hidden layer with 40 nodes
hidden2 = Dense(40, activation='sigmoid')(hidden1)

#Final output layer
out = Dense(5, activation='softmax')(hidden2)

model = Model(inp, out)
model.compile(optimizer='adam', loss='categorical_crossentropy')
model.summary()

#Training model
print ('Training')
model.fit(X_train, Y_train, nb_epoch = epos, batch_size = batchSize, class_weight = classWeights)

#Testing
print ('Testing')
Y_pred = model.predict(X_test)

Y_test_final = np.empty((len(Y_test),))
for i in range(len(Y_test)):
	Y_test_final[i] = np.argmax(Y_test[i])

Y_pred_final = np.empty((len(Y_pred),))
for i in range(len(Y_pred)):
	Y_pred_final[i] = np.argmax(Y_pred[i])

c = confusion_matrix(Y_test_final, Y_pred_final)
print c
precision, recall, f1, support = precision_recall_fscore_support(Y_test_final, Y_pred_final)
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
#precision, recall, f1, support = precision_recall_fscore_support(Y_test, Y_pred_final, average='binary')
#print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
