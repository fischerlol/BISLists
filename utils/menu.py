from utils.bis import *
from utils.sheet import *
from utils.class_strings import *


def print_menu():
    print('1. Scrape bis lists and store them locally')
    print('2. Populate sheet with local data')
    print('3. Setup sheet')
    print('Q. Quit')


def menu():
    print_menu()
    choice = str(input(': '))
    print()

    match choice:
        case '1':
            # scrape_wowhead_list(hunter)
            # scrape_wowhead_list(shaman)
            # scrape_wowhead_list(warlock)
            # scrape_wowhead_list(paladin)
            # scrape_wowhead_list(mage)
            # scrape_wowhead_list(rogue)
            # scrape_wowhead_list(druid)
            # scrape_wowhead_list(warrior)
            # scrape_wowhead_list(priest)
            # scrape_wowhead_list(death_knight)
            print()
            menu()
        case '2':
            print('\ntwo\n')
            menu()
        case '3':
            initial_setup()
            print()
            menu()
        case 'q':
            print('\nexiting program.')
            exit()
        case _:
            print('\nInvalid choice.')
            menu()
