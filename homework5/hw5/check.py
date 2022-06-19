import re

class ValidCarNumber:
    def __init__(self, number):
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    def is_valid(self):
        is_val = re.search(r"0([1-9])KG([0-9]{3})([A-Z]{3})", self.__number)
        try:
            if is_val.end() == len(self.__number):
                print(f'Car number {self.__number} is valid')
            else:
                raise ValueError
        except:
            print(f'Car number {self.__number} is invalid')
