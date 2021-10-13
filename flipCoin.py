'''
@Author: Rahul Deshpande
@Date: 2021-10-10 18:30:33
@Last Modified by: Rahul Deshpande
@Last Modified time: 2021-10-10 18:30:33
@Title :  Flip Coin and print percentage of Heads and Tails
'''
import random
no_Flip = int(input("Enter the value of coin to be fliped: "))
while no_Flip <= 0:
    print("Please enter only positive number..!")
    no_Flip = int(input("Enter the value of coin to be fliped: "))

def flipCoin(no_Flip):
    heads = 0
    tails = 0
    headPercentage = 0
    tailPercentage = 0
    for i in range(no_Flip):
        coin = random.random()
        if coin < 0.5:
            heads +=1
        else:
            tails +=1
    headPercentage = float(heads) * (100/no_Flip)
    tailPercentage = float(tails) * (100/no_Flip)
    print("Total Number of Heads    :",heads)
    print("Total Number of Tails    :",tails)
    print("Percentage of Head       :",round(headPercentage,2))
    print("Percentage of Tail       :",round(tailPercentage,2))
flipCoin(no_Flip)
