# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 22:56:26 2019

@author: A Amhar N
"""
#ini fungsi bikin url
def url (Lat, Lon):
    
    #Lat dan Lon bisa diperoleh dengan menggunakan loop untuk memperoleh several files
    NewBaseUrl = 'https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?'

    Request = 'request=execute'

    Identifiers = 'identifier=Regional'

    Parameters = 'parameters='
    # list of parameter available here: https://power.larc.nasa.gov/docs/v1/#examples

    Duration='startDate=YYYYMMDD&endDate=YYYYMMDD'
    #replace the YYYYMMDD with the duration

    UserCommunity = 'userCommunity=SSE'
    #SSE (Surface meteorology and Solar Energy),SB(sustainable Buildings), AG(Agroclimatology))

    TemporalAverage='tempAverage=DAILY'

    Output = 'outputList=CSV'
    #CSV,ASCII, JSON, etc

    Coordinates = 'lat='+str(Lat)+'&'+'lon='+ str(Lon)
    #La = Latitude, Lon = Longitude

    User = 'user=anonymous'

    Url = NewBaseUrl+Request+'&'+Identifiers+'&'+Parameters+'&'+Duration+'&'+UserCommunity+'&'+TemporalAverage+'&'+Output+'&'+Coordinates+'&'+User

    print (Url)

#Generate Coordinate 
# Fungsi Box 1, nlat = total pengulangan latitude (22), nlon total pengulangan longitude (40)
def box_1 (nlat,nlon):
    int (nlat)
    int (nlon)
    Lat = 0.7659
    Latakhir = -2.4852
    inclat = (Latakhir-0.7659)/nlat
    rinclat = round (inclat,4)
    Lon = 110.2623
    Lonakhir = 116.1950
    inclon = (Lonakhir-110.2623)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 1
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 110.2623
    print (i)
    return;

# Fungsi Box 2, nlat = total pengulangan latitude (40), nlon total pengulangan longitude (10)
def box_2 (nlat,nlon):
    int (nlat)
    int (nlon)
    Lat = 4.2995
    Latakhir = -0.7941
    inclat = (Latakhir-4.2995)/nlat
    rinclat = round (inclat,4)
    Lon = 116.2389
    Lonakhir = 117.1837
    inclon = (Lonakhir-116.2389)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 1
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 116.2389
    print (i)
    return;

# Fungsi Box 2, nlat = total pengulangan latitude (10), nlon total pengulangan longitude (10)
def box_3 (nlat,nlon):
    int (nlat)
    int (nlon)
    Lat = 0.8978
    Latakhir = -0.4425
    inclat = (Latakhir-0.8978)/nlat
    rinclat = round (inclat,4)
    Lon = 109.2516
    Lonakhir = 110.4821
    inclon = (Lonakhir-109.2516)/nlon
    rinclon = round(inclon,4)
    ilat = 1
    ilon = 1
    i = 1
    while ilat <= nlat :
        while ilon <= nlon:
            Lon = Lon + rinclon
            Lon = round (Lon,4)
            ilon = ilon+1
            url(Lat,Lon)
            #print (str (Lat)+','+str(Lon))
            i = i+1
        ilat = ilat+1
        ilon = 1
        Lat = Lat+rinclat
        Lat = round (Lat,4)
        Lon = 109.2516
    print (i)
    return;
    
box_1(22,40)
box_2 (40,10)
box_3(10,10)

