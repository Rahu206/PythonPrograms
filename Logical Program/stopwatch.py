'''
@Author: Rahul Deshpande
@Date: 2021-10-12 13:09:34
@Last Modified by: Rahul Deshpande
@Last Modified time: 2021-10-12 13:09:34
@Title :Stopwatch Program for measuring the time that elapses between
the start and end clicks
'''

import time
class StopWatch:
    try:
        while True:
            # print("Enter 1 to Start Time:");
            start = int(input("Enter 1 to Start:"))
            startTime = time.time()
            stop = int(input("Enter 0 to Stop Time:"))
            endTime = time.time()
            timeElapsed = endTime - startTime
            print("Time elapsed from Start to End is : ", timeElapsed, " Sec")
    except ValueError:
        print("Invalid input ")