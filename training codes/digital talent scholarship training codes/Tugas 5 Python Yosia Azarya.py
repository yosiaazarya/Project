# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:20:25 2019

@author: YOSIA AZARYA
"""

class Karyawan:
    cuti = 12
    gaji = 10000000
    def __init__ (self, nama, jenis_kelamin, alamat, tanggal_lahir):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat
        self.tanggal_lahir =  tanggal_lahir
        print (self.nama, self.jenis_kelamin, self.alamat, self.tanggal_lahir)
        
    def ubahalamat (self, alamat):
        self.alamat = alamat
        print ()
        print ("Alamat baru ", self.nama, "adalah ", self.alamat)
        print ()
                
    def ajukancuti (self, cutidiambil):
        if (self.cuti-cutidiambil >= 0): 
            print ("Selamat cuti berhasil diambil jumlah sisa cuti ", self.nama , "Adalah" , self.cuti-cutidiambil)
            print ()
        else:
            print ("jumlah hari cuti tidak tersedia")
            
    def tampilkangaji (self):
        print ()
        print ("Gaji" , self.nama, self.gaji)        

class Manajer(Karyawan):
    cuti = 15 
    gaji = 10000000
    pass
    
emp1 = Karyawan ("Budi ", "Laki-Laki ", "Depok ", "1 Januari 1990 ")
emp2 = Manajer ("Ani ", "Perempuan ", "Jakarta ", "2 Januari 1989 ")
emp3 = Manajer ("Tono ", "Laki-laki ", "Bandung ", "3 Januari 1989 ")

emp3.tampilkangaji ()
emp1.ubahalamat ("Surabaya ")
emp2.ajukancuti (3)
