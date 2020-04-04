import numpy as np
import sklearn as sk
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
import sys
import Feature as FR

categorical_feature = [1,2,3,6,11,20,21]
#ind = [32, 22, 31, 23, 34, 26, 27, 35, 40, 13, 39, 33, 28, 29, 9, 30, 25, 37, 38, 24]
nFeatures=41
nReduced_Features=10
percent_val=.2

files=sys.argv
files.pop(0)


ind,X,Y = FR.Feature_red(nFeatures,nReduced_Features,files[0],categorical_feature)

print ind
#****************************************************************************
#****************************Read Data***************************************

X_reduced=[]

Y1 = np.array(Y)
encoder = LabelEncoder()
encoder.fit(Y1)
Y = encoder.transform(Y1)
print str(encoder.classes_)



X=np.array(X).astype('float')
#for i in set(ind) | set(categorical_feature):
for i in set(ind):
	X_reduced.append(X[:,i])

X_reduced=np.array(X_reduced)
X_reduced=np.transpose(X_reduced)

#**************************************************************************
#*****************************Naive Bayes *********************************

N=X_reduced.shape[0]
val_len=int(N*percent_val)
X_test=X_reduced[0:val_len,:]
Y_test=Y[0:val_len]

X_reduced_train=X_reduced[val_len:,:]
Y_train=Y[val_len:]

gnb = MultinomialNB()
gnb.fit(X_reduced_train, Y_train)
y_pred = gnb.predict(X_test)
Accuracy = accuracy_score(Y_test, y_pred)
precision, recall, f1, support = precision_recall_fscore_support(Y_test, y_pred)
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
print"Accuracy =  ", Accuracy

#*************************************************************************
#**************************KNN Classifier*********************************
'''
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_reduced_train, Y_train)
y_pred = neigh.predict(X_test)

precision, recall, f1, support = precision_recall_fscore_support(Y_test, y_pred)
print('Precision: ' + str(precision) + '\tRecall: ' + str(recall) + '\tF1: ' + str(f1))
 '''