#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


#####################
# HELPER FUNCTIONS ##
#####################

def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):
    # takes the header for t
    # applies f to each row in t
    # takes the f(row) that returns true and attaches that to a new table
    # returns the new table
    # if f(row) does not return True, does not return a table / returns None?
    """
    Perform select operation on table t that satisfy condition f.

    param: t (table 1/a list of lists), function (operates on data rows of t1)
    raises:
    output: table that contains rows that meet criteria of function
    assumptions: the output of the function that is being passed in is a Boolean (T/F)

    Example:
    R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    # Define function f that returns True if the last element in the row is greater than 3.
    def f(row): row[-1] > 3
    select(R, f)
    [["A", "B", "C"], [4, 5, 6]]

    """

    return []


def projection(t, r):
    # for each element entered into list r
    # searches the hearder of t
    # finds all values in that index of t[0][r[0]], etc
    # adds them to a new table
    """
    Perform projection operation on table t
    using the attributes subset r.

    param: t (table1/a list of lists), r (the attributes subset/a list)
    raises: TypeError
    output: table (list of lists) containing all values under the heading of attributes subset
    assumptions:

    Example:
    R = [["A", "B", "C"], [1, 2, 3], [4, 5, 6]]
    projection(R, ["A", "C"])
    [["A", "C"], [1, 3], [4, 6]]
    
    """

    return []


def cross_product(t1, t2):
    # takes the header of t1 and attaches it to the header of t2
    # for each row in t1, appends each row of t2 to the end
    # returns a new table

    """
    Return the cross-product of tables t1 and t2.

    param: t1 (table1/a list of lists), t2 (table2/a list of lists)
    raises:
    output: table (list of lists) that combines every row of first table (t1) with every row of second table (t2)


    Example:
    > R1 = [["A", "B"], [1,2], [3,4]]
    > R2 = [["C", "D"], [5,6]]
    [["A", "B", "C", "D"], [1, 2, 5, 6], [3, 4, 5, 6]]
    if reversed:
    R2 = [["C", "D"], [5,6]]
    R1 = [["A", "B"], [1,2], [3,4]]
    [["C", "D", "A", B"], [5, 6, 1, 2], [5, 6, 3, 4]]


    """

    return []

