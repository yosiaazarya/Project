# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:56:26 2019

@author: A Amhar N
"""
import json
import urllib3
import time

#ini fungsi bikin url
def url (Lat, Lon):
    
    SD = 20140901
    ED = 20190831
    NewBaseUrl = 'https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?'

    Request = 'request=execute'

    Identifiers = 'identifier=SinglePoint'
    #Regional untuk area, SinglePoint untuk titik

    Parameters = 'parameters=T2M,ALLSKY_SFC_SW_DWN,QV2M,RH2M'
    # list of parameter available here: https://power.larc.nasa.gov/docs/v1/#examples
    
    Duration='startDate='+str(SD)+'&'+'endDate='+ str (ED)
    #replace the YYYYMMDD with the duration

    UserCommunity = 'userCommunity=SSE'
    #SSE (Surface meteorology and Solar Energy),SB(sustainable Buildings), AG(Agroclimatology))

    TemporalAverage='tempAverage=DAILY'

    Output = 'outputList=JSON'
    #CSV,ASCII, JSON, etc

    Coordinates = 'lat='+str(Lat)+'&'+'lon='+ str(Lon)
    #La = Latitude, Lon = Longitude

    User = 'user=anonymous'

    Url = NewBaseUrl+Request+'&'+Identifiers+'&'+Parameters+'&'+Duration+'&'+UserCommunity+'&'+TemporalAverage+'&'+Output+'&'+Coordinates+'&'+User
    time.sleep(30)
    print (Url)
    
    http = urllib3.PoolManager()
    read = http.request ('GET', Url)
    Namafile = str (Lat) + ','+ str (Lon)
    #DataNasa = pd.read_json(Url)
    DataNasa = json.loads(read.data.decode('utf-8'))
    #read.to_json(Namafile+'.json')
    with open (Namafile+'.json','w') as myfile:
        json.dump(DataNasa,myfile)

#Generate Coordinate 
# Fungsi Box 1, nlat = total pengulangan latitude (22), nlon total pengulangan longitude (40)
def box_1 (nlat,nlon):
    int (nlat)
    int (nlon)
    Lat = -1.5989
    #0.7659
    Latakhir = -2.4852
    inclat = (Latakhir-0.7659)/nlat
    rinclat = round (inclat,4)
    Lon = 112.3385
    #110.4106
    #110.2623
    Lonakhir = 116.1950
    inclon = (Lonakhir-110.2623)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 0
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
            print (i)
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 112.3385
        #110.4106
        #110.2623
    return;

# Fungsi Box 2, nlat = total pengulangan latitude (40), nlon total pengulangan longitude (10)
def box_2 (nlat,nlon):
    int (nlat)
    int (nlon)
    #4.2995
    Lat = 2.39
    Latakhir = -0.7941
    inclat = (Latakhir-4.2995)/nlat
    rinclat = round (inclat,4)
    Lon = 116.7114
    #116.2389
    Lonakhir = 117.1837
    inclon = (Lonakhir-116.2389)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 0
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
            print (i)
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 116.7114
        #116.2389
    
    return;

# Fungsi Box 2, nlat = total pengulangan latitude (10), nlon total pengulangan longitude (10)
def box_3 (nlat,nlon):
    int (nlat)
    int (nlon)
    #0.8978
    #-0.0402
    Lat = -0.0402
    Latakhir = -0.4425
    inclat = (Latakhir-0.8978)/nlat
    rinclat = round (inclat,4)
    Lon = 109.744
    #109.744
    #109.2516
    Lonakhir = 110.4821
    inclon = (Lonakhir-109.2516)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 0
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            #url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
            print (i)
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 109.744
        #109.2516
    return;
    
box_1(22,40)
#box_2 (40,10)
#box_3(10,10)

