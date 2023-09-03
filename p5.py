# Given 3 lists L1, L2, L3, write a python program to add individual elements of L2 and L3 to L1. The order of elemts in the resultant list should be elements of L1 followed by elements of L2 followed by elements of L3, L1 and L2.
L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
L3 = [11,12,13,14,15]
L1.extend(L2)
L1.extend(L3)
print(L1)