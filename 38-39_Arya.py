import requests, json, geocoder
from pprint import pprint
r=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=1dc7df1cf6d330b794b296dbdc11f643&q=" + input("City: ")).json() 
if r["cod"] != "404" and r["cod"] != "401":
    print("The temperature is " +str(r["main"]["temp"]) + " Kelvin. The atmospheric pressure is " + str(r["main"]["pressure"]) + " hPa. The humidity is " + str(r["main"]["humidity"]) + "%. There is currently a " +str(r["weather"][0]["description"])+".") 
elif r["cod"] == "404":
    r=requests.get("http://api.openweathermap.org/data/2.5/weather?appid=1dc7df1cf6d330b794b296dbdc11f643&q=" + geocoder.ip('me').geojson['features'][0]['properties']['city']).json()
    print("I could not find that city. Here is the informaation for where you live ("+geocoder.ip('me').geojson['features'][0]['properties']['city']+"):")
    print("The temperature is " +str(r["main"]["temp"]) + " Kelvin. The atmospheric pressure is " + str(r["main"]["pressure"]) + " hPa. The humidity is " + str(r["main"]["humidity"]) + "%. There is currently a " +str(r["weather"][0]["description"])+".") 
else:
    print("API Key is invalid")
