import csv
from ast import literal_eval

phonebook = {}
# phonebook = {'Chris': {'name': 'Chris', 'number': '5032779710', 'phrase': 'teach'},
#              'Remington': {'name': 'Remington', 'number': '5412813629', 'phrase': 'assist'},
#              'Donald': {'name': 'Donald', 'number': '3602711329', 'phrase': 'mrpaul'},
#              'Rodney': {'name': 'Rodney', 'number': '5033882824', 'phrase': 'make it so'},
#              'Tony': {'name': 'Tony', 'number': '5034536573', 'phrase': 'Winner'},
#              'Lynde': {'name': 'Lynde', 'number': '5033199118', 'phrase': 'last one in kindergarden'},
#              'Nathan': {'name': 'Nathan', 'number': '2532980835', 'phrase': 'Washington'},
#              'John': {'name': 'John', 'number': '9712958823', 'phrase': 'Who rang'},
#              'Sage': {'name': 'Sage', 'number': '5037582046', 'phrase': 'knows things'}}


def save_phonebook():
    while True:
        verify = input('Warning, this will delete the existing phonebook, continue? (y/n): ')
        if verify == 'y':
            w = csv.writer(open('.\phonebook.csv', 'w'))
            for key, val in phonebook.items():
                w.writerow([key, val])
                w.close()
            break
        elif verify == 'n':
            print('did not delete phonebook')
            break


def load_phonebook():
    while True:
        verify = input('Would you like to append the phonebook with the current contacts? (y/n): ')
        if verify == 'y':
            with open('.\phonebook.csv') as csvfile:
                spamreader = csv.reader(csvfile)
                for row in spamreader:
                    phonebook[row[0]] = literal_eval(row[1])

            break
        elif verify == 'n':
            print('did not load phonebook from file')
            break




def check_exists(name_phone_or_phrase):
    try:
        if phonebook[name_phone_or_phrase]:
            exists = True
        else:
            for key, value in phonebook.items():
                for key2, value2 in value.items():
                    if value2 == name_phone_or_phrase:
                        exists = True
    except KeyError:
        exists = False
    return exists


def create_new_contact():
    print("Creating new contact")
    active = True
    while active:

        while True:
            contact_name = input("Enter contact name: ")
            if not check_exists(contact_name):
                break
            print("name already exists, please choose another.")

        while True:
            contact_num = input("Enter contact phone number: ")
            if not check_exists(contact_num):
                break
            print("phone already exists, please choose another.")

        while True:
            contact_phrase = input("Enter contact phrase: ")
            if not check_exists(contact_phrase):
                break
            print("phrase already exists, please choose another.")

        print('Entering {}'.format(contact_name))
        print('with phone number {}'.format(contact_num))
        print('and phrase: {}'.format(contact_phrase))

        validate = ''
        while validate != 'y' and validate != 'n':
            validate = input('Does everything look correct? (y/n)')

        if validate == 'y':
            print('saving')
            phonebook[contact_name] = {'name': contact_name, 'number': contact_num, 'phrase': contact_phrase}
            active = False

        elif validate == 'n':
            continue


def retrieve_contact():
    print('Search')
    query = input('Retrieve pattern: ')
    query_results = []
    for key, value in phonebook.items():
        for key2, value2, in value.items():
            if value2.find(query, 0, len(value2)) > -1:
                query_results.append(value)

    if query_results == []:
        print('No results')
    print(query_results)


def update_contact():
    print('Update a contact')

    while True:
        user_in = input('What contact would you like to update? ')
        if user_in in phonebook:
            break
        print('Not in contacts')
    to_edit = phonebook[user_in]
    print("editing contact:" + str(to_edit))
    active = True
    while active:
        to_update = input('What would you like to edit? (name/number/phrase)')
        if to_update == 'name':
            new_name = input('Enter new name for {}'.format(phonebook[user_in]['name']))
            number = phonebook[user_in]['number']
            phrase = phonebook[user_in]['phrase']
            del phonebook[user_in]
            phonebook[new_name] = {'name': new_name, 'number': number, 'phrase': phrase}
            active = False
        elif to_update == 'number':
            new_number = input('Enter new number for {} '.format(phonebook[user_in]['name']))
            phonebook[user_in]['number'] = new_number
            active = False
        elif to_update == 'phrase':
            new_phrase = input('Enter new phrase for {} '.format(phonebook[user_in]['name']))
            phonebook[user_in]['phrase'] = new_phrase
            active = False

    print('Contact has been updated')


def delete_contact():
    print('Delete a contact')
    active = True
    while active:
        user_in = input('What contact would you like to delete? ')
        if user_in in phonebook:
            del phonebook[user_in]
            active = False
        print('Not a contact, please enter an existing contact')
    print('contact {} deleted'.format(user_in))


def prompt():
    active = True
    print("Enter 'q' to quit")
    while active:

        user_in = input(
            'You can (C)reate a new contact, (R)etrieve a contact, (U)pdate and existing contact, (D)elete a contact, (S)ave the phonebook to file, (L)oad the phonebook from file: ')
        if user_in == 'C':
            create_new_contact()
        elif user_in == 'R':
            retrieve_contact()
        elif user_in == 'U':
            update_contact()
        elif user_in == 'D':
            delete_contact()
        elif user_in == 'S':
            save_phonebook()
        elif user_in == 'L':
            load_phonebook()
        elif user_in == 'q':
            active = False
            exit()
        else:
            print('invalid response, try again.')


prompt()
