import random
import string
import datetime

class fakedata:
	"""Generate fake Malaysian residence personal information data such as name, ic, phone and age.
	"""

	def random_phone(self, start, n):
		"""Generate random phone number

		Args:
			start: The starting number (str/int)
			n: The total character to generate after <start> argument

		Example:
			random_phone("01",8)
			output: 0112345678
		"""

		phone = str(start)
		for a in range(n):
			phone += str(random.randint(0,9))
		return phone

	def random_otp(self, n):
		"""Generate random OTP

		Args:
			n: The total character of the OTP

		Example:
			random_otp(5)
			output: 12345
		"""

		otp = ""
		for a in range(n):
			otp += str(random.randint(0,9))
		#otp = "".join(str(random.randint(0,9) for a in range(n)))
		return otp

	def random_name(self, dict):
		"""Randomly pick one name form a list

		Args:
			dict: The list of names

		Example:
			list = fakedata().name_dict("names.txt",2)
			random_name(list)
			output: NameC NameA
		"""

		n = len(dict) - 1
		name = dict[random.randint(0,int(n))]
		return name

	def random_ic(self, n, style):
		"""Generate random identity card ID and Age based on the ID. The gender will be based on the last digit of the generated ID.

		Args:
			n: Total character of the ID
			style: 1 or 2 where 1 is without dash.

		Example:
			random_ic(10,1)
			output: ("800101223333","44","Lelaki")

			random_ic(10,2)
			output: ("800101-22-3333","44","Lelaki")

			ic, age = random_ic(10,2)
			print(ic, age)
			output("800101-22-3333" "44" "Lelaki")
		"""

		year = str(random.randint(50,99))
		month = str(random.randint(1,12)).zfill(2)
		day = str(random.randint(1,31)).zfill(2)
		mid = str(random.randint(1,99)).zfill(2)
		last = str(random.randint(10,9999)).zfill(4)
		age = int(datetime.date.today().year) - (1900 + int(year))
		if style == 1:
			ic = year + month + day + mid + last
		elif style == 2:
			ic = year + month + day + "-" + mid + "-" + last
		else:
			ic = year + month + day + mid + last

		#Check if the last digit is even or odd
		if int(last[-1]) % 2 == 0:
			gender = "Perempuan"
		else:
			gender = "Lelaki"

		return ic, age, gender

	def random_job(self):
		"""Randomly choose one job type from the list.
		"""

		joblist = ["Kerajaan","Swasta","Sendiri"]
		return joblist[random.randint(0,int(len(joblist) - 1))]

	def random_bank(self):
		"""Generate random bank account from the default bank dictionary.
		"""

		banklist = {
		'1': ["AmBank Berhad",13,"888"],
		'2': ["CIMB Bank Berhad",10,"7"],
		'3': ["Maybank Berhad",12,"1"],
		'4': ["Alliance Bank",14,"12"],
		'5': ["Hong Leong Bank",10,"3"],
		'6': ["Public Bank Berhad",10,"5"],
		'7': ["OCBC Bank",10,"5"]
		}

		choose_bank = random.choice(list(banklist.values()))
		bank_name = choose_bank[0]
		bank_account = str(self.random_phone(choose_bank[2],(choose_bank[1] - len(choose_bank[2]))))

		return bank_name, bank_account

	def __init__(self, name_list):
		#name_list = self.name_dict(dict, 1)
		self.name = self.random_name(name_list)
		self.ic, self.age, self.gender = self.random_ic(10,1)
		self.phone = self.random_phone("01",8)
		self.otp = self.random_otp(5)
		self.job = self.random_job()
		self.bankname, self.bankaccount = self.random_bank()

	def __str__(self):
		data = f"Name: {self.name}\nIC: {self.ic}\nAge: {self.age}\nGender: {self.gender}\nPhone: {self.phone}\nJob: {self.job}\nBank Name: {self.bankname}\nAccount Number: {self.bankaccount}\nOTP: {self.otp}"

		return data

class namelist:
	"""Generate list of random names.
	"""

	def generate(self, dict, name_count):
		"""Create new list of two words list of name from a list of single word names randomly.

		Args:
			dict: The file that contains the name list (Ex: names.txt)
			name_count: How many names to generate

		Example:
			names.txt content is:
				NameA
				NameB
				NameC

			name_dict("names.txt", 2)
			output:
				NameA NameB
				NameC NameA
		"""

		with open(dict, "r") as f:
			name_list = f.read().splitlines()
		n = len(name_list) - 1
		new_name_list = []
		for a in range(name_count):
			new_name_list.append(name_list[random.randint(0,int(n))] + " " + name_list[random.randint(0,int(n))])
		return new_name_list

	def load(self, dict):
		"""Load list of names from file."""

		with open(dict, "r") as f:
			name_list = f.read().splitlines()
		return name_list