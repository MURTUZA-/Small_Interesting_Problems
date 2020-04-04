# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:07:13 2017

@author: Pavan_Rashmi
"""

import numpy as np
import operator
import sys

def dist(C1,d1,C2,d2):
    #calculate distance
    distance = 0
    con =1
   
    distance = np.sum(np.square(np.subtract(C1,d1)))
    
    for i in range(len(C2)):
       
        if C2[i] != d2[i]:
            distance+=np.square(con)
    #print distance
    #print "calculate distance"
    np.sqrt(distance)
    return distance

  



args = sys.argv

data_file = args[1]
print("Loading RAW data...")


    


col1 = np.genfromtxt(data_file,dtype="float",delimiter=',',usecols = range(0,34))
col2= np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = range(34,40))
data_set = np.concatenate((col1,col2),axis = 1)


#print type(np.size(final_data))
final_data=data_set[:,0:40]
#print np.size(final_data[0])

# Two hyper parameters cluster Width, Percentage of Normal(used for labeling)
W=int(args[3])
N=int(args[4])
#Initialize set of clusters to be empty
dictS={}
#S=[]
#cluster_count = []
for i in range(len(final_data)):
    if i == 0:
        dictS[i]=1
        continue
    mindistance = dist(col1[0],col1[i],col2[0],col2[i])
    minindex= 0
    for k in dictS:
        
        distance = dist(col1[k],col1[i],col2[k],col2[i])
      
        if  distance < mindistance:
            mindistance = distance
            minindex = k
    if(mindistance <= W):
        dictS[k]+=1
    else:
        dictS[i]=1

cluster_size = len(dictS)
normal_ind= int(cluster_size*(float(N)/float(100)))
#Labelling
normal_indices=dict(sorted(dictS.iteritems(), key=operator.itemgetter(1), reverse=True)[:normal_ind])
print normal_indices.keys()


#reading test set
data_file = args[2]
print("Loading TEST data...")    


col3 = np.genfromtxt(data_file,dtype="float",delimiter=',',usecols = range(0,34))
col4= np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = range(34,40))
data_set = np.concatenate((col3,col4),axis = 1)

#print type(np.size(final_data))
final_data=data_set[:,0:40]
test_labels = np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = (41))
#print np.size(final_data[0])
normal_inst =0
intrus = 0
pred_intr_wrongly=0
pred_intrus =0

TP=0
TN=0
FP=0
FN=0

for i in range(len(final_data)):
   
    mindistance = dist(col1[0],col3[i],col2[0],col4[i])
    minindex= 0
    for k in dictS:        
        distance = dist(col1[k],col3[i],col2[k],col4[i])
      
        if  distance < mindistance:
            mindistance = distance
            minindex = k
    pred_class = 0
    if minindex in normal_indices:
        pred_class = 1
   
    if(test_labels[i] == 'normal.' and pred_class == 1):
        TN+=1
    if(test_labels[i] != 'normal.' and pred_class == 0):
        TP+=1
    if(pred_class == 1 and test_labels[i] != 'normal.'):
        FN+=1
    if(pred_class == 0 and test_labels[i] == 'normal.'):        
        FP+=1    


# Performance evaluation
#false positive - incorrectly classified as intrusion/ total number of normal instances
fp_rate  = float(FP) / float(FP+TN)
#detection rate - no of intrusions detected /total intrusion instances in the test data
detection_rate = float(TP)/float(FN+TP)
#Accuracy
accuaracy = float(TP+TN)/float(TP+TN+FP+FN)
#Precision
precision_A = float(TP)/float(TP+FP)
#Recall
recall_A = float(TP) / float(TP+FN)



print TP, "\t",FP,"\t",FN,"\t",TN,"\n"

#Precision
precision_N = float(TN)/float(TN+FN)
#Recall
recall_N = float(TN) / float(TN+FP)
#F1-Score
f1_score_A = float(2* recall_A*precision_A)/float(recall_A+precision_A)
f1_score_N = float(2* recall_N*precision_N)/float(recall_N+precision_N)
f1_score = float(f1_score_A+f1_score_N)/2

#print pred_intr_wrongly
print 'false rate: ', fp_rate,'\t'
print 'detection rate: ', detection_rate,'\t'
print 'Accuracy: ', accuaracy,'\t'
print 'Precision: ', precision_A,"\t",precision_N,'\t'
print 'Recall: ', recall_A,"\t",recall_N,'\t'
print 'F1-score: ', f1_score,'\t'

        
    
