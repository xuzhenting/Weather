#!/usr/bin/python 
#-*-coding:utf-8-*- 

import requests
from bs4 import BeautifulSoup
import json
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017) 
db = client["Weather"]
collection = db["Taiwan"]

a = ["001","005","009","013","017","021","025","029","033","037","041","045","049","053","057","061","065","069","073","077","081","085"]

for x in a :
    response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/"+"F-D0047-"+ str(x) +"?Authorization=CWB-795EF9D7-1372-4710-B033-4E0B1DE72F98&format=JSON")
    data_json = response.json()
    location = data_json["records"]["locations"][0]["location"]
    b = data_json["records"]["locations"][0]["locationsName"]
    collection = db["Taiwan - "+ b ]
    mongo = []
    for i in location:
        d = {}
        d["縣市名稱"] = i['locationName']
        d["降雨機率"] = i['weatherElement'][0]["time"]
        d["天氣現象"] = i['weatherElement'][1]["time"]
        d["體感溫度"] = i['weatherElement'][2]["time"]
        mongo.append(d)
    collection.insert_many(mongo)        
print(mongo)