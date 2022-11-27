# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:27:19 2022

@author: kriti
"""
 
list1= [12,-7,5,64,-14]
print("Orginal numbers in the list:" ,list1)
new_list1 = list(filter(lambda x: x>0, list1))
print ("Positive numbers in the list :", new_list1)

list2=[12, 14, -95, 3]
print("Orginal numbers in the list:" ,list2)
new_list2 = list(filter(lambda x: x>0, list2))
print ("Positive numbers in the list :", new_list2)