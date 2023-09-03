# A python program to read a line and print number of uppercase letters, number of lowercase letters, number of alphabets and number of digits in it
line = input('Enter a line: ')
upper = 0
lower = 0
alpha = 0
digit = 0
for i in line:
    if i.isupper():
        upper = upper + 1
    elif i.islower():
        lower = lower + 1
    if i.isalpha():
        alpha = alpha + 1
    elif i.isdigit():
        digit = digit + 1
print('Number of uppercase letters: ',upper)
print('Number of lowercase letters: ',lower)
print('Number of alphabets: ',alpha)
print('Number of digits: ',digit)