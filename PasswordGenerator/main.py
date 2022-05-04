import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-']

print("Python Password Generator !!!")
alpha = int(input("Enter number of alphabets you need :: "))
num = int(input("Enter number of numbers you need :: "))
syb = int(input("Enter number of symbols you need :: "))

alpha_list = []
num_list = []
sym_list = []

for i in range(0, alpha):
    alpha_list.append(random.choice(alphabets))

for i in range(0, num):
    num_list.append(random.choice(numbers))

for i in range(0, syb):
    sym_list.append(random.choice(symbols))

password = alpha_list+num_list+sym_list
random.shuffle(password)

final_password = ""
for i in password:
    final_password += i

print(final_password)
