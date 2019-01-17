#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:35:45 2019

@author: NINI
"""

# request html
# BeautifulSoup scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd
#import numpy as np

# collect FI all location's websites
locations = str('[7021,"Rio de Janeiro 2019","Rio de Janeiro","Brazil","2019-07-14",-22.9068,-43.1729],[7381,"Hanoi 2019","Hanoi","Vietnam","2019-05-19",21.0278,105.834],[7231,"Londrina 2019","Londrina","Brazil","2019-04-21",-23.3113,-51.1595],[7271,"Kuala Lumpur 2019","Kuala Lumpur","Malaysia","2019-03-31",3.139,101.687],[7331,"Ho Chi Minh City 2019","Ho Chi Minh City","Vietnam","2019-03-31",10.8231,106.63],[6761,"Hamburg 2019","Hamburg","Germany","2019-03-24",53.5511,9.99368],[7301,"Bolivia 2019","Santa Cruz de la Sierra","Bolivia","2019-03-24",-17.7892,-63.1975],[6481,"Manila 2019","Manila","Philippines","2019-03-17",14.5995,120.984],[7311,"Warsaw Spring 2019","Warsaw","Poland","2019-03-17",52.2297,21.0122],[7211,"Campinas 2019","Campinas","Brazil","2019-03-10",-22.9099,-47.0626],[7191,"Waterloo 2019","Waterloo","Canada","2019-03-03",43.4643,-80.5204],[7321,"Buffalo Spring 2019","Buffalo","US","2019-03-10",42.8864,-78.8784],[6241,"London Winter 2019","London","United Kingdom","2019-03-03",51.5074,-0.127758],[7161,"Prague 2019","Prague","Czech Republic","2019-02-17",50.0886,14.4214],[6921,"Los Angeles Winter 2019","Los Angeles","US","2019-02-10",34.0522,-118.244],[7001,"Belo Horizonte 2019","Belo Horizonte","Brazil","2019-02-10",-19.9245,-43.9352],[6461,"Brasilia Fall 2019","Brasilia","Brazil","2019-02-10",-15.7942,-47.8822],[6781,"Sydney 2019","Sydney","Australia","2019-02-10",-33.8688,151.209],[7181,"Ramallah 2018","Ramallah","Palestine","2019-02-03",31.942,35.1961],[6951,"Bogota Spring 2019","Bogota","Colombia","2019-01-20",4.71099,-74.0721],[6451,"Jamaica 2019","Kingston","Jamaica","2019-02-03",18.0179,-76.8099],[6891,"Luxembourg 2019","Luxembourg City","Luxembourg","2019-01-27",49.6015,6.13267],[6771,"Pittsburgh Winter 2019","Pittsburgh","US","2019-01-27",40.4406,-79.9959],[6471,"Rome Fall 2018","Rome","Italy","2019-01-20",41.9028,12.4964],[6641,"Tucson 2019","Tucson","US","2019-01-20",32.2032,-111.001],[7131,"New York Winter 2019","New York","US","2019-01-13",40.7128,-74.0059],[5761,"Columbus Winter 2019","Columbus","US","2018-12-30",39.9612,-82.9988],[5881,"Montreal Winter 2019","Montreal","Canada","2018-12-09",45.5017,-73.5673],[6441,"Munich Fall 2018","Munich","Germany","2018-12-02",48.1351,11.582],[6401,"Berlin Winter 2019","Berlin","Germany","2018-12-09",52.52,13.405],[6161,"Helsinki Winter 2019","Helsinki","Finland","2018-12-16",60.1699,24.9384],[6721,"Yangon Winter 2019","Yangon","Myanmar","2018-12-16",16.8661,96.1951],[7071,"Kabul Winter 2019","Kabul","Afghanistan","2018-12-09",34.5553,69.2075],[6321,"Sacramento Winter 2019 ","Sacramento","US","2018-12-16",38.5816,-121.494],[6901,"Luanda 2018","Luanda","Angola","2018-11-25",-8.83999,13.2894],[6671,"Costa Rica 2019","San Jose","Costa Rica","2018-12-16",37.3382,-121.886],[6751,"Seattle 2019","Seattle","US","2018-12-09",47.6062,-122.332],[7041,"Silicon Valley Winter 2019","Silicon Valley","US","2018-12-16",37.3875,-122.058],[6831,"Oslo Winter 2019","Oslo","Norway","2018-12-02",59.9139,10.7522],[6801,"Chisinau Fall 2018","Chisinau","Moldova","2018-11-11",47.0105,28.8638],[6601,"Cairo 2018","Cairo","Egypt","2018-11-11",30.0444,31.2357],[6221,"Stockholm Fall 2018","Stockholm","Sweden","2018-11-11",59.3293,18.0686],[6561,"Barcelona Fall 2018","Barcelona","Spain","2018-11-11",41.3851,2.1734],[6271,"Bucharest Fall 2018","Bucharest","Romania","2018-11-11",44.4268,26.1025],[5821,"Dublin Fall 2018","Dublin","Ireland","2018-11-11",53.3498,-6.26031],[6851,"Istanbul Fall 2018","Istanbul","Turkey","2018-11-11",41.0082,28.9784],[6181,"Sofia Fall 2018","Sofia","Bulgaria","2018-11-04",42.6977,23.3219],[6031,"Johannesburg 2018","Johannesburg","South Africa","2018-10-21",-26.2041,28.0473],[6661,"Bangalore 2018","Bangalore","India","2018-10-07",12.9716,77.5946],[6121,"Boston Fall 2018","Boston","US","2018-10-14",42.3601,-71.0589],[6541,"Toronto Fall 2018","Toronto","Canada","2018-10-20",43.6532,-79.3832],[5871,"Lisbon Fall 2018","Lisbon","Portugal","2018-10-07",38.7223,-9.13934],[6701,"Austin Fall 2018","Austin","US","2018-10-07",30.2672,-97.7431],[6711,"San Francisco Fall 2018","San Francisco","US","2018-09-23",37.7749,-122.419],[7081,"National Incubation Center Peshawar Fall 2018","Peshawar","Pakistan","2018-08-26",34.0151,71.5249],[6251,"Curitiba Fall 2018","Curitiba","Brazil","2018-08-26",-25.429,-49.2671],[6361,"Seoul 2018","Seoul","South Korea","2018-08-19",37.5665,126.978],[6291,"Sao Paulo Fall 2018","Sao Paulo","Brazil","2018-08-19",-23.5505,-46.6333],[6351,"Johor Bahru 2018","Johor Bahru","Malaysia","2018-07-22",1.49266,103.741],[6151,"Buenos Aires 2018","Buenos Aires","Argentina","2018-08-05",-34.6037,-58.3816],[5961,"East Bay 2018","Oakland","US","2018-07-22",37.8044,-122.271],[6011,"Chennai 2018","Chennai","India","2018-07-08",13.0827,80.2707],[6001,"Hong Kong 2018","Hong Kong","Hong Kong","2018-06-24",22.3964,114.109],[5941,"Accra Spring 2018","Accra","Ghana","2018-06-24",5.60372,-0.186964],[6141,"Ribeirao Preto 2018","Ribeirao Preto","Brazil","2018-06-10",-21.1705,-47.8102],[5831,"Cincinnati Spring 2018 ","Cincinnati","US","2018-06-10",39.1031,-84.512],[5801,"Cordoba AR 2018","Cordoba","Argentina","2018-06-03",-31.4201,-64.1888],[6111,"Chicago Summer 2018","Chicago","US","2018-06-03",41.8781,-87.6298],[5911,"Denver Summer 2018","Denver","US","2018-05-20",39.7392,-104.99],[5571,"Cologne 2018","Cologne","Germany","2018-05-20",50.9375,6.96028],[5781,"Tunisia Spring 2018","Tunis","Tunisia","2018-04-29",36.8065,10.1815],[5971,"Milan 2018","Milan","Italy","2018-04-15",45.4642,9.18998],[6371,"Hangzhou Spring 2018","Hangzhou","China","2018-03-06",30.2741,120.155],[5121,"Arizona Winter 2018","Phoenix","US","2018-03-18",33.4484,-112.074],[5671,"Madrid Winter 2018","Madrid","Spain","2018-03-04",40.4168,-3.70379],[5261,"South Florida 2018 ","South Florida","US","2018-01-21",25.7617,-80.1918],[4691,"Tokyo 2018","Tokyo","Japan","2017-12-22",35.6895,139.692],[5391,"Washington DC Winter 2018","Washington DC","US","2017-12-22",38.9072,-77.0369],[5681,"DePaul 2018","DePaul","US","2018-01-04",41.8781,-87.6274],[5171,"Santiago 2018","Santiago","Chile","2018-01-07",-33.4489,-70.6693],[5631,"Islamabad 2017","Islamabad","Pakistan","2017-12-17",33.7294,73.0931],[5501,"Jakarta 2017","Jakarta","Indonesia","2017-11-05",-6.17447,106.823],[4821,"Yerevan 2017","Yerevan","Armenia","2017-10-29",40.1792,44.4991],[5071,"Mexico City Fall 2017","Mexico City","Mexico","2017-10-29",19.4326,-99.1332],[4861,"San Diego Fall 2017","San Diego","US","2017-10-15",32.7157,-117.161],[4461,"Philadelphia 2017","Philadelphia","US","2017-10-15",39.9526,-75.1652],[5051,"Atlanta 2017","Atlanta","US","2017-10-08",33.749,-84.388],[5111,"Taipei 2017","Taipei","Taiwan","2017-09-24",25.033,121.565],[5161,"Vancouver Fall 2017","Vancouver","Canada","2017-09-17",49.2827,-123.121],[5041,"Perth 2017","Perth","Australia","2017-07-23",-31.9505,115.86],[4651,"Greenville Spring 2017","Greenville","US","2017-05-28",34.8526,-82.394],[4851,"Penang 2017","Penang","Malaysia","2017-04-23",5.41635,100.333],[4641,"Ottawa Spring 2017","Ottawa","Canada","2017-04-02",45.4215,-75.6972],[4601,"Paris Spring 2017","Paris","France","2017-03-26",48.8566,2.35222],[4471,"Shenyang 2017","Shenyang","China","2017-03-18",41.8057,123.431],[4031,"Belgrade Winter 2017","Belgrade","Serbia","2017-02-26",44.7866,20.4489],[4391,"Zurich Winter 2017","Zurich","Switzerland","2017-03-05",47.3769,8.54169],[4191,"Lima 2017","Lima","Peru","2017-02-05",-12.0464,-77.0428],[3871,"Zagreb 2017","Zagreb","Croatia","2017-01-23",45.815,15.9819],[3821,"Morocco 2017","Rabat","Morocco","2017-01-11",33.9716,-6.84981],[4041,"Kolkata 2016","Kolkata","India","2016-11-27",22.5726,88.3639],[3961,"Zaragoza 2016","Zaragoza","Spain","2016-10-23",41.6488,-0.889085],[3851,"Melbourne 2016","Melbourne","Australia","2016-09-11",-37.8136,144.963],[3831,"Moscow 2016","Moscow","Russia","2016-09-11",55.7558,37.6173],[3761,"Fort Lauderdale-Boca Raton Summer 2016","Fort Lauderdale","US","2016-07-24",26.1224,-80.1373],[3361,"Bangkok 2016","Bangkok","Thailand","2016-06-26",13.7563,100.502],[3501,"Hyderabad Summer 2016","Hyderabad","India","2016-06-05",17.385,78.4867],[2951,"Orange County Spring 2016","Orange County","US","2016-04-17",33.7175,-117.831],[2721,"Abidjan 2016","Abidjan","Ivory Coast","2016-03-14",5.35995,-4.00826],[2331,"Andalusia Spring 2016","Andalusia","Spain","2016-03-20",37.8882,-4.77938],[2791,"Panama City 2016","Panama City","Panama","2016-03-06",8.98238,-79.5199],[2581,"Puerto Rico 2016","San Juan","US","2015-12-13",18.4655,-66.1057],[2161,"Bangladesh Fall 2015","Dhaka","Bangladesh","2015-11-27",23.8103,90.4125],[2181,"Miami 2015","Miami","US","2015-11-22",25.7617,-80.1918],[1991,"Cyprus 2015 ","Nicosia","Cyprus","2015-11-18",35.1856,33.3823],[2291,"Chengdu Winter 2015","Chengdu","China","2015-10-31",30.5728,104.067],[2081,"Karachi Fall 2015","Karachi","Pakistan","2015-11-02",24.8615,67.0099],[2071,"New Delhi Fall 2015","New Delhi","India","2015-10-08",28.6139,77.209],[2151,"Saint Petersburg Fall 2015","Saint Petersburg","Russia","2015-09-13",59.9343,30.3351],[2221,"Singapore Summer 2015","Singapore","Singapore","2015-08-16",1.35208,103.82],[1401,"Athens Spring 2015","Athens","Greece","2015-03-27",37.9838,23.7275],[1131,"Shenzhen Fall 2014","Shenzhen","China","2014-11-18",22.5431,114.058],[871,"Tallinn Autumn 2014","Tallinn","Estonia","2014-11-16",59.437,24.7536],[721,"Brussels Autumn 2014","Brussels","Belgium","2014-11-16",50.8503,4.35172],[461,"Kansai Spring 2014","Osaka","Japan","2014-04-27",34.6937,135.502],[155,"Honolulu Summer 2013","Honolulu","US","2013-07-07",21.3069,-157.858],[134,"Medellin Summer 2013","Medellín","Colombia","2013-05-19",6.2442,-75.5812],[149,"Rijeka Summer 2013","Rijeka","Croatia","2013-05-07",45.3271,14.4422]')
locations = locations.split("],")
# store the website link and the name of each location
mapid = list()
mapname = list()

for i in range(128):
    locations[i] = locations[i].replace('[', '')
    temp = locations[i].split(',')
    mapid.append(temp[0])
    mapname.append(temp[2])
    mapid.sort()
    mapid.remove('6371')

# fetch mentor's name and linkedin of each location
if __name__=='__main__':
    
    for i in range(127):
        target = 'https://fi.co/mentors/%s' % mapid[i]
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        # mentors' name
        texts = bf.find_all('h4', class_ = 'name')
        for j in range(len(texts)):
            texts[j]= texts[j].text.replace("<h4 class='name'>", "")
            texts[j] = texts[j].replace("\n", "")
        
        names = list(texts)
        
        # link of mentors' linkedin
        a = bf.find_all('a', class_ = 'link')
        linkedin = list()
        for j in range(len(a)):
            linkedin.append(a[j].get('href'))
        
        linkedin = filter(lambda s: 'linkedin.com' in s, linkedin)
        linkedin = list(linkedin)
        linkedin.pop()
        
        # store name and linkedin link into csv file
        
        FIname = pd.DataFrame(data = names)
        FIname.columns = ['name']
        FIlink = pd.DataFrame(data = linkedin)
        FIlink.columns = ['contact']
        FIcontact = pd.concat([FIname, FIlink], axis = 1)
        
        FIcontact.to_csv('%s.csv' % mapname[i])
        
        



