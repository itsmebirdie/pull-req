# python program to create to create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message
import pickle
f = open('file.dat','wb') 
n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter name: ')
    roll = int(input('Enter roll number: '))
    pickle.dump([name,roll],f)
f.close()
f = open('file.dat','rb')
roll = int(input('Enter roll number to search: '))
found = False
try:
    while True:
        name,rollno = pickle.load(f)
        if rollno == roll:
            print('Name: ',name)
            found = True
            break
except EOFError:
    if found == False:
        print('Roll number not found')
f.close()