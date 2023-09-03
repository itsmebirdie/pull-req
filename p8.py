# a python program to read a text file line by line and display each word separated by a # symbol
f = open('file.txt','r')
for line in f:
    words = line.split()
    for word in words:
        print(word,end='#')
    print()
f.close()