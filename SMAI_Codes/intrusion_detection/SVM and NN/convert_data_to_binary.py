import sys

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

inputFile = open(inputFilePath)
outputFile = open(outputFilePath, 'w')

#Categorical Value Maps
protocolMap = {}
serviceMap = {}
flagMap = {}
landMap = {}
loggedInMap = {}
hostLoginMap = {}
guestLoginMap = {}
classMap = {}

for line in inputFile:
	lineParts = line.strip().split(',')
	newLine = ''
	
	#duration: numeric
	newLine = newLine + ' ' + lineParts[0]
	
	#protocol: categorical
	if (lineParts[1] not in protocolMap):
		tempLen = len(protocolMap)
		protocolMap[lineParts[1]] = tempLen + 1
	newLine = newLine + ' ' + str(protocolMap[lineParts[1]])
	
	#service: categorical
	if (lineParts[2] not in serviceMap):
		tempLen = len(serviceMap)
		serviceMap[lineParts[2]] = tempLen + 1
	newLine = newLine + ' ' + str(serviceMap[lineParts[2]])

	#flag: categorical
	if (lineParts[3] not in flagMap):
		tempLen = len(flagMap)
		flagMap[lineParts[3]] = tempLen + 1
	newLine = newLine + ' ' + str(flagMap[lineParts[3]])
	
	#src_bytes: numeric
	newLine = newLine + ' ' + lineParts[4]

	#dst_bytes: numeric
	newLine = newLine + ' ' + lineParts[5]
	
	#land: categorical
	if (lineParts[6] not in landMap):
		tempLen = len(landMap)
		landMap[lineParts[6]] = tempLen + 1
	newLine = newLine + ' ' + str(landMap[lineParts[6]])

	#wrong_fragment: numeric
	newLine = newLine + ' ' + lineParts[7]
	
	#urgent: numeric
	newLine = newLine + ' ' + lineParts[8]
	
	#hot: numeric
	newLine = newLine + ' ' + lineParts[9]
	
	#num_failed_logins: numeric
	newLine = newLine + ' ' + lineParts[10]
	
	#logged_in: categorical
	if (lineParts[11] not in loggedInMap):
		tempLen = len(loggedInMap)
		loggedInMap[lineParts[11]] = tempLen + 1
	newLine = newLine + ' ' + str(loggedInMap[lineParts[11]])

	#num_compromised: numeric
	newLine = newLine + ' ' + lineParts[12]
	
	#root_shel1: numeric
	newLine = newLine + ' ' + lineParts[13]
	
	#su_attempted: numeric
	newLine = newLine + ' ' + lineParts[14]
	
	#num_root: numeric
	newLine = newLine + ' ' + lineParts[15]
	
	#num_file_creations: numeric
	newLine = newLine + ' ' + lineParts[16]
	
	#num_shells: numeric
	newLine = newLine + ' ' + lineParts[17]
	
	#num_access_files: numeric
	newLine = newLine + ' ' + lineParts[18]
	
	#num_outbound_cmds: numeric
	newLine = newLine + ' ' + lineParts[19]
	
	#is_host_login: categorical
	if (lineParts[20] not in hostLoginMap):
		tempLen = len(hostLoginMap)
		hostLoginMap[lineParts[20]] = tempLen + 1
	newLine = newLine + ' ' + str(hostLoginMap[lineParts[20]])
	
	#is_guest_login: categorical
	if (lineParts[21] not in guestLoginMap):
		tempLen = len(guestLoginMap)
		guestLoginMap[lineParts[21]] = tempLen + 1
	newLine = newLine + ' ' + str(guestLoginMap[lineParts[21]])
	
	#count: numeric.
	newLine = newLine + ' ' + lineParts[22]
	
	#srv_count: numeric.
	newLine = newLine + ' ' + lineParts[23]
	
	#serror_rate: numeric.
	newLine = newLine + ' ' + lineParts[24]
	
	#srv_serror_rate: numeric.
	newLine = newLine + ' ' + lineParts[25]
	
	#rerror_rate: numeric.
	newLine = newLine + ' ' + lineParts[26]
	
	#srv_rerror_rate: numeric.
	newLine = newLine + ' ' + lineParts[27]
	
	#same_srv_rate: numeric.
	newLine = newLine + ' ' + lineParts[28]
	
	#diff_srv_rate: numeric.
	newLine = newLine + ' ' + lineParts[29]
	
	#srv_diff_host_rate: numeric.
	newLine = newLine + ' ' + lineParts[30]
	
	#dst_host_count: numeric.
	newLine = newLine + ' ' + lineParts[31]
	
	#dst_host_srv_count: numeric.
	newLine = newLine + ' ' + lineParts[32]
	
	#dst_host_same_srv_rate: numeric.
	newLine = newLine + ' ' + lineParts[33]
	
	#dst_host_diff_srv_rate: numeric.
	newLine = newLine + ' ' + lineParts[34]
	
	#dst_host_same_src_port_rate: numeric.
	newLine = newLine + ' ' + lineParts[35]
	
	#dst_host_srv_diff_host_rate: numeric.
	newLine = newLine + ' ' + lineParts[36]
	
	#dst_host_serror_rate: numeric.
	newLine = newLine + ' ' + lineParts[37]
	
	#dst_host_srv_serror_rate: numeric.
	newLine = newLine + ' ' + lineParts[38]
	
	#dst_host_rerror_rate: numeric.
	newLine = newLine + ' ' + lineParts[39]
	
	#dst_host_srv_rerror_rate: numeric.
	newLine = newLine + ' ' + lineParts[40]

	"""#class
	if (lineParts[41] not in classMap):
		tempLen = len(classMap)
		classMap[lineParts[41]] = tempLen + 1
	newLine = newLine + ' ' + str(classMap[lineParts[41]])"""
	if(lineParts[41].startswith('normal')):
		newLine = newLine + ' ' + '1'
	else:
		newLine = newLine + ' ' + '0'
	
	newLine = newLine.strip()
	outputFile.write(newLine + '\n')
	
inputFile.close()
outputFile.close()
