# BrutePin

## Table of Contents

- [Update Logs](#update-logs)
- [What is BrutePin?](#what-is-brutepin)
- [Why Does BrutePin Require the Account's Cookie (ROBLOSECURITY) and CSRF Token?](#why-does-brutepin-require-the-accounts-cookie-roblosecurity-and-csrf-token)
- [How Do I Obtain the Account's Cookie (ROBLOSECURITY) and CSRF Token?](#how-do-i-obtain-the-accounts-cookie-roblosecurity-and-csrf-token)
- [Can I Use BrutePin on Accounts I Don't Have Access To?](#can-i-use-brutepin-on-accounts-i-dont-have-access-to)

---

## Update Logs
```
[i] 10/12/2020 - Added Colorama to BrutePin and an option to read the cache (currently broken, refer to the first issue if you want; considered beta for now).
[i] 10/13/2020 - Added requirements.txt for users to install necessary modules to run this tool.
```

## What is BrutePin?

BrutePin is a ROBLOX pin bruteforcer that systematically tries every possible 4-digit pin to gain access to specific functionalities within a ROBLOX account. This tool was created by Tangly.

## Why Does BrutePin Require the Account's Cookie (ROBLOSECURITY) and CSRF Token?

BrutePin needs both the ROBLOSECURITY cookie and the CSRF token to function. The CSRF token is essential for preventing Cross-Site Request Forgery (CSRF) attacks, where unauthorized actions are performed using a user's identity without their consent.

## How Do I Obtain the Account's Cookie (ROBLOSECURITY) and CSRF Token?

To obtain these tokens:
1. Open the browser's developer tools (inspect element).
2. Navigate to the Network tab.
3. Attempt to enter a random pin using BrutePin.
4. Locate the unlock request in the network traffic details.

You will find the required tokens (`cookie` and `x-csrf-token`) in the request headers.

![Cookie and CSRF Token](https://media.discordapp.net/attachments/743744964500127814/764601419625267242/unknown.png?width=469&height=475)

![Request Headers](https://media.discordapp.net/attachments/743744964500127814/764602197958197258/unknown.png?width=470&height=475)
![Request Headers](https://media.discordapp.net/attachments/743744964500127814/764602356448624640/unknown.png?width=468&height=475)

Copy the contents of these tokens and paste them into BrutePin when prompted.

## Can I Use BrutePin on Accounts I Don't Have Access To?

No, BrutePin is designed to be used only on accounts where you have legitimate access and authorization.

Created by Tangly <3  
With assistance from pr0xy1337