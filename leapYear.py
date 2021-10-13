'''
@Author: Rahul Deshpande
@Date: 2021-10-10 19:04:30
@Last Modified by: Rahul Deshpande
@Last Modified time:2021-10-10 19:04:30
@Title : Print the year is a Leap Year or not
'''
year = input("Enter a year value : ") # Taking the year input
while len(year) > 4 or len(year) < 4:
    print("Year should be 4 digit Number...!")
    year = input("Enter a year value : ")

def isLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

if isLeap(int(year)):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
