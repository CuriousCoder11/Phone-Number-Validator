#Program to check whether a phone number is valid or not.

import phonenumbers

phone_number = phonenumbers.parse(input("Enter your phone number with country code: "))

#Validating a phone number
valid = phonenumbers.is_valid_number(phone_number)

#Checking possiblity of phone number
possible = phonenumbers.is_possible_number(phone_number)

if valid and possible == True:
    print("This is a valid and possible phone number.")
elif valid and possible == False:
    print("This is not a valid phone number.")
elif valid == True and possible == False:
    print("This number is valid but not possible.")
elif valid == False and possible == True:
    print("This number is not valid but is possible.")
else:
    print("An error occured, please try again.")