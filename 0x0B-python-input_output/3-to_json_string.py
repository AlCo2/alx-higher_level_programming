#!/usr/bin/python3
"""
    To Json String
"""


import json


def to_json_string(my_obj):
    """
        function that appends a string at the end of a text file
        (UTF8)
        and returns the number of characters added
    """

    return json.dumps(my_obj)
