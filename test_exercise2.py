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

    assert decide("test_incoming_foreigner.json", "countries_altered.json") ==\
        ['Quarantine', 'Quarantine', 'Quarantine', 'Accept']


def test_traveling_via():
    """
    Test incoming foreigners & returning citizens traveling via somewher else

    """
    assert decide("test_traveling_via.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept', 'Reject']

    assert decide("test_traveling_via.json", "countries_altered.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept', 'Quarantine']

def test_visa_validity():
    """
    Test validity & formatting of incoming travelers from countries that require visas

    """
    assert decide("test_check_visa.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Reject']

    assert decide("test_check_visa.json", "countries_altered.json") ==\
        ['Quarantine', 'Accept', 'Quarantine', 'Reject']


def test_location_unknown():
    """
    Test that an unknown location returns Reject (or Quarantine) rather than crashing the program

    """
    assert decide("test_location_known.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept']

    assert decide("test_location_known.json", "countries_altered.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Quarantine']


def test_new_country_file():
    # test for changes to the country file
    assert decide("test_returning_citizen.json", "countries_altered.json") ==\
        ['Quarantine', 'Accept', 'Quarantine']

def test_missing_entries():
    #tests for missing entries in traveller information
    assert decide("test_missing_entries,json", "countries.json") ==\
    ['Reject', 'Reject', 'Reject', 'Reject', 'Reject']


def test_reject_and_quarantine():
    #test reject and quarantine
    assert decide("test_jsons/test_reject.json", "test_jsons/countries.json") ==\
        ['Reject', 'Reject', 'Reject', 'Reject', 'Quarantine', 'Quarantine']














