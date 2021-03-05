# BrutePin

# Table of Contents

[Update Logs](https://github.com/Luckytrang2010/BrutePin#update-logs)

[What is BrutePin?](https://github.com/Luckytrang2010/BrutePin#what-is-brutepin)

[Why is it asking me to get the account's cookie (ROBLOSECURITY) and CSRF token?](https://github.com/Luckytrang2010/BrutePin#why-is-it-asking-me-to-get-the-accounts-cookie-roblosecurity-and-csrf-token)

[How do I find the account's cookie (ROBLOSECURITY) and CSRF token?](https://github.com/Luckytrang2010/BrutePin#how-do-i-find-the-accounts-cookie-roblosecurity-and-csrf-token)

[Can you use this on another accounts you don't have access to?](https://github.com/Luckytrang2010/BrutePin#can-you-use-this-on-another-accounts-you-dont-have-access-to)

# Update Logs
```
[i] 10/12/2020 - added colorama to BrutePin and an option to read the cache (broken rn, answer the first issue if you want, considered beta for now)
[i] 10/13/2020 - added requirements.txt for people to install modules needed for this to run
```

# What is BrutePin?

It's a ROBLOX pin bruteforcer that tries every possible 4 digit pins in order to unlock whatever you want to do in its account. This is made by Tangly.

# Why is it asking me to get the account's cookie (temporary) and CSRF token?

This is because it would require both of those in order to get the bad boy going. CSRF token is used for preventing anyone to perform CSRF attack on a victim. CSRF is an attack where someone sends a request the web application trusts to the victim, then the victim accepts the request, and someone gets the info.

# How do I find the account's cookie (temporary) and CSRF token?

You open up inspect element, open Network tab, and try to enter in some random pin, then find the unlock request, you will see this.
![](https://media.discordapp.net/attachments/743744964500127814/764601419625267242/unknown.png?width=469&height=475)

Then look for the cookie and x-csrf-token in request headers.

![](https://media.discordapp.net/attachments/743744964500127814/764602197958197258/unknown.png?width=470&height=475)
![](https://media.discordapp.net/attachments/743744964500127814/764602356448624640/unknown.png?width=468&height=475)

Copy its contents and paste them to whatever question it's asking for.

# Can you use this on another accounts you don't have access to?

Common sense, no, you can't.

Made by Tangly <3

with help of pr0xy1337
