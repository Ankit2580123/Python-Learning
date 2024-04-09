#Random Password Generator
import random
import string

pass_length=12

all=string.ascii_letters+string.digits+string.punctuation

generated_pass=""
for i in range(pass_length):
                    one_password=random.choice(all)
                    generated_pass +=one_password
                    
print("Your Generated Password is: ",generated_pass)

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)