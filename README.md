# BrutePin

# What is BrutePin?

It's a ROBLOX pin bruteforcer that tries every possible 4 digit pins in order to unlock whatever you want to do in its account. This is made by Tangly.

# Why is it asking me to get the account's cookie (ROBLOSECURITY) and CSRF token?

This is because it would require both of those in order to get the bad boy going. CSRF token is used for anti-XSS.

# How do I find the account's cookie (ROBLOSECURITY) and CSRF token?

You open up inspect element, open Network tab, and try to enter in some random pin, then find the unlock request, you will see this.
![](https://media.discordapp.net/attachments/743744964500127814/764601419625267242/unknown.png?width=469&height=475)

Then look for the cookie and x-csrf-token in request headers.

![](https://media.discordapp.net/attachments/743744964500127814/764602197958197258/unknown.png?width=470&height=475)
![](https://media.discordapp.net/attachments/743744964500127814/764602356448624640/unknown.png?width=468&height=475)

Copy its contents and paste them to whatever question it's asking for.

Made by Tangly <3
