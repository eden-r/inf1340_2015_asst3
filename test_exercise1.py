#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise1 import selection, projection, cross_product


###########
# TABLES ##
###########

EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]

R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

VOTERS = [["Surname", "FirstName", "Age"],
          ["Smith", "Sammy", 17],
          ["Vasquez", "Maria", 23],
          ["Allen", "Grant", 18],
          ["Allen", "Bethany", 16],
          ["Xun", "Lu", 47],
          ["Qian", "Sima", 117]]

CANDIDATES = [["Candidate", "Party"],
              ["Justin Trudeau", "Liberal"],
              ["Stephen Harper", "Conservative"],
              ["Tom Mulcair", "NDP"]]


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


def filter_eligible_voters(row):
    return row[-1] >= 18


###################
# TEST FUNCTIONS ##
###################

def test_selection():
    """
    Test select operation.
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Verdi", "Nico", 36, 4500],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees))


def test_projection():
    """
    Test projection operation.
    """

    result = [["Surname", "FirstName"],
              ["Smith", "Mary"],
              ["Black", "Lucy"],
              ["Verdi", "Nico"],
              ["Smith", "Mark"]]

    assert is_equal(result, projection(EMPLOYEES, ["Surname", "FirstName"]))


def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Employee", "Department", "Department", "Head"],
              ["Smith", "sales", "production", "Mori"],
              ["Smith", "sales", "sales", "Brown"],
              ["Black", "production", "production", "Mori"],
              ["Black", "production", "sales", "Brown"],
              ["White", "production", "production", "Mori"],
              ["White", "production", "sales", "Brown"]]

    assert is_equal(result, cross_product(R1, R2))



##################
# OUR TEST CASES #
##################

def test_selection_by_team():
    result = [["Surname", "FirstName", "Age"],
          ["Vasquez", "Maria", 23],
          ["Allen", "Grant", 18],
          ["Xun", "Lu", 47],
          ["Qian", "Sima", 117]]

    assert is_equal(result, selection(VOTERS, filter_eligible_voters))

def test_project_by_team():
    result = [["Surname", "Age"],
          ["Smith", 17],
          ["Vasquez", 23],
          ["Allen", 18],
          ["Allen", 16],
          ["Xun", 47],
          ["Qian", 117]]

    assert is_equal(result, projection(VOTERS, ["Surname", "Age"]))

def test_cross_product_by_team():
    result = [["Surname", "FirstName", "Age", "Candidate", "Party"],
            ["Smith", "Sammy", 17, "Justin Trudeau", "Liberal"],
            ["Smith", "Sammy", 17, "Stephen Harper", "Conservative"],
            ["Smith", "Sammy", 17, "Tom Mulcair", "NDP"],
            ["Vasquez", "Maria", 23, "Justin Trudeau", "Liberal"],
            ["Vasquez", "Maria", 23, "Stephen Harper", "Conservative"],
            ["Vasquez", "Maria", 23, "Tom Mulcair", "NDP"],
            ["Allen", "Grant", 18,"Justin Trudeau", "Liberal"],
            ["Allen", "Grant", 18, "Stephen Harper", "Conservative"],
            ["Allen", "Grant", 18, "Tom Mulcair", "NDP"],
            ["Allen", "Bethany", 16, "Justin Trudeau", "Liberal"],
            ["Allen", "Bethany", 16, "Stephen Harper", "Conservative"],
            ["Allen", "Bethany", 16, "Tom Mulcair", "NDP"],
            ["Xun", "Lu", 47, "Justin Trudeau", "Liberal"],
            ["Xun", "Lu", 47, "Stephen Harper", "Conservative"],
            ["Xun", "Lu", 47, "Tom Mulcair", "NDP"],
            ["Qian", "Sima", 117, "Justin Trudeau", "Liberal"],
            ["Qian", "Sima", 117, "Stephen Harper", "Conservative"],
            ["Qian", "Sima", 117, "Tom Mulcair", "NDP"]]

    assert is_equal(result, cross_product(VOTERS, CANDIDATES))


def test_selection_returns_nothing():
    t = [["Name", "Age"],
         ["Bob", 47],
         ["Mary", 65],
         ["Carla", 54]]

    def f(r):
        return r[-1] < 35

    assert selection(t,f) == None

def test_projection_returns_error():
    try:
        projection(VOTERS, ["Age", "Riding"])
    except AttributeError:
        assert True