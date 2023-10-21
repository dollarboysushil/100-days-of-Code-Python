import random
import string



print("Welcome to the PyPassword Generator!")
lett_amt = int(input ("How many letters would you like in your password?"))
sym_amt = int(input(("How many symbols would you like?")))
num_amt = int(input("How many numbers would you like?"))

password = ""
letter = string.ascii_letters
symbol = string.punctuation
number  = string.digits

for _ in range(1, lett_amt+1):
    password = password + random.choice(letter)

for _ in range(1 ,sym_amt+1):
    password += random.choice(symbol)

for _ in range(1 , num_amt+1):
    password += random.choice(number)


# Shuffling the characters in password variable
password = list(password)
random.shuffle(password)

password2 = ''.join(password)
print(password2)