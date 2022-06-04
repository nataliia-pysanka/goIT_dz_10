"""
Module describes class Name with parameters: value
"""


class NameValidator:
    """
    Class for validating value of the Name
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value: str):
        if not isinstance(value, str) or value is None:
            raise ValueError('Name should be a string \n')

        instance.__dict__[self.name] = value

        return instance.__dict__[self.name]

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Name:
    """
    Class Name
    """
    value = NameValidator()

    def __init__(self, name):
        self.value = name

    def __str__(self):
        return self.value
