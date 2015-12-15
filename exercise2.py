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



#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Checks if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() > 0



def valid_date_format(date_string):
    """
    Checks date regex against date string, ensuring whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean; True if the format is valid, False otherwise

    """

    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True



def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes. Imports passport
    number from json file and tests passport number against regex.

    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise

    """

    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True


def valid_visa_code_format(visa_code):
    """
    Checks visa regex against visa code, ensuring visa code has two groups of five alphanumerical characters

    :param visa_code: alpha-numberic string
    :return: Boolean; True if the format is valid, False otherwise

    """

    visa_regex = re.compile(r'\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)
    if visa_match is None:
        return False
    else:
        return True


def check_visa_date(x, visa_date):
    """

    :param x:
    :param visa_date:
    :return: Boolean; True if valid, False otherwise
    """

    valid = False
    visa_formatted = valid_date_format(visa_date)
    visa_expired = is_more_than_x_years_ago(x, visa_date)
    if (visa_formatted and visa_expired) is True:
        return True
    else:
        return False

    # checks visa date validity
    # valid visa date is one that is less than two years old as per assignment instructions
    # if the visa date format is True, the visa is still valid

def check_if_valid_visa(traveler):
    """
    Checks whether the entire visa format is valid

    :param traveler: visa code & visa date
    :return: Boolean; True if valid, False otherwise
    """

    visa_code = traveler['visa']['code']
    visa_date = traveler['visa']['date']
    valid_visa_code = valid_visa_code_format(visa_code)
    visa_date_formatted = valid_date_format(visa_date)
    valid_visa_date = is_more_than_x_years_ago(2, visa_date)
    if valid_visa_code is True:
        if visa_date_formatted is True:
            if valid_visa_date is True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def check_visa(traveler, countries):
    """

    :param traveler:
    :param valid_visa_format:
    :return:
    """
    home_country = traveler['home']['country']

    if traveler['entry_reason'] == "returning":
        if home_country == "KAN":
            return True
        else:
            return False
    elif traveler['entry_reason'] == "visit":
        if countries[home_country]['visitor_visa_required'] == "0":
            return True
        elif countries[home_country]['visitor_visa_required'] == "1":
            try:
                valid = check_if_valid_visa(traveler)
                return valid
            except KeyError:
                return False
    else:
        return "Oops"



    # for a in VISA_HAVERS:
    # print valid_visa_pls(a)


def quarantine_traveler(traveler):
    """

    :param traveler:
    :param country:
    :return:
    """

    from_country = traveler['from']['country']
    if (COUNTRIES[from_country]['medical_advisory']) == "":
        return False
        try:
            via_country = traveler['via']['country']
            if COUNTRIES[via_country]['medical_advisory'] == "":
                return False
            else:
                return True
        except KeyError:
            return False
    else:
        return True


    # list where each traveler has come from
    # compare that to the corresponding entry in the list of countries for a medical advisory
    # if the medical advisory returns blank, it passes
    # if there is anything at all in the medical advisory, return that the traveler should be quarantined

def check_entry_completeness(REQUIRED_FIELDS, traveler):
    """
    Checks that traveler entry record is complete and that the date format is valid.
    :param: REQUIRED_FIELDS,traveler
    :return: Boolean; True if valid, False otherwise
    :raises: KeyError
    """
    for entry in REQUIRED_FIELDS:
        try:
            j = traveler[entry]
            if len(j) > 1:
                return True
        except KeyError:
            return True
        try:
           if valid_date_format(traveler["birth_date"]) == True:
               return True
           else:
               return False
        except KeyError:
            return False







def decide(input_file, countries_file):
    """
     Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains cases to decide
    :param countries_file: The name of a JSON formatted file that contains country data, such as whether an entry or transit visa is required, and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"

    """

    results_list = []

    # function assumes that all json files are properly formatted and will not run otherwise
    with open(input_file, 'r') as a:
        b = a.read()
        travelers = json.loads(b)
    with open(countries_file, 'r') as a:
        b = a.read()
        global COUNTRIES
        COUNTRIES = json.loads(b)

    for person in travelers:
        accept = True
        quarantine = False

        quarantine = quarantine_traveler(person)
        if quarantine is True:
            results_list.append("T")
        else:
            results_list.append("F")
    return results_list
        # check for required fields
        # check for valid passport
        # check home country / valid visa
        # check if quarantine material


testcountries = "test_jsons/countries.json"
returningcitizens = "test_jsons/test_returning_citizen.json"
incomingforners = "test_jsons/test_incoming_foreigner.json"

print decide(returningcitizens, testcountries)
print decide(incomingforners, testcountries)
