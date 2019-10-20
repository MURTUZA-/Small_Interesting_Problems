import numpy as np
from sys import stdin, stdout
def fair_team(A,N,p):
	running_sum = np.sum(A[:p])
	# min_num_hours = np.sum(A[p-1]-A[:p])
	min_num_hours = p*A[p-1]-running_sum
	for itr in range(p,N):
		# num_hours = np.sum(A[itr] - A[itr-p+1:itr+1])
		running_sum = running_sum + A[itr] - A[itr-p]
		num_hours = p*A[itr]-running_sum
		if(num_hours<= min_num_hours):
			min_num_hours = num_hours
	return min_num_hours

T = int(stdin.readline())
for itr in range(T):
	N,p = [int(x) for x in stdin.readline().split()]
	A = [int(x)for x in stdin.readline().split()]

	Arr = np.sort(np.array(A))
	output = 'Case #'+str(itr+1)+': '+str(fair_team(Arr,N,p))+'\n'
	stdout.write(output)
