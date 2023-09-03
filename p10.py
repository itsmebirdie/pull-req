# python program to remove all the lines that contain the character 'a' in a text file and write it to another file
f = open('file.txt','r')
f1 = open('file1.txt','w')
for line in f:
    if 'a' not in line:
        f1.write(line)
f.close()
f1.close()