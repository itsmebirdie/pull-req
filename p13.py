# python program to create a csv file saving information about products. (ProductID, ProductName, ProductPrice, ProductQuantity)
import csv
f = open('file.csv','w',newline='')
w = csv.writer(f)
n = int(input('Enter number of products: '))
for i in range(n):
    pid = int(input('Enter product id: '))
    pname = input('Enter product name: ')
    pprice = int(input('Enter product price: '))
    pquantity = int(input('Enter product quantity: '))
    w.writerow([pid,pname,pprice,pquantity])
f.close()