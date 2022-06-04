from collections import UserDict
from record import Record


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
