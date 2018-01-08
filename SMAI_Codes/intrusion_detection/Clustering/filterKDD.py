# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:07:13 2017

@author: Pavan_Rashmi
"""

import numpy as np
from sklearn.preprocessing import StandardScaler
import random

data_file = "kddcup.data_10_percent_corrected"
print("Loading RAW data...")
raw_data = np.genfromtxt(data_file,dtype="|S10",delimiter=',')


print "before normal",np.size(raw_data,axis=1)
# separate dataset based on the classes 
normal_data = np.array([[x for x in a]for a in raw_data if a[-1] == 'normal.'])
print np.size(normal_data,axis=0)
attack_data = np.array([[x for x in a]for a in raw_data if a[-1] != 'normal.'])
print np.size(attack_data,axis=0)




# sampling amount
normal_size_data = np.size(normal_data,axis=0)
print normal_size_data
attack_size_data =int(normal_size_data*(float(100)/float(99)) - normal_size_data)
print attack_size_data


# Sampling 99 % normal data
new_sampled_normal_data = random.sample(normal_data,int(normal_size_data))
print np.size(new_sampled_normal_data,axis=0)




# Sampling 1% attack data equally distributed between the attack

new_sampled_attack_data = random.sample(attack_data,int(attack_size_data))
print np.size(new_sampled_attack_data,axis=0)


raw_set = np.concatenate((new_sampled_normal_data,new_sampled_attack_data),axis=0)

#print np.size(raw_set)
labels = raw_set[:,-1]
#print labels
data_set =raw_set[:,0:40]
#print data_set[0]

# Scale the non-discrete data
scale_data = data_set[:,[0,4,5,7,8,9,10,12,13,14,15,16,17,18,19]]
scale_data = np.concatenate((scale_data, data_set[:,21:41]), axis=1)

scaler = StandardScaler(copy=True,with_mean=True,with_std=True)    
scaler.fit(scale_data)
scale_data = scaler.transform(scale_data)

#Combine discrete and continous 
#6,11,20,21
final_data = np.concatenate((scale_data, data_set[:,[6,11,20,21,1,2,3]]), axis=1)

print np.size(labels)
print np.size(final_data,axis =0)

final_data = np.insert(final_data,41,labels,axis=1)
np.random.shuffle(final_data)
f=open("ffrfilterKDD.csv","w+")
for i in final_data:
    for x in i:        
        f.write(x)
        f.write(",")
    f.write("\n")
f.close()