import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter the length of the password: "))

password = ''.join(random.choices(all_characters, k=length))

print("Your password is:", password)

# import the string and random modules
import string
import random

# define the characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# ask the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# generate a password using randomly chosen characters
# using the 'choices' function from the random module
# and joining the resulting characters into a string
password = ''.join(random.choices(all_characters, k=length))

# display the generated password to the user
print("Your password is:", password)

import random
import string

def generate_password(length, count):
    passwords = []
    for i in range(count):
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        passwords.append(password)
    return passwords

random
string
passwords = generate_password(8, 5)
print(passwords)
