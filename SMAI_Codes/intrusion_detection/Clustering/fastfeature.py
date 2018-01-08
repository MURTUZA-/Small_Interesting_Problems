# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:07:13 2017

@author: Pavan_Rashmi
"""

import numpy as np
import operator
import sys
import csv
import time

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

def mapping(col_list):
    print col_list
    col =[]
    cat_col =[]
    for i in col_list:
       
        if int(i) == 0:
            
            col.append(0)
        if int(i)==4:
            col.append(4)
        if int(i)==5:
            col.append(5)
        if int(i) in (7,8,9,10):
            col.append(int(i)-4)
        if int(i) in range(12,20):
            col.append(int(i)-5)
        if int(i) in range(21,41):
            col.append(int(i)-6)
        if int(i) in (1,2,3):
            cat_col.append(int(i)+37)
        if int(i) == 6:
            cat_col.append(35)
        if int(i) == 11:
            cat_col.append(36)
        if int(i) == 20:
            cat_col.append(37)
    
    return col,cat_col
        
    
    

#edit for giving time aswell



args = sys.argv
f=open("fastfeatureAnalysis.csv","w+")
p=0
with open("fastfeature.csv") as csvfile:
    colreader = csv.reader(csvfile, delimiter=',')    
    for c in colreader:
        if not(c):
            break
        p+=1
        start_time = time.time()
        col,cat_col=mapping(c)
        data_file = "P2.csv"
        print("Loading Train data...")
        
        
        
        col1 = np.genfromtxt(data_file,dtype="float",delimiter=',',usecols = col)
        col2= np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = cat_col)
        data_set = np.concatenate((col1,col2),axis = 1)
        
        
        #print type(np.size(final_data))
        final_data=data_set[:,0:(np.size(data_set,axis=1))]
        #print np.size(final_data[0])
        
         #reading test set
        data_file = "P10.csv"
        print("Loading Validation data...")    
        
        
        
        col3 = np.genfromtxt(data_file,dtype="float",delimiter=',',usecols = col)
        col4= np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = cat_col)
        data_set = np.concatenate((col3,col4),axis = 1)
        
        #print type(np.size(final_data))
        final_val_data=data_set[:,0:(np.size(data_set,axis=1))]
        test_labels = np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = (41))
        #print np.size(final_data[0])
        
            
        high_f1_score = 0
        opt_W = 0
        opt_N = 0
        
        
        # Two hyper parameters cluster Width, Percentage of Normal(used for labeling)
        for W in (20,30,40):
            print "W: ",W,"\n"
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
            for N in (10,15,20,25,30,35,40):  
                print "N: ",N,"\n"
                 
                cluster_size = len(dictS)
                normal_ind= int(cluster_size*(float(N)/float(100)))
                #Labelling
                normal_indices=dict(sorted(dictS.iteritems(), key=operator.itemgetter(1), reverse=True)[:normal_ind])
                print normal_indices.keys()
                
                normal_inst =0
                intrus = 0
                pred_intr_wrongly=0
                pred_intrus =0
                
                TP=0
                TN=0
                FP=0
                FN=0
                       
                
                for i in range(len(final_val_data)):
                   
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
                
                print TP, "\t",FP,"\t",FN,"\t",TN,"\n"
                # Performance evaluation
                if (FP+TN)== 0 or (FN+TP)==0 or (TP+FN) == 0 or (TP+FP) == 0 or (TN+FN)==0:
                    continue
                
                
                #false positive - incorrectly classified as intrusion/ total number of normal instances
                fp_rate  = float(FP) / float(FP+TN)
                #detection rate - no of intrusions detected /total intrusion instances in the test data
                detection_rate = float(TP)/float(FN+TP)
                #Recall
                recall_A = float(TP) / float(TP+FN)
                #Accuracy
                accuaracy = float(TP+TN)/float(TP+TN+FP+FN)
                #Precision
                precision_A = float(TP)/float(TP+FP)
                
                
                
                
                
                
                #Precision
                precision_N = float(TN)/float(TN+FN)
                #Recall
                recall_N = float(TN) / float(TN+FP)
                #F1-Score
                f1_score_A = float(2* recall_A*precision_A)/float(recall_A+precision_A)
                f1_score_N = float(2* recall_N*precision_N)/float(recall_N+precision_N)
                f1_score = float(f1_score_A+f1_score_N)/2
                
                if high_f1_score < f1_score:
                    high_f1_score = f1_score
                    opt_W = W
                    opt_N = N
        
        print opt_W ,"\t", opt_N
        
        #training on P2,P3
        print "Training"
        col1 = np.concatenate((col1,col3),axis=0)
        col2 = np.concatenate((col2,col4),axis=0)
        data_set = np.concatenate((col1,col2),axis = 1)
        
        #print type(np.size(final_data))
        final_data=data_set[:,0:(np.size(data_set,axis=1))]
        #print np.size(final_data[0])
        
        # Two hyper parameters cluster Width, Percentage of Normal(used for labeling)
        W=opt_W
        N=opt_N
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
        
        
        
        
        #Testing on P10.csv
        data_file ="P3.csv"
        print("Loading TEST data...")    
        
        
        col3 = np.genfromtxt(data_file,dtype="float",delimiter=',',usecols = col)
        col4= np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = cat_col)
        data_set = np.concatenate((col3,col4),axis = 1)
        
        #print type(np.size(final_data))
        final_data=data_set[:,0:(np.size(data_set,axis=1))]
        test_labels =np.genfromtxt(data_file,dtype="str",delimiter=',',usecols = (41))
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
        
        
        
        
        
        #Precision
        precision_N = float(TN)/float(TN+FN)
        #Recall
        recall_N = float(TN) / float(TN+FP)
        #F1-Score
        f1_score_A = float(2* recall_A*precision_A)/float(recall_A+precision_A)
        f1_score_N = float(2* recall_N*precision_N)/float(recall_N+precision_N)
        f1_score = float(f1_score_A+f1_score_N)/2
        end_time = (time.time() - start_time)
        f.write('Column list '+str(p)+',')
        f.write('W='+str(W)+',')
        f.write('N='+str(N)+',')
        
          
        f.write('false rate: '+str(fp_rate)+',')
        f.write('detection rate: '+str(detection_rate)+',')
        f.write('Accuracy: '+str(accuaracy)+',')
        f.write('Precision: '+str(precision_A)+','+str(precision_N)+',')
        f.write('Recall: '+ str(recall_A)+','+str(recall_N)+',')
        f.write('F1-score: '+ str(f1_score))
        f.write('Time taken:'+str(end_time))
        f.write("\n")
csvfile.close()
f.close()
        
                
            
        
                        
                    
