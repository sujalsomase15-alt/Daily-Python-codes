
# mini project for Random Password Generator

import random
import string

pass_len = 8

charValue = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(pass_len):
    password += random.choice(charValue)

print("your random password is:", password)

#list comprehension[function for i in range(n)]
password = "".join([random.choice(charValue) for i in range(pass_len)])