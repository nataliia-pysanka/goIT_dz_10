from collections import UserDict, UserList
import re


class Field:
    pass


class NameValidator:
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
    value = NameValidator()

    def __init__(self, name):
        self.value = name

    def __str__(self):
        return self.value


class PhoneValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value: str):
        if not isinstance(value, str):
            raise ValueError('Number should be a string \n')
        if not value:
            instance.__dict__[self.name] = None
            return instance.__dict__[self.name]

        search_symb = re.search('\D', value)
        if 10 <= len(value) <= 15 and search_symb is None:
            instance.__dict__[self.name] = value

        return instance.__dict__[self.name]

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)


class Phone:
    value = PhoneValidator()

    def __init__(self, number=None):
        self.value = number

    def __str__(self):
        return self.value


class Record:
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

    def check_number(self, new_number):
        for number in self.numbers:
            if number.value == new_number:
                return True
        return False

    def append_number(self, number: str):
        if not self.check_number(number):
            print(f'The number {number} already exist \n')
            return False
        try:
            new_number = Phone(number)
        except ValueError as err:
            print(err)
            return False
        self.numbers.append(new_number)
        print(f'The number {new_number} was added \n')
        return True

    def edit_number(self, edit_number: str, new_number: str):
        for number in self.numbers:
            if number.value == edit_number:
                number.value = new_number
                print('The number was changed \n')
                return True
        return False

    def delete_number(self, del_number: str):
        index = 0
        for number in self.numbers:
            if number.value == del_number:
                self.numbers.pop(index)
                print('The number was deleted \n')
                return True
            index += 1
        return False


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, rec: Record):
        key = rec.name.value
        self[key] = rec

    def __str__(self):
        res = ''
        for key in self.data:
            res += f'{key}\n'
            for number in self[key].numbers:
                res += f'\t{number}\n'
        return res


class User:
    def __init__(self, name, surname, adress_book: AddressBook):
        self.name = name
        self.surname = surname
        self.adress_book = adress_book


user_phone = Phone('08854544422')
print(user_phone)
user_name = Name('Nataliia')
print(user_name)
user_rec = Record(user_name, user_phone)
print(user_rec)
user_rec.append_number('0549127473')
user_rec.append_number(549127473)
print(user_rec)
user_rec.delete_number('0669176473')
print(user_rec)

my_book = AddressBook()
my_book.add_record(user_rec)
print(my_book)
my_book.add_record(Record(Name('Maks'), Phone('0998765432')))
print(my_book)
user_rec.edit_number('0669127473', '0669127472')
print(my_book)
