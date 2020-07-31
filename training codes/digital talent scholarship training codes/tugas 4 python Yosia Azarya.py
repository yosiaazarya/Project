# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:23:43 2019

@author: YOSIA AZARYA
"""

print ("Tugas 4 Phyton Programming")
print ("Yosia Azarya")
print ()

daftar_nilai = [86,75,55,90,98,87,65,87,85,68]
n = 0



b = len(daftar_nilai)


def avgnilai (lst):
    sum = 0
    for each in daftar_nilai:
        sum = sum + each
        avg = sum/b

    print ("Rata-rata nilai peserta DTS adalah: ", avg)

avgnilai(daftar_nilai)

def maksnilai (lst):
    nilai_tertinggi = 0
    for num in daftar_nilai:
    
        if (nilai_tertinggi < num):
            nilai_tertinggi = num
        
    print ("Nilai tertinggi peserta DTS adalah: ", nilai_tertinggi) 
maksnilai(daftar_nilai)

def minnilai (lst):
   nilai_terendah = daftar_nilai[n] 
   for num in daftar_nilai:
        if (nilai_terendah > num):
            nilai_terendah = num
   print ("Nilai terendah peserta DTS adalah: ", nilai_terendah) 
        
minnilai (daftar_nilai)
 