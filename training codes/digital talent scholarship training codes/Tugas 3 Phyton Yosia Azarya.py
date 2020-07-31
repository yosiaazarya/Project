# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 07:03:15 2019

@author: YOSIA AZARYA
"""

print ("Tugas 3 Phyton Programming")
print ("Yosia Azarya")
print()

print("""
      Simple calculator
      """) #kalkulator sederhana tambah kurang kali bagi 2 angka

num1 = int (input ("Masukkan angka pertama: ")) #Input angka untuk diperasi
ope = str (input ("Masukkan operator (+ - * /): ")) #input operator
num2 = int (input ("masukkan angka kedua: ")) #Input angka kedua untuk dioperasi

if (ope == "+"):
    print (num1 , "+", num2, "=", (num1 + num2))
elif (ope == "-"):
    print (num1 , "-", num2, "=", (num1 - num2))
elif (ope == "*"):
    print (num1 , "*", num2, "=", (num1 * num2))
elif (ope == "/"):
    print (num1 , "/", num2, "=", (num1 / num2))
else:
    print ("operator tidak dapat digunakan")
