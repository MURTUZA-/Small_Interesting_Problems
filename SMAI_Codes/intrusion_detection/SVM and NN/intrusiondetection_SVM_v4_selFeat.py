#Balanced class distribution for each fold
import os
import sys
import math
import time
import random
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate
from sklearn.metrics import precision_recall_fscore_support

inputDirPath = sys.argv[1]
testFold = sys.argv[2]
selectedFeatFile = sys.argv[3]

sfFile = open(selectedFeatFile)
sf = []
for line in sfFile:
	lineParts = line.strip().split(',')
	for part in lineParts:
		sf.append(int(part.strip()))
sfFile.close()

print ('Preparing Data')
strX_train = []
strY_train = []
strX_test = []
strY_test = []
testFoldFile = 'fold' + testFold + '.txt'
fileList = os.listdir(inputDirPath)
for currFile in fileList:
	if(currFile == testFoldFile):
		f = open(os.path.join(inputDirPath, currFile))
		for line in f:
			lineParts = line.split()
			currFeat = [lineParts[j] for j in sf]
			strX_test.append(currFeat)
			strY_test.append(lineParts[41])
		f.close()
	else:
		f = open(os.path.join(inputDirPath, currFile))
		for line in f:
			lineParts = line.split()
			currFeat = [lineParts[j] for j in sf]
			strX_train.append(currFeat)
			strY_train.append(lineParts[41])
		f.close()

X_train = np.array(strX_train)
X_train = X_train.astype('float')
scaler = preprocessing.StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
print X_train.shape

Y_train = np.array(strY_train)
encoder = LabelEncoder()
encoder.fit(Y_train)
Y_train = encoder.transform(Y_train)
print Y_train.shape

X_test = np.array(strX_test)
X_test = X_test.astype('float')
X_test = scaler.transform(X_test)
print X_test.shape

Y_test = np.array(strY_test)
Y_test = encoder.transform(Y_test)
print Y_test.shape

print ('Training model')
#Initializing SVM
clf = svm.SVC(kernel = 'rbf', decision_function_shape = 'ovo')

#Training model
s = time.time()
clf.fit(X_train, Y_train)
e = time.time()
print 'Training time: ' + str(e - s)
print str(len(clf.support_vectors_))

#Testing
print ('Testing')
Y_pred = clf.predict(X_test)

print str(encoder.classes_)
precision, recall, f1, support = precision_recall_fscore_support(Y_test, Y_pred)
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
precision, recall, f1, support = precision_recall_fscore_support(Y_test, Y_pred, average='macro')
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
