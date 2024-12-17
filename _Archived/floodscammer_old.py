import requests
import random

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
scmUrl = 'http://bantuantunai2024-gt1-pov.my.id/app7/secondData.php'
rn = 0

for name in newNames:
	full_name = name
	phone_number = randPhone('01',8)
	otp_code = randOtp(5)
	response = requests.post(scmUrl, allow_redirects = False, data = {
	'full_name': full_name,
	'phone_number': phone_number,
	'otp_code': otp_code
	})
	status_text = ''
	if (response.status_code == 200):
		status_text = 'OK'
	elif (response.status_code == 302):
		status_text = 'Redirect'
	else:
		status_text = 'Unknown' 
	rn += 1
	#print(f'Phone: {phone_number}\nOTP: {otp_code}')
	print(f'Sequnce: {rn}')
	print(f'Name: {name}\nPhone: {phone_number}\nOTP: {otp_code}')
	print(f'Response: {status_text} {response.status_code}')
	print(f'Response Headers: {response.headers['Content-Type']}\n')
