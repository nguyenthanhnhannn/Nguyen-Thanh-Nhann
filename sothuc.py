# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:09:55 2024

@author: Hi
"""
import math 
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
tu1=math.sqrt(a)-math.sqrt(b)
mau2=a**(1/4)-b**(1/4)
tu3=math.sqrt(a)+(a*b)**(1/4)
mau4=a**(1/4)+b**(1/4)
ketqua=(tu1/mau2)-(tu3/mau4)
print("ket qua cua bieu thuc la:", ketqua)
