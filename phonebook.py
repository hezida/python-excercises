import sys
import os.path

book = dict()
FILE_PATH = 'C:\\python\\MyPhonebook.txt'


def create():
    first_name = input('Enter first name: ')
    phone_number = input('Enter Phone Number: ')
    book[first_name] = phone_number
    print("Your record was successfully saved")


def read():
    name = input('Enter the name of the record you want to get: ')
    if name in book:
        phone = book[name]
        print('The phone number of {} is {}'.format(name, phone))
    else:
        print("record was not found")


def update():
    name = input('Enter the record name you want to get: ')
    if name not in book:
        print("record was not found")
        return

    phone = input('Enter the new phone number of {}: '.format(name))
    book[name] = phone


def delete():
    name = input('Enter the name of the record you want to delete: ')
    if name not in book:
        print("record was not found")
        return
    del book[name]


def leave():
    with open(FILE_PATH, 'w') as f:
        for name, phone in book.items():
            f.write('{}\t{}'.format(name, phone))
    sys.exit()


def main():
    file_exists = os.path.isfile(FILE_PATH)
    if file_exists:
        print('file exists')
        with open(FILE_PATH, 'r') as f:
            for line in f:
                name, phone = line.split('\t')
                book[name] = phone
    while True:
        print('Select one of your choice: \n'
              '-------------------------- \n'
              'c - Create a new phone record \n'
              'r - Read a phone record by name \n'
              'u - Update an existing phone record \n'
              'd - Delete an existing phone record \n')
        menu_choices = {'c': create, 'r': read, 'u': update, 'd': delete, 'q': leave}
        menu_choices[input()]()


main()
