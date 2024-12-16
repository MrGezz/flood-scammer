import requests
import random
import string

def randPhone(start, n):
	phone = str(start)
	for a in range(n):
		phone += str(random.randint(0,9))
	return phone

def randOtp(n):
	otp = ''
	for a in range(n):
		otp += str(random.randint(0,9))
	return otp

def dictNames(dict):
	with open(dict,'r') as f:
		nameList = f.read().splitlines()
	x = len(nameList) - 1
	z = 0
	newNameList = []
	for a in range(x):
		newNameList.append(nameList[z] + ' '  + nameList[random.randint(0,int(x))])
		z += 1
	return newNameList

def randDictNames(dict):
	with open(dict, 'r') as f:
		nameList = f.read().splitlines()
	x = len(nameList) - 1
	z = 0
	newNameList = []
	for a in range(x):
		newNameList.append(nameList[random.randint(0,int(x))] + ' ' + nameList[random.randint(0,int(x))])
		z += 1
	return newNameList

newNames = randDictNames('names.txt')
scmUrl = 'https://www.instne.eu/a/bantuan/module/satu.php'
scmUrl2 = 'https://www.instne.eu/a/bantuan/module/dua.php'
scmUrl3 = 'https://www.instne.eu/a/bantuan/module/tiga.php'
scmUrl4 = 'https://www.instne.eu/a/bantuan/module/empat.php'
rn = 0

for name in newNames:
	full_name = name
	phone_number = randPhone('01',8)
	otp_code = randOtp(5)
	password = ''.join(random.choice(string.printable) for a in range(12))
	response = requests.post(scmUrl, allow_redirects = False, data = {
	'kad': full_name,
	'nomor': phone_number,
	#'otp_code': otp_code
	})
	response2 = requests.post(scmUrl2, allow_redirects = False, data = {
	'kode': otp_code
	})
	response3 = requests.post(scmUrl3, allow_redirects = False, data = {
	'kataLaluan': password
	#'otp_code': otp_code
	})
	status_text = ''
	status_text2 = ''
	status_text3 = ''
	if (response.status_code == 200):
		status_text = 'OK'
	elif (response.status_code == 302):
		status_text = 'Redirect'
	else:
		status_text = 'Unknown'
	if (response2.status_code == 200):
		status_text2 = 'OK'
	elif (response2.status_code == 302):
		status_text2 = 'Redirect'
	else:
		status_text2 = 'Unknown'
	if (response3.status_code == 200):
		status_text3 = 'OK'
	elif (response3.status_code == 302):
		status_text3 = 'Redirect'
	else:
		status_text3 = 'Unknown' 
	rn += 1
	#print(f'Phone: {phone_number}\nOTP: {otp_code}')
	print(f'Sequnce: {rn}')
	print(f'Name: {name}\nPhone: {phone_number}\nOTP: {otp_code}\nPass: {password}')
	print(f'Response: {status_text} {response.status_code}')
	print(f'Response2: {status_text2} {response2.status_code}')
	print(f'Response3: {status_text3} {response3.status_code}\n')
	#print(f'Response Headers: {response.headers['Content-Type']}\n')
