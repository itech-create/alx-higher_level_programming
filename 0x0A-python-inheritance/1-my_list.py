#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """Subclass of list that adds a print_sorted() method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
