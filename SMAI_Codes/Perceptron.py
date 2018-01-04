arg_A = '';
arg_B = '';

import csv
import numpy as np
import sys
files=sys.argv
files.pop(0)
validating=np.genfromtxt(files[0][1:],delimiter=",", missing_values=['?'],filling_values=np.NAN)
validating=validating[~np.isnan(validating).any(axis=1)]
A = np.matrix(validating).astype("float")

validating=np.genfromtxt(files[1],delimiter=",", missing_values=['?'],filling_values=np.NAN)
validating=validating[~np.isnan(validating).any(axis=1)]
test=np.matrix(validating).astype("float")
target=np.matrix([1 for i in range(test.shape[0])])
test=np.hstack((target.T,test))


n = A.shape[1]-1
N = A.shape[0]

W = np.zeros((n+1,1),dtype=float)
margin = 0

P = 100
perc_val= 0

val_len= int(N*(perc_val/100.0))
tr_len= N-val_len

# **************Split data into training and validataion*************************


import random
rnd_val=random.sample(range(0,N), val_len)

iterator_val=0
iterator_tr=0


y_val=np.matrix([0 for i in range(val_len)])
y_tr=np.matrix([0 for i in range(tr_len)])

val=np.matrix([ [ 0 for i in range(n+1) ] for j in range(val_len) ])
tr=np.matrix([ [ 0 for i in range(n+1) ] for j in range(tr_len) ])

for i in range(0,N):
  if i in rnd_val:
    val[iterator_val,:]=A[i,0:n+1]
    val[iterator_val,0]=1
    if A[i,0]==1:
      y_val[0,iterator_val]=A[i,0]
    else:
      y_val[0,iterator_val]=-1

    iterator_val+=1;
  else:
    tr[iterator_tr,:]=A[i,0:n+1]
    tr[iterator_tr,0]=1
    if A[i,0]==1:
      y_tr[0,iterator_tr]=A[i,0]
    else:
      y_tr[0,iterator_tr]=-1

    iterator_tr+=1;

#*****************************Augmenting test data And Target spliting***********

for i in range(test.shape[0]):
  if test[i,0]==1:
    target[0,i]=test[i,0]
  else:
    target[0,i]=-1
  test[i,0]=1


# ****************************@@@@@@@@@@@@@@@@@@@@@******************************

def training(b,w):
  miss=np.zeros((1,P),dtype=int)

  for i in range(0,P):
    rnd_tr=random.sample(range(0,tr_len),tr_len)
    for j in rnd_tr:
      if float(y_tr[0,j]*tr[j,:]*w) <= b:
        miss[0,i]+=1
        w=w+y_tr[0,j]*tr[j,:].transpose()
    if int(miss[0,i])==0:
      break;
  return w,miss

#*****************************@@@@@@@@@@@@@@@@@@@@*******************************

def validating(b,w):
  TP=0
  TN=0
  FP=0
  FN=0

  for i in range(0,val_len):
    if float(y_val[0,i]*val[i,:]*w) >b:
      if y_val[0,i]>0:
        TP+=1
      else:
        TN+=1
    else:
      if y_val[0,i]>0:
        FN+=1
      else:
        FP+=1
  return TP,TN,FP,FN


#*****************************Batch Training*************************************


def batch_training(b,w,eta,p):
  miss=np.zeros((1,p),dtype=int)

  for i in range(0,p):
    update=0
    for j in range(0,tr_len):
      if float(y_tr[0,j]*tr[j,:]*w) <= b:
        miss[0,i]+=1
        update=update + eta*y_tr[0,j]*tr[j,:].transpose()
    w=w+update
    if int(miss[0,i])==0:
      break;
  return w,miss


#*********************************Testing***************************************

def testing(b,w):
  for i in range(0,test.shape[0]):
    if float(test[i,:]*w) >b:
      print 1
    else:
      print 0


#*****************************@@@@@@@@@@@@@@@@@*********************************
margin=0
W,miss = training(margin,W)
testing(margin,W)

margin=0.2
W,miss = training(margin,W)
testing(margin,W)

margin=0.2
W,miss = batch_training(margin,W,.02,100)
testing(margin,W)

margin=0
W,miss = batch_training(margin,W,.02,100)
testing(margin,W)

#TP,TN,FP,FN=validating(margin,W)
'''

precision=TP/float(TP+FP)
recall=TP/float(TP + FN)
accuracy=float(TP+TN)/val_len
print 'accuracy=', accuracy
print 'precision=', precision
print 'recall=', recall
'''