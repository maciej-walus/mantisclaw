# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:42:32 2023

@author: Maciook
"""

from bs4 import BeautifulSoup
import phonenumbers
import ipwhois

print("\n (  `                    )           (    (                \n )\))(      )         ( /( (         )\   )\    )  (  (    \n((_)()\  ( /(   (     )\()))\  (   (((_) ((_)( /(  )\))(   \n(_()((_) )(_))  )\ ) (_))/((_) )\  )\___  _  )(_))((_)()\  \n|  \/  |((_)_  _(_/( | |_  (_)((_)((/ __|| |((_)_ _(()((_) \n| |\/| |/ _` || ' \))|  _| | |(_-< | (__ | |/ _` |\ V  V / \n|_|  |_|\__,_||_||_|  \__| |_|/__/  \___||_|\__,_| \_/\_/\n")
print("Welcome to MantisClaw. Select desired function:\n 1. Phone number OSINT\n")
function = int(input())

if function == 1:
    print ("\nPhone number OSINT selected.")
    shutdown = False
    while shutdown != True:
        
        print("\nSelect desired functionality:\n 1. Inserting target phone number.\n 2. Shutdown\n")
        function = int(input())
        
        if function == 1:
            pass
        
        if function == 2:
            function = -1
            shutdown = True;
            print("\nIn the darkness I descend...")

