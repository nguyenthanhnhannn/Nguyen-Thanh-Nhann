# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:49:30 2024

@author: Hi
"""

n = int(input("Nhập năm sinh: "))
if n >= 1900 and n < 2024: 
    t = 2024 - n 
    print(f" bạn sinh năm {n} vậy bạn {t} tuổi: ")
elif n == 2024:
    print("Bạn chưa được 1 tuổi ")
else: 
    print("Năm sinh bạn nhập không hợp lệ: ")
    
    

