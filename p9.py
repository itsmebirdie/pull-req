# a python program to read a text file and display the number of vowels, consonants, uppercase, lowercase characters in the file
f = open('file.txt','r')
vowels = 0
consonants = 0
upper = 0
lower = 0
for line in f:
    for i in line:
        if i.isupper():
            upper = upper + 1
        elif i.islower():
            lower = lower + 1
        if i.isalpha():
            if i in 'aeiouAEIOU':
                vowels = vowels + 1
            else:
                consonants = consonants + 1
print('Number of vowels: ',vowels)
print('Number of consonants: ',consonants)
print('Number of uppercase letters: ',upper)
print('Number of lowercase letters: ',lower)
f.close()