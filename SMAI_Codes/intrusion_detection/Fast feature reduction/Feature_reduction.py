import numpy as np
import sklearn as sk
import csv
import heapq
from sklearn.naive_bayes import MultinomialNB

def Feature_red(nF,nR_F,file_name,categorical_feature):


	nReduced_Features=nR_F
	nFeatures=nF
#	categorical_feature = [1,2,3,6,11,20,21]
#	categorical_feature = []
	datareader = csv.reader(open(file_name, "rb"), delimiter=" ")
	labels=['normal','probe','DoS','r2l','u2r']
	nClasses=5


	X=[]
	Y=[]

	for row in datareader:
		X.append(row[0:nFeatures])
		Y.append(row[nFeatures])
	#***************************************************************************
	#************************Partitioning into classes**************************

	classes={}
	for i in labels:
		classes[i]=[]

	for i in range(0,len(X)):
		classes[Y[i]].append(X[i])
	#***************************************************************************
	#************************Mean and variance**********************************

	mn=np.zeros((nFeatures,nClasses))
	#print np.sum(np.asarray(classes[labels[0]]).astype('float')[0:5,1])

	for i in range(0,nClasses):
		for j in range(0,nFeatures):
			if j in categorical_feature:
				mn[j,i]= 0
			else:
				temp=np.asarray(classes[labels[i]]).astype('float')[:,j]
				minimum=np.min(temp)
				maximum=np.max(temp)
				if maximum-minimum<0.00001:
					mn[j,i]=0
				else:
					temp=temp-minimum
					temp=temp/(maximum-minimum)
					mn[j,i]= np.sum(temp)/len(classes[labels[i]])

	mn_data=np.zeros((nFeatures,)).astype('float')

	for i in range(0,nClasses):
		mn_data=mn_data + mn[:,i]

	mn_data/=nClasses

	variance=np.zeros((nFeatures,)).astype('float')

	for i in range(0,nClasses):
		variance+=(mn[:,i]-mn_data)**2

	variance1={}
	for i in range(0,nFeatures):
		variance1[i]=variance[i]
	print variance
	#**************************************************************************
	#************************Feature Reduction/selection***********************

	ind=heapq.nlargest(nReduced_Features,variance1,key=variance1.get)
	return ind,X,Y
