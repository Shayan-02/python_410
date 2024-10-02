import requests
import ipapi

myip = requests.get("http://api.ipify.org/").text

ip_loc = ipapi.location(myip)["country_code"]

if ip_loc == "IR":
    print("lotfan VPN zade va badesh varede abzar shid !!!")
    exit
else:
    print("khosh omadi!")