import sys
import math
import random
import numpy as np
from sklearn import svm
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_validate
from sklearn.metrics import precision_recall_fscore_support

inputFilePath = sys.argv[1]
lineCount = int(sys.argv[2])
inputFile = open(inputFilePath)
scores = ['precision_macro', 'recall_macro', 'f1_macro']
#percent = 0.8

allLines = []
for line in inputFile:
	allLines.append(line.strip())
random.seed(1)
random.shuffle(allLines)

if(lineCount >= len(allLines)):
	consideredLines = allLines
else:
	consideredLines = allLines[0:lineCount]

strX = []
strY = []
for line in consideredLines:
	lineParts = line.split()
	strX.append(lineParts[0:41])
	strY.append(lineParts[41])

X = np.array(strX)
X = X.astype('float')
print X.shape

scaler = preprocessing.StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

Y = np.array(strY)
encoder = LabelEncoder()
encoder.fit(Y)
Y = encoder.transform(Y)
print Y.shape

"""split = int(math.ceil(percent * len(X)))
X_train = X[0: split]
Y_train = Y[0: split]

X_test = X[split:]
Y_test = Y[split:]"""

#Initializing SVM
clf = svm.SVC(C = 1.0, kernel = 'rbf', decision_function_shape = 'ovr')

#Cross Validation and scoring
scores = cross_validate(clf, X, Y, cv = 5, scoring = scores, verbose = 1)
print scores['test_precision_macro']
print scores['test_recall_macro']
print scores['test_f1_macro']

"""#Training model
print ('Training')
clf.fit(X_train, Y_train)

#Testing
print ('Testing')
Y_pred = clf.predict(X_test)

c = confusion_matrix(Y_test, Y_pred)
print c
precision, recall, f1, support = precision_recall_fscore_support(Y_test, Y_pred)
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
precision, recall, f1, support = precision_recall_fscore_support(Y_test, Y_pred, average='macro')
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))"""
