__author__ = 'Eden Rusnell'
__email__ = 'e.rusnell@mail.utoronto.ca'
__copyright__ = '2015 Eden Rusnell'


__author__ = 'Isabelle Deluce, Jeanne Marie Alfonso, & Eden Rusnell'


# imports one per line


from exercise2 import valid_date_format, valid_passport_format, check_if_valid_visa



test_traveler1 = {
    "passport": "THISI-SAPAS-SPORT-NUMBE-RISAY",
    "first_name": "VICKI",
    "last_name": "NOYES",
    "birth_date": "1969-12-11",
    "home": {
      "city": "a",
      "region": "a",
      "country": "III"
        },
    "entry_reason": "visit",
    "visa": {
      "date": "2015-12-31",
      "code": "CFR6X-XSMVA"
        },
    "from": {
      "city": "a",
      "region": "a",
      "country": "BRD"
        }
    }

test_traveler2 = {
    "passport": "nope",
    "first_name": "VICKI",
    "last_name": "NOYES",
    "birth_date": "199-12-11",
    "home": {
      "city": "a",
      "region": "a",
      "country": "III"
        },
    "entry_reason": "visit",
    "visa": {
      "date": "2012-12-31",
      "code": "CFR6X-XSMVA"
        },
    "from": {
      "city": "a",
      "region": "a",
      "country": "BRD"
        }
    }

def test_passport_validity():
    assert valid_passport_format(test_traveler1['passport']) == True
    assert valid_passport_format(test_traveler2['passport']) == False

def test_visa_validity():
    assert check_if_valid_visa(test_traveler1) == True
    assert check_if_valid_visa(test_traveler2) == False

def test_date_validity():
    assert valid_date_format(test_traveler1['birth_date']) == True
    assert valid_date_format(test_traveler2['birth_date']) == False

