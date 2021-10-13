'''
@Author: Rahul Deshpande
@Date: 2021-10-10 18:00:30
@Last Modified by: Rahul Deshpande
@Last Modified time: 2021-10-10 18:00:30
@Title : Print the String with User Name
'''
strtemp = "Hello <<UserName>>, How are you?"
username = input("Enter User Name: ")
if len(username) < 3:
	print("User Name must have 3 characters.")
else:
	print(strtemp.replace("<<UserName>>",username))