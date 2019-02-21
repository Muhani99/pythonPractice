#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:06:34 2019

@author: allen
"""

myDict = {"A":"E", "B":"F", "C":"G", "D":"H", "E":"I", "F":"J", "G":"k"
          , "H":"L", "I":"M", "j":"N", "K":"O", "L":"P", "M":"Q", "N":"R"
          , "O":"S", "P":"T", "Q":"U", "R":"V", "S":"W", "T":"X", "U":"Y"
          , "V":"Z", "W":"A", "X":"B", "Y":"C", "Z":"D", " ":".", ".":" ", "?":"*","*":"?"}
message = input("Enter the message:").upper()
encrypted = ""
for letters in message:
    if letters in myDict:
        encrypted = encrypted + myDict[letters]
    else :
        encrypted = encrypted + letters
        
print(encrypted.lower())        
