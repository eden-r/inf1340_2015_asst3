#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None


"""
importing and making json files readable
"""
# open json file(s)
# stylize them so they print readably
# name the different parts so the different functions can access them?

with open("test_jsons/test_returning_citizen.json", "r") as file_reader:
    file_contents = file_reader.read()
    json_citizens = json.loads(file_contents)
with open("test_jsons/countries.json", "r") as file_reader2:
    file_contents2 = file_reader2.read()
    json_countries = json.loads(file_contents2)

#print json.dumps(json_citizens, indent=1)
#print json.dumps(json_countries, indent=1)

VISA_HAVERS = [
  {
    "passport": "JMZ0S-89IA9-OTCLY-MQILJ-P7CTY",
    "first_name": "ELIZABETH",
    "last_name": "WENDT",
    "birth_date": "1958-08-22",
    "home": {
      "city": "Bala",
      "region": "ON",
      "country": "BRD"
    },
    "entry_reason": "returning",
    "from": {
      "city": "Weasel",
      "region": "Rodent",
      "country": "BRD"
    },
    "visa": {
        "code": "JMZ0S-89IA9-OTCLY-MQILJ-P7CTY",
        "date": "2015-11-11"
    }
  }
]



#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() > 0


"""
FUNCTIONS TO BE WRITTEN
"""


def decide(input_file, countries_file):
    citizen_no = 0
    valid = False
    for citizen in json_citizens:
        passport_validity = valid_passport_format(citizen['passport'])
        if passport_validity is True:
            print("valid")
        else:
            print("False")
        date_validity = valid_date_format(citizen['birth_date'])
        if date_validity is True:
            print("valid")
        else:
            print("False")




    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """




def valid_passport_format(passport_number):
    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True
    # delineates valid regex for passport numbers
    # imports passport number from json file
    # tests passport number against regex
    # returns True is passport is valid
    # returns False if passport is not valid
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """

#print valid_passport_format("wwwww-wwwww-wwwww-wwwww-wwwww")
#print valid_passport_format("wwww-wwww-wwww-wwww-wwww")

def valid_visa_code_format(visa_code):
    visa_regex = re.compile(r'\w{5}-\w{5}-\w{5}-\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)
    if visa_match is None:
        return False
    else:
        return True

    # visa has two fields: date (YYYY-MM-DD) and code (five groups of five alphanumeric characters
    # check visa regex against visa code
    # returns false if not found, returns True if found
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """

def valid_date_format(date_string):
    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True
    # checks date regex against date string
    # returns false if not found, returns True if found
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

def valid_visa_pls(traveler):
    valid = False
    visa_code = traveler['visa']['code']
    visa_date = traveler['visa']['date']
    valid_visa_code = valid_visa_code_format(visa_code)
    valid_visa_date = check_visa_date(2, visa_date)
    if (valid_visa_code and valid_visa_date) is True:
        valid = True
    else:
        valid = False
    return valid



def check_visa_date(x, visa_date):
    valid = False
    visa_formatted = valid_date_format(visa_date)
    visa_expired = is_more_than_x_years_ago(x, visa_date)
    if (visa_formatted and visa_expired) is True:
        return True
    else:
        return False


    """
    Checks whether the entire visa format is valid
    input: the date (date_string) and visa code (visa_code) of visitor's visa
    :param valid_date_format(), valid_visa_format(), is_more_than_x_years_ago()
    :return: Boolean; True if format is valid, False otherwise
    """

for a in VISA_HAVERS:
    print valid_visa_pls(a)




#def check_visa(traveler, valid_visa_format):
#    if traveler['home']['country'] == "KAN":
#        return True
#    else:



def quarantine_traveler(traveler, country):
    for a in json_citizens:
        b = a['from']['country']
        if (json_countries[b]['medical_advisory']) == "":
            print("None")
        else:
            print("Quarantine")
    # list where each traveler has come from
    # compare that to the corresponding entry in the list of countries for a medical advisory
    # if the medical advisory returns blank, it passes
    # the there is anything at all in the medical advisory, return that the traveler should be quarantined

#print quarantine_traveler(json_citizens, json_countries)

#decide(json_citizens, json_countries)
#print json.dumps(json_countries, indent=1)



