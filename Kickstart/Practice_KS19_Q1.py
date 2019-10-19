def guess_the_number(A, B, N):
	for itr in range(N):
		number = int((B+A)/2)
		print(number)
		response = input()
		if(response =='CORRECT'):
			break
		elif(response == 'TOO_SMALL'):
			# number = int((B-number)/2)
			A = number+1
		elif(response == 'TOO_BIG'):
			B = number-1
		elif(response == 'WRONG_ANSWER'):
			quit()


T = input()
T= int(T)
# print(T)
for test_itr in range(T):
	AB = input()
	A = int(AB.split()[0])
	# print(A)
	B = int(AB.split()[1])
	# print(B)
	N = int(input())
	guess_the_number(A+1,B,N)