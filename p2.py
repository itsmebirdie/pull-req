# A python program to print sum of sqaures of first n natural numbers
n = int(input('Enter a number: '))
sum = 0
for i in range(1,n+1):
    sum = sum + i*i
print('Sum of squares of first n natural numbers: ',sum)