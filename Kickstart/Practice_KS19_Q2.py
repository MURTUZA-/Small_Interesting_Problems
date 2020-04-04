import numpy as np

def max_subarray(arr):
	len_subarray = int(np.ceil(arr.shape[0]/2))
	sum_sub_arr = np.sum(arr[:len_subarray])
	max_sum_arr = sum_sub_arr
	max_idx = 0
	for itr in range(0,int(arr.shape[0]/2)):
		sum_sub_arr = arr[itr+len_subarray] + sum_sub_arr - arr[itr]
		if sum_sub_arr>max_sum_arr:
			max_sum_arr = sum_sub_arr
			max_idx = itr
	return max_sum_arr
T = int(input())
for i in range(T):
	N = int(input())
	arr = np.zeros(N)
	b_score = input()
	arr = np.array([int(b_score[j]) for j in range(len(b_score))])
	print('Case #'+str(i+1)+': '+ str(max_subarray(arr)))