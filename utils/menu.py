from utils.bis import *


def print_menu():
    print('1. Scrape bis lists and store them')
    print('2. Check for bis list updates')
    print('3. Setup and populate sheet')
    print('Q. Quit')


def menu():
    print_menu()
    choice = str(input(': '))
    print()

    match choice:
        case '1':
            #scrape_wowhead_list(hunter)
            #scrape_wowhead_list(shaman)
            scrape_wowhead_list(warlock)
            menu()
        case '2':
            print('\ntwo\n')
            menu()
        case '3':
            print('\nthree\n')
            menu()
        case 'q':
            print('\nexiting program.')
            exit()
        case _:
            print('\nInvalid choice.')
            menu()
