# python program to create a binary file with roll number, name and marks. Input a roll number and update the marks
import pickle
f = open('file.dat','wb')
n = int(input('Enter number of students: '))
for i in range(n):
    roll = int(input('Enter roll number: '))
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    pickle.dump([roll,name,marks],f)
f.close()
f = open('file.dat','rb')
roll = int(input('Enter roll number to update marks: '))
found = False
try:
    while True:
        rollno,name,marks = pickle.load(f)
        if rollno == roll:
            marks = int(input('Enter new marks: '))
            found = True
            break
except EOFError:
    if found == False:
        print('Roll number not found')
f.close()
f = open('file.dat','rb')
f1 = open('file1.dat','wb')
try:
    while True:
        rollno,name,marks = pickle.load(f)
        if rollno == roll:
            pickle.dump([rollno,name,marks],f1)
        else:
            pickle.dump([rollno,name,marks],f1)
except EOFError:
    pass
f.close()
f1.close()
f = open('file.dat','wb')
f1 = open('file1.dat','rb')
try:
    while True:
        rollno,name,marks = pickle.load(f1)
        pickle.dump([rollno,name,marks],f)
except EOFError:
    pass
f.close()
f1.close()