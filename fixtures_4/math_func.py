# math_func.py

import json

class StudentDB:
    def __init__(self):
        self.__data = None

    def connectData(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for student in self.__data["Student"]:
            if student["name"] == name:
                return student
        return None  # if not found
    def close(self):
      pass  
