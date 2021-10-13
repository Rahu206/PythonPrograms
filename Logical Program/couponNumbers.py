'''
@Author: Rahul Deshpande
@Date: 2021-10-12 14:06:52
@Last Modified by: Rahul Deshpande
@Last Modified time:2021-10-12 14:06:52
@Title :  Program to find Distinct Coupon Number
'''

    # ------------------------------------------------------------------------------
    # a. Desc ­> Given N distinct Coupon Numbers, how many random numbers do you
    # need to generate distinct coupon number? This program simulates this random
    # process.
    # b. I/P ­> N Distinct Coupon Number
    # c. Logic ­> repeatedly choose a random number and check whether it's a new one.
    # d. O/P ­> total random number needed to have all distinct numbers.
    # e. Functions => Write Class Static Functions to generate random number and to
    # process distinct coupons
    # ------------------------------------------------------------------------------

import random

class CouponNumbers:

    def inputNoOfCoupon(self):  #method to take input from user for no of coupons
        while True:
            try:     # Exception handling
                numberOfCoupons = int(input("Enter the number of coupons: ")) #Taking input from user
                if numberOfCoupons <= 1:
                    print("Number of coupons should be greater than 1")
                    continue
                break
            except Exception as e:
                print(e)
        return numberOfCoupons        #Return no of coupons

    def findDistinctCoupons(self, totalCoupons):
        distinctCouponNos = []
        while len(distinctCouponNos) < totalCoupons:
            randomNumber = random.randint(1, totalCoupons)    #Generate random number between 1 to totalCoupons
            if randomNumber not in distinctCouponNos:
                distinctCouponNos.append(randomNumber)
        return distinctCouponNos

if __name__ == '__main__':  #main method
    couponNumbers = CouponNumbers()  #creating object of CouponNumbers Class
    numberOfCoupons = couponNumbers.inputNoOfCoupon()  #calling inputNumberOfCoupons through object
                                                       # reference and store its value in a variable
    ditinctCoupons = couponNumbers.findDistinctCoupons(numberOfCoupons) #calling findDistinctCoupons method
    print("Distinct coupons are: ", ditinctCoupons)  #Printing distinct coupons
