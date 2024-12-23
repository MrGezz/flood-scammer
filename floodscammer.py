import requests
import fakedata_my as fd

scam_url = ''

name_obj = fd.namelist()
names = name_obj.load('names_MY.txt')

#one liner for the above code
#names = fd.namelist().load('names_MY.txt')

#Loop the proses for len(names) time
for a in range(len(names)):
	fake_data = fd.fakedata(names)

	#The data content is depend on the website. Inspect what data it sumbmitting via the post request
	response = requests.post(scam_url, allow_redirects = False, data = {
	'fullname': fake_data.name,
	'phone': fake_data.phone,
	'otp': fake_data.otp
	})
	status_text = ''
	if response.status_code == 200:
		status_text = 'OK'
	elif response.status_code == 302:
		status_text = 'Redirect'
	else:
		status_text = 'Undefined'

	#Change based on the desired output
	print(fake_data)
	print(f'Response: {status_text} {response.status_code}\n')
