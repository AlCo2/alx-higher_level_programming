#!/usr/bin/python3
"""
 9. Student to JSON
"""


class Student:
    """
     class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if isinstance(attrs, list):
            for name in attrs:
                if name == 'first_name':
                    dic['first_name'] = self.first_name
                if name == 'age':
                    dic['age'] = self.age
                if name == 'last_name':
                    dic['last_name'] = self.last_name
        if (len(dic) > 0 and isinstance(attrs, list)):
            return dic
        return self.__dict__
