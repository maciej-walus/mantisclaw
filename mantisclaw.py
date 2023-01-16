# -*- coding: utf-8 -*-

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone


class PhoneNumber:
    def __init__(self, parsed_number):
        self.parsed_number = parsed_number


class PhoneNumberInformation:
    
    def __init__(self):
        self.phone_numbers = []
    
    def store_phone_number(self, phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                return "Invalid phone number."
            else:
                phone_number = PhoneNumber(parsed_number)
                self.phone_numbers.append(phone_number)
                
        except phonenumbers.phonenumberutil.NumberParseException as e:
            return e
        
    def information(self, phone_number):
            pn = phonenumbers.parse(phone_number)
            self.country_code = phonenumbers.region_code_for_country_code(pn.country_code)
            self.country_name = geocoder.description_for_number(pn,"en")
            self.valid = phonenumbers.is_valid_number(pn)
            self.possible = phonenumbers.is_possible_number(pn)
            self.timezone = timezone.time_zones_for_number(pn)
            self.carrier = carrier.name_for_number(pn, "pl")
            print(f"\n Phone number: {phone_number}\n Country code: {self.country_code}\n Country name: {self.country_name}\n Is valid?: {self.valid}\n Is possible?: {self.possible}\n Potential timezone: {self.timezone}\n Potential carrier: {self.carrier}")
        
        
print("\n (  `                    )           (    (                \n )\))(      )         ( /( (         )\   )\    )  (  (    \n((_)()\  ( /(   (     )\()))\  (   (((_) ((_)( /(  )\))(   \n(_()((_) )(_))  )\ ) (_))/((_) )\  )\___  _  )(_))((_)()\  \n|  \/  |((_)_  _(_/( | |_  (_)((_)((/ __|| |((_)_ _(()((_) \n| |\/| |/ _` || ' \))|  _| | |(_-< | (__ | |/ _` |\ V  V / \n|_|  |_|\__,_||_||_|  \__| |_|/__/  \___||_|\__,_| \_/\_/\n")
print("Welcome to MantisClaw. Select desired function:\n 1. Phone number OSINT\n")
function = int(input())

if function == 1:
    print ("\nPhone number OSINT selected.")
    shutdown = False
    pni = PhoneNumberInformation()
    phone_function = 0
    info_function = 0
    
    while shutdown != True:
        
        print("\nSelect desired functionality:\n 1. Inserting target phone number.\n 2. Print all the phone numbers in the table. \n 3. Print information about phone number(s). \n 4. Shutdown\n")        
        phone_function = int(input())
            
        if phone_function == 1:
            print("\nInsert the phone number including the country code in a single string")
            phone_number = input()
            pni.phone_numbers.append(phone_number)
            phone_function = -1
            
        if phone_function == 2:
            if len(pni.phone_numbers) != 0:
                print("\nPhone numbers inserted into the table:")
                for _ in range(len(pni.phone_numbers)):
                    print (pni.phone_numbers[_])
            else:
                print("\nNo phone numbers inserted into the table.")
            phone_function = -1
              
        if phone_function == 3:
            if len(pni.phone_numbers) != 0:
                print("\nProceed with all phone numbers inserted into the table?\n 1. Yes \n 2. No, let me pick a specific number.")
                info_function = int(input())
                if info_function == 1:
                    for _ in range(len(pni.phone_numbers)):
                        pni.information(pni.phone_numbers[_])
                if info_function == 2:
                    print("Insert the index of desired phone number:")
                    number = int(input())
                    pni.information(pni.phone_numbers[number])
            else:
                print("\nNo phone numbers inserted into the table.")
            phone_function = -1
            
            
        if phone_function == 4:
            shutdown = True          
        

print("\nInto the darkness I descend...")