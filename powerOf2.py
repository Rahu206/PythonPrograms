'''
@Author: Rahul Deshpande
@Date: 2021-10-10 19:30:52
@Last Modified by: Rahul Deshpande
@Last Modified time:2021-10-10 19:30:52
@Title :  Flip Coin and print percentage of Heads and Tails
'''
n = int(input("Enter value of N : "))
while n < 0 or n >= 31:
    print("please enter the value of N between 0 to 31...!")
    n = int(input("Enter value of N again : "))

i = 0
powerOf2 = 1
print("Table of powers of 2 is : ")
while i <= n:
    print(i,powerOf2)
    powerOf2 = 2 * powerOf2
    i=i+1