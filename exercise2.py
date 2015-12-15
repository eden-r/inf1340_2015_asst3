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
importing and making json files readable, naming different parts so that different functions can access them
"""

"""
with open("test_json/test_returning_citizen.json", "r") as file_reader:
    file_contents = file_reader.read()
    json_citizens = json.loads(file_contents)

with open("countries.json", "r") as file_reader2:
    file_contents2 = file_reader2.read()
    json_countries = json.loads(file_contents2)
"""

#print json.dumps(json_citizens, indent=1)
#print json.dumps(json_countries, indent=1)





"""
WRITING TO JSON FILES

# to overwrite the existing "test_incoming_foreigner.json" file:

with open(incoming_foreigners, "w") as output:
    json.dump(VISA_HAVERS, output, sort_keys=True, indent=1)

with open(incoming_foreigners[0], mode='w') as feeds:
    for item in VISA_HAVERS:
        json.dump(item, feeds, sort_keys=True, indent=1)
"""

#####################
# HELPER FUNCTIONS ##
#####################

def is_more_than_x_years_ago(x, date_string):
    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() > 0

def valid_date_format(date_string):
    date_regex = re.compile(r'\d\d\d\d-\d\d-\d\d')
    date_match = date_regex.search(date_string)
    if date_match is None:
        return False
    else:
        return True


#### PASSPORT RELATED

def valid_passport_format(passport_number):
    passport_regex = re.compile(r'(\w{5}-){4}\w{5}')
    passport_match = passport_regex.search(passport_number)
    if passport_match is None:
        return False
    else:
        return True


#### VISA RELATED

def check_visa_code(visa_code):
    visa_regex = re.compile(r'\w{5}-\w{5}')
    visa_match = visa_regex.search(visa_code)

    if visa_match is None:
        return False
    else:
        return True


def check_visa_date(x, visa_date):
    valid = False
    visa_formatted = valid_date_format(visa_date)
    visa_expired = is_more_than_x_years_ago(x, visa_date)
    if (visa_formatted and visa_expired) is True:
        return True
    else:
        return False

def check_visa(traveler):
    valid = False
    visa_code = traveler['visa']['code']
    visa_date = traveler['visa']['date']
    valid_visa_code = check_visa_code(visa_code)
    valid_visa_date = check_visa_date(2, visa_date)
    if (valid_visa_code and valid_visa_date) is True:
        valid = True
    else:
        valid = False
    return valid


#### QUARENTINE RELATED
def quarantine_traveler(traveler, countries):
    quarantine = False
    b = traveler['from']['country']
    if (countries[b]['medical_advisory']) == "":
        quarantine = False
    else:
        quarantine = True
    return quarantine


def decide(input_file, countries_file):
    results_list = []

    # opening json files
    # assumption: all input files will be properly-formatted (i.e. no errors) json files
    with open(input_file, 'r') as a:
        b = a.read()
        input_contents = json.loads(b)
    with open(countries_file, 'r') as a:
        b = a.read()
        countries = json.loads(b)

    for citizen in input_contents:
        # check for required fields
        for element in REQUIRED_FIELDS:
            try:
                citelement = citizen[element]
                valid = True
            except KeyError:
                valid = False

        # name some vaiables to make things simpler
        from_country = citizen['from']['country']
        reason = citizen['entry_reason']
        home_country = citizen['home']['country']

        # check for visa
        if valid is True:
            if reason == "visit":
                if (countries[from_country]['visitor_visa_required']) == "1":
                    valid = check_visa(citizen)
            elif reason == "returning":
                if home_country == "KAN":
                    valid = True
                else:
                    valid = False

            # check for passport
            if valid is True:
                valid = valid_passport_format(citizen['passport'])
            else:
                valid = False

        # check if the traveler needs to be quarantined
        quarantine = quarantine_traveler(citizen, countries)
        if (quarantine is True) and (valid is True):
            results_list.append("Quarantine")
        elif (quarantine is True) and (valid is False):
            results_list.append("Quarantine")
        elif (quarantine is False) and (valid is True):
            results_list.append("Accept")
        elif (quarantine is False) and (valid is False):
            results_list.append("Reject")

    return results_list


testcountries = "test_jsons/countries.json"
returningcitizens = "test_jsons/test_returning_citizen.json"
incomingforners = "test_jsons/test_incoming_foreigner.json"

print decide(incomingforners, testcountries)
print decide(returningcitizens, testcountries)

