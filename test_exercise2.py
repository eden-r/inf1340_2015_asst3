#!/usr/bin/env python3

""" Module to test papers.py  """


__author__ = 'Isabelle Deluce, Jeanne Marie Alfonso, & Eden Rusnell'

__status__ = "Prototype"

# imports one per line
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]

def test_incoming():
    """
    Foreigners entering KAN. Must check if their documents are in order and properly filled

    """

    assert decide("test_incoming_foreigner.json", "countries.json") ==\
           ['Accept', 'Reject', 'Quarantine', 'Accept']

    # test for traveling via somewhere
    assert decide("test_traveling_via.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept']

    # test checking visa validity
    assert decide("test_check_visa.json", "countries.json") ==\
        ['Accept', 'Accept', 'Quarantine']


def test_location_unknown():
    assert decide("test_location_known.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept']

def test_new_country_file():
    assert decide("test_returning_citizen.json", "countries_altered.json") ==\
        ['Quarantine', 'Accept', 'Quarantine']
    assert decide("test_incoming_foreigner.json", "countries_altered.json") ==\
        ['Quarantine', 'Quarantine', 'Quarantine', 'Accept']
    assert decide("test_traveling_via.json", "countries_altered.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Quarantine']
    assert decide("test_check_visa.json", "countries_altered.json") ==\
        ['Quarantine', 'Accept', 'Quarantine']
    assert decide("test_location_known.json", "countries_altered.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Quarantine']








