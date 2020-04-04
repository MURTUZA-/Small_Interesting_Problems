def maxSum(indx):
	global max_trinket
	global from_indx
	if indx==0:
		count_dict = {}
		count_dict[A[indx]]=1
		return count_dict,1
	else:
		count_dict,temp = maxSum(indx-1)
		try:
			if count_dict[A[indx]]+1>S:

				if A[indx]==A[from_indx]:
					from_indx +=1
					max_sum = temp
				else:
					if count_dict[A[indx]]==S:
						max_sum = temp-S
					else:
						max_sum = temp
					count_dict[A[indx]]+=1

				if max_sum<=1:
					max_sum = 1
					from_indx = indx
					count_dict = {}
					count_dict[A[indx]]=1
			else:
				count_dict[A[indx]] +=1
				max_sum = temp + 1
			max_trinket = max(max_trinket, max_sum)
		except:
			count_dict[A[indx]] = 1
			max_sum = temp + 1
			max_trinket = max(max_trinket, max_sum)
		return count_dict, max_sum

T = int(input())
for itr in range(T):
	N,S = [int(ele) for ele in input().split()]
	A = [int(ele) for ele in input().split()]
	max_trinket = 0
	if S<=1:
		print('Case #'+str(itr+1)+': '+str(0))
	else:
		from_indx = 0
		indx = N-1
		count_dict, temp = maxSum(indx)
		print('Case #'+str(itr+1)+': '+str(max_trinket))
