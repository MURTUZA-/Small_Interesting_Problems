import numpy as np
modulo = 1000000007
def cal_power (x,n):
	if (n==1):
		return x
	temp = cal_power(x,np.floor(n/2))
	result = (temp*temp)%modulo
	if(n%2):
		result = (result*x)% modulo
	return result

def cal_sum_arr (N,K):
	sum_arr = np.zeros(N).astype('int')
	sum_arr[0] = K
	for x in range(2,N+1):
		sum_arr[x-1] = (sum_arr[x-2] + (((x * cal_power(x-1, modulo-2))% modulo) * (cal_power(x,K)-1))% modulo)% modulo
	return sum_arr


def kickstart_alarm(A_i,N, sum_arr_i, i):

	contribution_A_i = ( ((A_i * (N-i+1))%modulo) * sum_arr_i)% modulo
	return contribution_A_i


T = int(input())
for itr in range(T):
	input_list = input().split()
	N,K,x,y,C,D,E1,E2,F = [int(input_list[q]) for q in range(len(input_list))]

	sum_arr = cal_sum_arr(N,K)
	A_i = (x+y)%F
	sum_power = kickstart_alarm(A_i, N, sum_arr[0], 1)
	for i in range(2,N+1):
		temp_x = (C*x + D*y + E1)% F
		temp_y = (D*x + C*y + E2)% F
		A_i = (temp_x + temp_y)% F
		contribution_A_i = ( ((A_i * (N-i+1))%modulo) * sum_arr[i-1])% modulo
		sum_power = (sum_power + contribution_A_i)%modulo
		# sum_power = (sum_power + kickstart_alarm(A_i, N, sum_arr[i-1], i))%modulo
		x = temp_x
		y = temp_y
	output = 'Case #'+str(itr+1)+': ' + str(sum_power)
	print(output)