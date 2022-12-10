import os
from utils.class_spec_strings import *
from utils.class_strings import *
from utils.item_slot_strings import *
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


def remove_from_list(list_1, list_2, keep_set):
    count = 0
    for x in list_1:
        count += 1
        print('item:', [x], 'slot:', count - 1)
    """takes items out of list_1 and list_2 depending on keep_set"""
    match keep_set:
        case 1:
            if len(list_1) % 2 == 0:
                del list_1[set_2_start[0]:set_2_end[0]]
                del list_2[set_2_start[0]:set_2_end[0]]
            if len(list_1) % 3 == 0:
                del list_1[set_2_start[0]:set_2_end[0]]
                del list_2[set_2_start[0]:set_2_end[0]]
                del list_1[set_3_start[0]:set_3_end[0]]
                del list_2[set_3_start[0]:set_3_end[0]]
        case 2:
            if len(list_1) % 1 == 0:
                del list_1[set_1_start[0]:set_1_end[0]]
                del list_2[set_1_start[0]:set_1_end[0]]
            if len(list_1) % 3 == 0:
                del list_1[set_3_start[0]:set_3_end[0]]
                del list_2[set_3_start[0]:set_3_end[0]]
        case 3:
            if len(list_1) % 1 == 0:
                del list_1[set_1_start[0]:set_1_end[0]]
                del list_2[set_1_start[0]:set_1_end[0]]
            if len(list_1) % 2 == 0:
                del list_1[set_2_start[0]:set_2_end[0]]
                del list_2[set_2_start[0]:set_2_end[0]]


def generate_list(parser, list_1, list_2):
    """generates a list of epic items into local list_1 and remote list_2"""
    for gear in parser.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
        list_1.append(gear.text)
        list_2.append(gear.text)


def bis_list(player_spec, file):
    check_local()
    epic_list, wowhead_list = [], []
    session = HTMLSession()
    spec = session.get(player_spec[0])
    spec.html.render(timeout=60)
    parser = BeautifulSoup(spec.html.html, 'html.parser')

    if player_spec == paladin_holy_spec:
        generate_list(parser, epic_list, wowhead_list)
        remove_from_list(epic_list, wowhead_list, keep_set=2)

    elif player_spec == paladin_protection_spec:
        pass

    elif player_spec == paladin_retribution_spec:
        pass

    elif player_spec == mage_arcane_spec:
        generate_list(parser, epic_list, wowhead_list)
        remove_from_list(epic_list, wowhead_list, keep_set=2)

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
        bis_list(hunter_beast_mastery_spec, 'hunter_beast_mastery.txt')
        bis_list(hunter_marksmanship_spec, 'hunter_marksmanship.txt')
        bis_list(hunter_survival_spec, 'hunter_survival.txt')

    if player_class == shaman:
        bis_list(shaman_elemental_spec, 'shaman_elemental.txt')
        bis_list(shaman_enhancement_spec, 'shaman_enhancement.txt')
        bis_list(shaman_restoration_spec, 'shaman_restoration.txt')

    if player_class == warlock:
        bis_list(warlock_affliction_spec, 'warlock_affliction.txt')
        bis_list(warlock_demonology_spec, 'warlock_demonology.txt')
        bis_list(warlock_destruction_spec, 'warlock_destruction.txt')

    if player_class == paladin:
        bis_list(paladin_holy_spec, 'paladin_holy.txt')
        bis_list(paladin_protection_spec, 'paladin_protection.txt')
        bis_list(paladin_retribution_spec, 'paladin_retribution.txt')

    if player_class == mage:
        bis_list(mage_arcane_spec, 'mage_arcane.txt')

    print()
