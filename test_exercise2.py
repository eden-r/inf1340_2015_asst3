#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

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


def test_reject():
    """
    Should reject all (returning citizens, incoming foreigners, people travlling via KAN)
    :return:
    """


def test_traveling_via():
    assert decide("test_traveling_via.json", "countries.json") ==\
        ['Reject', 'Accept', 'Quarantine', 'Accept']

def test_location_unknown():
    assert decide("test_location_known.json", "countries.json") ==\
        ['Reject', 'Accept', 'Reject', 'Accept']
#def test_location_known():
# traveling travelling

def test_reject_and_quarantine():
    assert decide("test_jsons/test_reject.json", "test_jsons/countries.json") ==\
        ['Reject', 'Reject', 'Reject', 'Reject', 'Quarantine', 'Quarantine']
