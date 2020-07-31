# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:09:04 2019

@author: YOSIA AZARYA
"""

import math #memanggil modul math untuk keperluan sqrt

print ("Tugas 1 Phyton Programming")
print ("Yosia Azarya")
print ()
print("""
      This program will show you
      C = squareroot of A squared plus B squared
      """)
A = int (input("Masukkan nilai A: "))
B = int (input("Masukkan nilai B: "))
A = A*A
B = B*B
C = math.sqrt(A+B) #membuat persamaan untuk mendapat nilai C
print ("Nilai C=", C)
