# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:26:55 2019

@author: A Amhar N
"""

import os
import json
#import csv
import pandas as pd
#from pprint import pprint

def outputdaya(Hum,Temp,ASky):
    #rumus menghitung effiesiensi pv panel efek temp dan humidity
    eff = (((Hum*-0.1518)+17.222-((Temp-25)*0.5))/100)
    #print (eff)
    output = ASky*eff/24*1000
    return (output)
    #print(output)
def effisiensi (Hum,Temp):
    eff = (((Hum*-0.1518)+17.222-((Temp-25)*0.5))/100)
    return (eff)

IsiFile = os.scandir('D:/Data Project DTS/')
ListFile = []
ListLatitude = []
ListLongitude = []
ListT2M = []
ListAllSky = []
ListQV2M = []
ListRH2M = []
ListOutput = []
ListEfisiensi = []
ListCoordinate = []
IndexData = 0
FileKe = 1

with IsiFile as Entries:
    for entry in Entries:
        if entry.is_file():
            ListFile.append(entry.name)
for Namafile in ListFile:
    with open('D:/Data Project DTS/'+Namafile) as f:
        print ('Nama File ', Namafile, ' File ke ', FileKe)
        data = json.load(f)
        features = data['features']
        ValueFeatures = features[0]
        Geometry = ValueFeatures ['geometry']
        Coordinate = Geometry ['coordinates']
        #Format Coordinate dalam bentuk list [lon, Lat, Belum tau ini apa, altitude mungkin]
        CoordinateLat = Coordinate[1]
        ListLatitude.append(CoordinateLat)
        CoordinateLon = Coordinate[0]
        ListLongitude.append(CoordinateLon)
        Coordinate = str (CoordinateLat)+ ',' + str (CoordinateLon)
        ListCoordinate.append (Coordinate)
        Properties = ValueFeatures['properties']
        Parameter = Properties['parameter']
        ParameterKey = ['T2M','ALLSKY_SFC_SW_DWN','QV2M','RH2M']
        for Key in ParameterKey:
            DateData= Parameter[Key]
            ListValue = list (DateData.values())
            for Value in ListValue:
                if Value == -999:
                    ListValue.remove(-999)
                    continue
            SumofData = 0
            for Value in ListValue:
                SumofData = SumofData+Value
            AverageofData = SumofData/len(ListValue)
            if Key == 'T2M':
                AverageofData4 = round (AverageofData,4)
                ListT2M.append(AverageofData4)
            elif Key == 'ALLSKY_SFC_SW_DWN' :
                AverageofData4 = round (AverageofData,4)
                ListAllSky.append(AverageofData4)
            elif Key == 'QV2M':
                AverageofData4 = round (AverageofData,4)
                ListQV2M.append(AverageofData4)
            elif Key == 'RH2M':
                AverageofData4 = round (AverageofData,4)
                ListRH2M.append(AverageofData4)
            else:
                continue
        print ("Assign Data Complete")
        FileKe= FileKe+1
        
print ('All File Complete')
while IndexData < len (ListFile):
    print ('Ini index data ke ', IndexData)
    DayaPV = round (outputdaya(ListRH2M[IndexData],ListT2M[IndexData],ListAllSky[IndexData]),4)
    EffisiensiPV = round (effisiensi (ListRH2M[IndexData],ListT2M[IndexData]),4)
    ListOutput.append(DayaPV)
    ListEfisiensi.append(EffisiensiPV)
    IndexData = IndexData+1
print ("Creating Data Frame")    
MeanDataNasa = {'Latitude' : ListLatitude, 'Longitude' : ListLongitude, 'Coordinate': ListCoordinate, 'Temperature at 2 Meters' : ListT2M,'All Sky Insolation Incident on a Horizontal Surface' : ListAllSky, 'Specific Humidity at 2 Meters' : ListQV2M, 'Relative Humidity at 2 Meters' : ListRH2M, 'Efisiensi' : ListEfisiensi, 'Output' : ListOutput }
#print (df)
df = pd.DataFrame(MeanDataNasa)
print ("Data Frame Created")
df = df.sort_values(by='Output', ascending=False)
print ("Sorting berhasil")
df.to_csv('D:/Data Project DTS/Final dengan efisiensi.csv', index = False)
print ("File Created")

