# flood-scammer

This project is created to randomly generate fake personal information specifically for Malaysia residence from a class called fakedata. A demonstration of Object-Oriented Programming in Python. Features include:
* Pick name from list of names
* Generate random Malaysian Identity Card Number
* Assign Age and Gender based on the generated IC Number
* Generate random phone number
* Generate random OTP
* Pick random bank from list and generate Account Number according to picked bank
* Pick random job type from a list

## Getting Started

These instructions will get you a brief overview of how to start testing and using this.

### Prerequisites

You need Python 3.x or above to use this. All the library used are installed by default with Python.

## Running the tests

Import the fakedata_my.py into your main code:

```
import fakedata_my as fd
```

### Creating object from the class fakedata

Create name list from the file called names_MY.txt:

```
#import list of names with the class namelist()
names_data = fd.namelist()
names = names_data.load("names_MY.txt")
```

Create the fake personal data:

```
#using the previous name list created
info = fd.fakedata(names)
```

You can print the content of info with:

```
print(info)
```

Example output:

```
Name: Siti Khatijah
IC: 600424737310
Age: 64
Gender: Perempuan
Phone: 0190967974
Job: Sendiri
Bank Name: AmBank Berhad
Account Number: 8884761905878
OTP: 37853
```

You can access and modify each of the attributes:

```
print(info.job)
>>> Sendiri
info.job = "new job type"
print(info.job)
>>> new job type
```

Or modify it by calling the function used to randomize the value:

```
info.job = info.random_job()
print(info.job)
>>> new job type
```

Here is the list of important functions:
* random_name(dict)
* random_phone(start,n)
* random_ic(n, style)
* random_otp(n)
* random_job()
* random_bank()

For more information of the function you can access it with this:

```
help(fakedata_my)
```
or
```
print(info.__doc__)
```

## Authors

* **Pazran** - *Initial work* - [Pazran](https://github.com/Pazran)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
