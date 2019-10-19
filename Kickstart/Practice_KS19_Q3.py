import numpy as np
modulo = 1000000007
def cal_power (x,n):
	temp = 1
	for i in range(n):
		temp = (temp*x) % modulo
	return temp

def kickstart_alarm(A,K):
	sum_power = 0
	N = len(A)
	for itr_A in range(1,N+1):
		for x in range(1,N+1):
			if(itr_A-x >= 0 and x>1):
				sum_power =  (sum_power + (A[itr_A-1] * (N-itr_A+1) * (((x/(x-1))*(cal_power(x,K)-1)))) )% modulo
				# sum_power =  (sum_power + (A[itr_A-1]  * ((cal_power(x-1,modulo-2))*(cal_power(x,K+1)-1))) )% modulo

			else:
				sum_power =  (sum_power + (A[itr_A-1] * (N-itr_A+1) * K ))% modulo
				# sum_power =  (sum_power + (A[itr_A-1] * K ))% modulo

	return sum_power

T = int(input())
for itr in range(T):
	input_list = input().split()
	N,K,x,y,C,D,E1,E2,F = [int(input_list[q]) for q in range(len(input_list))]

	A=[]
	A.append(x+y)
	for i in range(1,N):
		temp_x = (C*x + D*y + E1)% F
		temp_y = (D*x + C*y + E2)% F
		value = (temp_x + temp_y)% F
		A.append(value)
		x = temp_x
		y = temp_y
	output = 'Case #'+str(itr+1)+': ' + str(kickstart_alarm(A,K))
	print(output)