"""
Module describes class Record with next parameters: name, list of phones
"""
from name import Name
from phone import Phone


class Record:
    """
    Class for instance Record
    """
    def __init__(self, name: Name, phone: Phone = None):
        self.numbers = []
        self.name = name
        if phone:
            self.numbers.append(phone)

    def __str__(self):
        rec = '{:<6} : {:<15}'.format('Name', self.name.value) + '\n'
        for number in self.numbers:
            rec += '{:<6} : {:<15}'.format('Number', number.value) + '\n'
        return rec

    def append_number(self, number: Phone):
        """
        Function append new Phone object to the list of phones
        """
        print('Adding a new number...')
        if not isinstance(number, Phone):
            print('\t It should be a Phone object')
            print("Can't add this number \n")
            return False

        if number in self.numbers:
            print(f'\t The number {number} already exist \n')
            return False

        self.numbers.append(number)
        print(f'\t The number {number} was added \n')
        return True

    def edit_number(self, edit_number: Phone, new_number: str):
        """
        Function edit Phone object
        """
        print(f'Editing {edit_number}...')
        if not isinstance(edit_number, Phone):
            print('\t It should be a Phone object')
            print("Can't edit this number \n")
            return False
        if edit_number.edit(new_number):
            print(f'\t Number {edit_number} was changed \n')
            return True
        print(f"\t Number {edit_number} wasn't changed \n")
        return True

    def delete_number(self, del_number: Phone):
        """
        Function delete Phone object from the list of phones
        """
        print(f'Deleting {del_number}...')
        if not isinstance(del_number, Phone):
            print('\t It should be a Phone object')
            print("Can't delete this number \n")
            return False
        if del_number in self.numbers:
            index = self.numbers.index(del_number)
            self.numbers.pop(index)
            print(f'\t The number {del_number} was deleted \n')
            return True
        print(f'\t No number {del_number} in the book')
        return False
