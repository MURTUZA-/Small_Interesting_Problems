import numpy as np
def fair_team(A,p):
	n_players = A.shape[0]
	min_num_hours = np.sum(A[p-1]-A[:p])
	for itr in range(p,n_players):
		num_hours = np.sum(A[itr] - A[itr-p+1:itr+1])
		if(num_hours<= min_num_hours):
			min_num_hours = num_hours
	return min_num_hours

T = int(input())
for itr in range(T):
	N,p = map(int, input().split())
	A = list(map(int, input().split()))

	Arr = np.sort(np.array(A))
	output = 'Case #'+str(itr+1)+': '+str(fair_team(Arr,p))
	print(output)
