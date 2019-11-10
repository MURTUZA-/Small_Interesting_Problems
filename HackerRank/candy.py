'''
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line and each of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.

For example, assume her students' ratings are [4, 6, 4, 5, 6, 2]. She gives the students candy in the following minimal amounts: [1, 2, 1, 2, 3, 1]. She must buy a minimum of 10 candies.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
candy_dict = {}

def assign_candy(n, arr, index):
    global candy_dict
    if arr[index]==1:
        candy_dict[index]=1
        return 1
    left_count = right_count = -1

    if index-1 >= 0 and arr[index-1]<= arr[index]:
            if index-1 in candy_dict.keys():
                if arr[index-1]== arr[index]:
                    left_count = 1
                else:
                    left_count = candy_dict[index-1]+1
            else:
                if arr[index-1]<arr[index]:
                    value = assign_candy(n, arr, index-1)
                    candy_dict[index-1]=value
                    left_count = value+1
    
    if index+1<n and arr[index+1]<= arr[index]:
        if index+1 in candy_dict.keys():
            if arr[index+1]== arr[index]:
                right_count = 1
            else:
                right_count = candy_dict[index+1]+1
        else:
            if arr[index+1]<arr[index]:
                value = assign_candy(n, arr, index+1)
                candy_dict[index+1]=value
                right_count= value+1
    
    if left_count==-1 and right_count==-1:
        candy_dict[index]=1
        return 1
    else:
        candy_dict[index]=max(left_count, right_count)
        return candy_dict[index]





def candies(n, arr):
    count=0
    for index in range(n):
        if index in candy_dict.keys():
            count+=candy_dict[index]
        else:
            count += assign_candy(n,arr,index)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

