#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = 'Isabelle Deluce, Jeanne Marie Alfonso, & Eden Rusnell'


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


##########################
## supporting functions ##
##########################

def valid_date_format(date_string):
    # function for checking date string formats

    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True



def valid_passport_format(passport_number):
    # function for checking passport number formats

    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True


def valid_visa_code_format(visa_code):
    # function for checking visa code formats

    visa_regex = re.compile(r'\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)
    if visa_match is None:
        return False
    else:
        return True





def check_if_valid_visa(traveler):
    # function for checking if a traveler's visa is valid

    visa_to_check = traveler['visa']
    if valid_visa_code_format(visa_to_check['code']) is True:
        if valid_date_format(visa_to_check['date']) is True:
            if is_more_than_x_years_ago(2, visa_to_check['date']) is True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False




def check_visa(traveler):
    # function for checking whether or not the traveler NEEDS a visa

    home_country = traveler['home']['country']

    if traveler['entry_reason'] == "returning":
        if home_country == "KAN":
            return True
        else:
            return False
    elif traveler['entry_reason'] == "visit":
        try:
            if COUNTRIES[home_country]['visitor_visa_required'] == "0":
                return True
            elif COUNTRIES[home_country]['visitor_visa_required'] == "1":
                try:
                    valid = check_if_valid_visa(traveler)
                    return valid
                except KeyError:
                    return False
        except KeyError:
            return False
    else:
        return False





def check_location_is_known(traveler):
    # function for checking if the traveler is coming from a real location

    home_location = traveler['home']['country']
    home_location = home_location.upper()
    from_location = traveler['from']['country']
    from_location = from_location.upper()

    if from_location not in COUNTRIES:
        if home_location != "KAN":
            if home_location not in COUNTRIES:
                return False
    else:
        return True


def check_entry_completeness(traveler):
    # function for checking that all required fields are present

    complete = False
    for entry in REQUIRED_FIELDS:
        try:
            j = traveler[entry]
            if len(j) > 1:
                complete = True
            try:
                if valid_date_format(traveler["birth_date"]) is True:
                    if check_location_is_known(traveler) is True:
                        complete = True
                    else:
                        return  False
                else:
                    return False
            except KeyError:
                return False
        except KeyError:
            return False
    return complete






def quarantine_traveler(traveler):
    # function for checking if there is a medical advisory for the country the trvaler is coming from/via

    try:
        from_country = traveler['from']['country']
        from_country = from_country.upper()
        if (COUNTRIES[from_country]['medical_advisory']) == "":
            try:
                via_country = traveler['via']['country']
                via_country = via_country.upper()
                if COUNTRIES[via_country]['medical_advisory'] == "":
                    return False
                else:
                    return True
            except KeyError:
                return False
        else:
            return True
    except KeyError:
        return False



###################
## MAIN FUNCTION ##
###################

def decide(input_file, countries_file):
    # Decides whether a traveller's entry into Kanadia should be accepted
    # function assumes that all json files are properly formatted and will not run otherwise

    results_list = []

    # making JSON entries readable
    with open(input_file, 'r') as a:
        b = a.read()
        travelers = json.loads(b)
    with open(countries_file, 'r') as a:
        b = a.read()
        global COUNTRIES
        COUNTRIES = json.loads(b)


    # run all the functions by iterating through the input list
    for person in travelers:
        accept = True
        quarantine = False
        accept = check_entry_completeness(person)
        if accept is True:
            accept = valid_passport_format(person['passport'])
            if accept is True:
                accept = check_visa(person)
        quarantine = quarantine_traveler(person)

        # return according to the priority ranking 1) Quarantine 2) Reject 3) Accept
        if (quarantine is True) and (accept is True):
            results_list.append("Quarantine")
        elif (quarantine is True) and (accept is False):
            results_list.append("Quarantine")
        elif (quarantine is False) and (accept is False):
            results_list.append("Reject")
        elif (quarantine is False) and (accept is True):
            results_list.append("Accept")

    return results_list



# TESTING THE CODE

#"""
test1 = "test_jsons/test_returning_citizen.json"
test2 = "test_jsons/test_incoming_foreigner.json"
test3 = "test_jsons/test_traveling_via.json"
test4 = "test_jsons/test_location_known.json"
test5 = "test_jsons/test_check_visa.json"
count1 = "test_jsons/countries.json"
count2 = "test_jsons/countries_altered.json"


print decide(test1, count1)
print decide(test2, count1)
print decide(test3, count1)
print decide(test4, count1)
print decide(test5, count1)
print decide(test1, count2)
print decide(test2, count2)
print decide(test3, count2)
print decide(test4, count2)
print decide(test5, count2)

#"""
