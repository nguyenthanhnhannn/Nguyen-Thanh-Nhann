# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:36:49 2024

@author: Hi
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
tong = a + b
hieu = a - b 
tích = a * b 
thuong = a / b 
chia_du = a % b 
chia_nguyen = a // b 
print("Tổng của a và b là:" , tong)
print("Hiệu của a và b là:" , hieu)
print("Tích của a và b là:" , tích)
print("Thương của a và b là:" , thuong)
print("Thương làm tròn 2 chữ số:" ,round(thuong,2))
print("Thương làm tròn 3 chữ số:" ,round(thuong,3))
print("Chia lấy dư của a và b là:" , chia_du)
print("Chia lấy nguyên của a và b là:" , chia_nguyen)
