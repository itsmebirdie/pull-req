# a python function to check whether a number entered by user is even or odd
def even_odd(n):
    if n%2==0:
        print('Even')
    else:
        print('Odd')
n = int(input('Enter a number: '))
even_odd(n)