import os
from utils.class_specs import *
from utils.class_strings import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def check_local():
    check_local.is_same = True


def compare_lists(list_1, file):
    check_local()
    list_two = []

    with open('local/' + str(file), 'r') as file:
        for line in file:
            stripped_line = line.strip()
            list_two.append(stripped_line)

    illegal_chars = ['[', ']', '\\', "'", '"']
    list_one = ''.join(str(list_1))
    list_two = ''.join(str(list_two))
    for characters in illegal_chars:
        list_one = list_one.replace(characters, '')
        list_two = list_two.replace(characters, '')

    if len(list_one) != len(list_two):
        check_local.is_same = False
    file.close()


def create_empty_file(file):
    file_name = str(file)
    path = 'local/' + str(file)

    file_exists = os.path.exists(path)
    if file_exists is False:
        file = open('local/' + str(file), 'w')
        print(file_name.capitalize(), 'does not exist, Creating now...', end='')
        print('[Done!]')
        file.close()


def create_file(player_spec, gear_list):
    illegal_chars = ['[', ']']
    list_x = ''.join(str(gear_list))
    for characters in illegal_chars:
        list_x = list_x.replace(characters, '')
    with open('local/' + str(player_spec), 'w') as file:
        file.write(list_x)
    file.close()


def get_list(player_spec, file):
    check_local()
    epic_list, blue_list, wowhead_list = [], [], []
    session = HTMLSession()
    spec = session.get(player_spec[0])
    spec.html.render(timeout=60)
    parser = BeautifulSoup(spec.html.html, 'html.parser')

    for gear in parser.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
        epic_list.append(gear.text)
        wowhead_list.append(gear.text)
    for gear in parser.findAll('a', class_="gear-planner-slots-group-slot-link q3", limit=1):
        blue_list.append(gear.text)

    if len(blue_list) != 0:
        epic_list.insert(13, blue_list)
        wowhead_list.insert(13, blue_list)

    create_empty_file(file)
    compare_lists(wowhead_list, file)

    if check_local.is_same is False:
        print(file.capitalize(), 'is different to wowhead. Updating now...', end='')
        create_file(file, epic_list)
        print('[Done!]')
    else:
        print(file.capitalize(), 'is already up to date.')


def scrape_wowhead_list(player_class):
    if player_class == hunter:
        get_list(hunter_beast_mastery_spec, 'hunter_beast_mastery.txt')
        get_list(hunter_marksmanship_spec, 'hunter_marksmanship.txt')
        get_list(hunter_survival_spec, 'hunter_survival.txt')

    if player_class == shaman:
        get_list(shaman_elemental_spec, 'shaman_elemental.txt')
        get_list(shaman_enhancement_spec, 'shaman_enhancement.txt')
        get_list(shaman_restoration_spec, 'shaman_restoration.txt')

    if player_class == warlock:
        get_list(warlock_affliction_spec, 'warlock_affliction.txt')
        get_list(warlock_demonology_spec, 'warlock_demonology.txt')
        get_list(warlock_destruction_spec, 'warlock_destruction.txt')

    print()
