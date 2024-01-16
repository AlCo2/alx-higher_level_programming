#!/usr/bin/python3
""" file that represant a base class"""
import json


class Base:
    """
    base class that will be the base of all other
    classes in this projcet
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        turn object to json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to a file json
        """
        with open("{}".format(cls.__name__ + ".json"), 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        read from json file
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create method
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        load from a file
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to a file as csv
        """
        filename = str(cls.__name__) + ".csv"
        with open(filename, 'w') as f:
            for rect in list_objs:
                if cls.__name__ == 'Rectangle':
                    f.write(f"{rect.id}, {rect.width},
                            {rect.height}, {rect.x}, {rect.y}\n")
                else:
                    f.write(f"{rect.id}, {rect.size}, {rect.x}, {rect.y}\n")

    @classmethod
    def load_from_file_csv(cls):
        """
        read from a csv file
        """
        filename = str(cls.__name__) + ".csv"
        list = []
        with open(filename, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                temp = [int(i) for i in line.split(',')]
                if cls.__name__ == 'Rectangle':
                    list.append(cls(id=temp[0], width=temp[1],
                                    height=temp[2], x=temp[3], y=temp[4]))
                else:
                    list.append(cls(id=temp[0],
                                    size=temp[1], x=temp[2], y=temp[3]))
        return list
