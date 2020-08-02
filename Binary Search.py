# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 23:33:56 2020

@author: SUPERNOVA2813
O(log base 2 n)
a searching algo requires a minimum number of comparisions in unsuccessful search

"""
#Array should be sorted inorder for the program to work
def BinarySearch(low,high):
    if(low>high):
        return -1
    center=(low+high)//2 # Dividing the list into half
    if(array[center]==data): # Checking if center data match with the element
        return center
    else:
        if(data>array[center]): #if data is greater than the center element
            return BinarySearch(center+1,high) # search the upper half
        else:
            return BinarySearch(low,center-1) # Else searcg the lower half


    
array=[x for x in input("Please enter the array elements in ascending order:").split(" ")]      
data=input("Enter the element to search:")

i=BinarySearch(0,len(array)-1)


if i<0:
    print("Data not found or array not in order!")
else:
    print("Element ",data," found at position ",i+1)            