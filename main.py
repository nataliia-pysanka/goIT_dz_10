"""
Main module
"""
from address_book import AddressBook
from phone import Phone
from name import Name
from record import Record


if __name__ == '__main__':
    user_phone = Phone('08854544422')
    user_name = Name('Nataliia')
    user_rec = Record(user_name, user_phone)
    print(user_rec)

    user_rec.edit_number(user_phone, '04456544423')
    print(user_rec)

    user_rec.append_number('0549127473')
    user_rec.append_number(549127473)
    user_rec.append_number(Phone('0549127473'))

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
