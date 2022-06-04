"""
Module describes class Phone with parameters: value
"""
from re import search as re_search


class PhoneValidator:
    """
    Class for validating value of Phone
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError('Number should be a string \n')
        if not value:
            instance.__dict__[self.name] = None
            return instance.__dict__[self.name]

        if 10 <= len(value) <= 15 and re_search('\D', value) is None:
            instance.__dict__[self.name] = value
            return instance.__dict__[self.name]
        raise ValueError('\t Length of number should be 10-15 symbols')

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Phone:
    """
    Class Phone
    """
    value = PhoneValidator()

    def __init__(self, number=None):
        try:
            self.value = number
        except ValueError as err:
            print(err)
            self.value = None

    def __str__(self):
        return self.value

    def edit(self, new_value: str):
        """
        Function for editing value of Phone
        :param new_value: str
        :return: boolean
        """
        try:
            self.value = new_value
        except ValueError as err:
            print(err)
            return False
        return True
