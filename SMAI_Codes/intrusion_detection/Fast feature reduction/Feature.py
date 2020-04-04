import numpy as np
import sklearn as sk
import csv
import heapq

def oneHotEncode(feature_col):
	print feature_col.shape
	temp_max = np.max(feature_col)
	temp=[]
	for i in range(0,int(temp_max)):
		feature_col = feature_col- temp_max
		temp.append(np.floor((feature_col/temp_max) + 1))
		feature_col = np.abs(feature_col) + 1
	return np.transpose(np.array(temp))


def DataRead(nFeatures,file_name,categorical_feature):
	datareader = csv.reader(open(file_name, "rb"), delimiter=" ")
	x=[]
	Y=[]

	for row in datareader:
		x.append(row[0:nFeatures])
		Y.append(row[nFeatures])

	X1 = {}
	x=np.array(x).astype('float')
	for col in range(0,nFeatures):
		if col in categorical_feature:
			X1[col] = oneHotEncode(x[:,col])
			print X1[col].shape
		else:
			X1[col]= np.reshape(x[:,col],(x[:,col].shape[0],1))
			print X1[col].shape
	print "*******************"
	print "*******************"

	X = X1[0]
	print X1[0].shape
	for i in range(1,nFeatures):
		print X1[i].shape
		X = np.hstack((X,X1[i]))

	print "Shape of oneHotEncoded Data    ",X.shape
	return X,Y,X.shape[1]


def Feature_red(nFeatures,nReduced_Features,file_name,categorical_feature):


	labels=['normal','probe','DoS','r2l','u2r']
	nClasses=5
	X,Y,nFeatures=DataRead(nFeatures,file_name,categorical_feature)

	#***************************************************************************
	#************************Partitioning into classes**************************

	classes={}
	for i in labels:
		classes[i]=[]

	for i in range(0,X.shape[0]):
		classes[Y[i]].append(X[i,:])
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
