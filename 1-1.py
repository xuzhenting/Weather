#!/usr/bin/python 
#-*-coding:utf-8-*- 

import requests
from bs4 import BeautifulSoup
import json
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017) 
db = client["Weather"]
collection = db["Taiwan"]

response = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-795EF9D7-1372-4710-B033-4E0B1DE72F98&format=JSON")
data_json = response.json()
location = data_json['records']["location"]

mongo = []
for i in location:
    for x in range(0,3):
        d = {}
        d["城市"] = i['locationName']    # 縣市名稱
        d["開始時間"] = i['weatherElement'][0]['time'][x]['startTime'] 
        d["結束時間"] = i['weatherElement'][0]['time'][x]['endTime'] 
        d["天氣現象"] = i['weatherElement'][0]['time'][x]['parameter']['parameterName']    # 天氣現象
        d["舒適度"] = i['weatherElement'][3]['time'][x]['parameter']['parameterName']    # 舒適度
        d["最高溫"] = i['weatherElement'][4]['time'][x]['parameter']['parameterName']+"度"  # 最低溫
        d["最低溫"] = i['weatherElement'][2]['time'][x]['parameter']['parameterName']+"度"  # 最高溫
        d["降雨機率"] = i['weatherElement'][2]['time'][x]['parameter']['parameterName']+"%"   # 降雨機率
        mongo.append(d)
collection.insert_many(mongo)        
print(mongo)

