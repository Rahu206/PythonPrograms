'''
@Author: Rahul Deshpande
@Date: 2021-10-11 16:30:52
@Last Modified by: Rahul Deshpande
@Last Modified time:2021-10-11 16:30:52
@Title :  Print function to print 2 Dimensional Array
'''
row = int(input("Enter the size of row: "))
col = int(input("Enter the size of col: "))

element = []
print("Enter Array Elements : ")
for i in range(row):
    a = [i]
    for j in range(col):
        a.append(int(input()))
    element.append(a)

for i in range(row):
    for j in range(col):
        print(element[i][j],end=" ")
    print()