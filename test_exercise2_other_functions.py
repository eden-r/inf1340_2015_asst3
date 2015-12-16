__author__ = 'Eden Rusnell'
__email__ = 'e.rusnell@mail.utoronto.ca'
__copyright__ = '2015 Eden Rusnell'


__author__ = 'Isabelle Deluce, Jeanne Marie Alfonso, & Eden Rusnell'


# imports one per line


from exercise2 import valid_date_format, valid_passport_format, valid_visa_code_format, check_if_valid_visa



test_traveler = {
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

def test_passport_validity():
    assert valid_passport_format(test_traveler['passport']) == True