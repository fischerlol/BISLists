import os
from utils.class_spec_strings import *
from utils.item_slot_strings import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup


class MyClass:
    def __init__(self):
        self.is_same_local_and_remote = None

    def check_local(self):
        self.is_same_local_and_remote = True


# Instantiate a MyClass object
my_class = MyClass()

# Set the is_same_local_and_remote attribute for this instance
my_class.is_same_local_and_remote = True


def compare_lists(local_list, local_file):
    with open('local/' + str(local_file), 'r') as local_file:
        remote_list = [line.strip() for line in local_file]

    illegal_chars = ['[', ']', '\\', "'", '"']
    local_list = ''.join(str(local_list))
    remote_list = ''.join(str(remote_list))

    for characters in illegal_chars:
        local_list = local_list.replace(characters, '')
        remote_list = remote_list.replace(characters, '')

    if len(local_list) != len(remote_list):
        my_class.is_same_local_and_remote = False
    else:
        my_class.is_same_local_and_remote = True


def create_empty_file(file):
    file_name = str(file)
    file_path = 'local/{}'.format(file)

    file_exists = os.path.exists(file_path)
    if file_exists is False:
        with open(file_path, 'w') as file:
            print(file_name.capitalize(), 'does not exist, Creating now...', end='')
            print('[Done!]')


def write_to_file(player_spec, remote_gear_list):
    illegal_chars = ['[', ']']
    remote_gear_list = ''.join(str(remote_gear_list))
    for characters in illegal_chars:
        remote_gear_list = remote_gear_list.replace(characters, '')
    with open('local/' + str(player_spec), 'w') as file:
        file.write(remote_gear_list)
    file.close()


def remove_from_list(local_list, remote_list, keep_set):
    # Calculate the number of sets in the local list
    num_sets = len(local_list) // 16
    if len(local_list) % 16 == 0:
        num_sets -= 1

    # Calculate the number of elements to remove from the start of the list
    num_to_remove = (keep_set - 1) * 16

    # If the local list has 17 elements per set, add one to the number of elements to remove
    # to account for the extra element in the first set
    if num_sets == keep_set:
        num_to_remove += 1

    # Remove the elements from the start of the local and remote lists
    for i in range(num_to_remove):
        del local_list[0]
        del remote_list[0]


def generate_list(parser, local_list, remote_list):
    """generates a list of epic items into local list_1 and remote list_2"""
    for gear in parser.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
        local_list.append(gear.text)
        remote_list.append(gear.text)


def values(player_spec, local_file):
    local_list, remote_list = [], []
    session = HTMLSession()
    spec = session.get(player_spec[0])
    spec.html.render(timeout=60)
    parser = BeautifulSoup(spec.html.html, 'html.parser')

    # Concatenate the strings in the player spec list to create a unique identifier for the player spec
    player_spec_id = "".join(player_spec)

    # Define a dictionary that maps player spec identifiers (as strings) to the corresponding sets of items to keep
    sets_to_keep = {
        "".join(hunter_beast_mastery_spec): None,
        "".join(hunter_marksmanship_spec): None,
        "".join(hunter_survival_spec): 2,
        "".join(shaman_elemental_spec): None,
        "".join(shaman_enhancement_spec): None,
        "".join(shaman_restoration_spec): None,
        "".join(warlock_affliction_spec): 2,
        "".join(warlock_demonology_spec): None,
        "".join(warlock_destruction_spec): 2,
        "".join(paladin_holy_spec): 2,
        "".join(paladin_protection_spec): None,
        "".join(paladin_retribution_spec): 2,
        "".join(mage_arcane_spec): 2,
        "".join(mage_fire_spec): None,
        "".join(mage_frost_spec): None,
        "".join(rogue_assassination_spec): None,
        "".join(rogue_combat_spec): None,
        "".join(rogue_subtlety_spec): None,
        "".join(druid_balance_spec): 1,
        "".join(druid_feral_cat_spec): None,
        "".join(druid_feral_bear_spec): 1,
        "".join(druid_restoration_spec): None,
        "".join(warrior_arms_spec): 2,
        "".join(warrior_fury_spec): 2,
        "".join(warrior_protection_spec): None,
        "".join(priest_discipline_spec): 2,
        "".join(priest_holy_spec): 2,
        "".join(priest_shadow_spec): None,
        "".join(death_knight_blood_spec): None,
        "".join(death_knight_frost_spec): None,
        "".join(death_knight_unholy_spec): None
    }

    # Iterate over the items in the sets_to_keep dictionary
    for spec, keep_set in sets_to_keep.items():
        # If the spec matches the input player spec identifier
        if spec == player_spec_id:
            # Call the generate_list function
            generate_list(parser, local_list, remote_list)
            # If the keep_set is not None, call the remove_from_list function
            if keep_set is not None:
                remove_from_list(local_list, remote_list, keep_set=keep_set)

    create_empty_file(local_file)
    compare_lists(remote_list, local_file)

    if my_class.is_same_local_and_remote is False:
        print(local_file.capitalize(), 'is different to wowhead. Updating now...', end=' ')
        write_to_file(local_file, local_list)
        print('[Done!]')
    if my_class.is_same_local_and_remote is True:
        print(local_file.capitalize(), 'is already up to date.')


def scrape_wowhead_list(player_class):
    # Define a dictionary that maps player classes to lists of spec URLs and names
    player_class_urls = {
        'hunter': [
            (hunter_beast_mastery_spec, 'hunter_beast_mastery'),
            (hunter_marksmanship_spec, 'hunter_marksmanship'),
            (hunter_survival_spec, 'hunter_survival')
        ],
        'shaman': [
            (shaman_elemental_spec, 'shaman_elemental'),
            (shaman_enhancement_spec, 'shaman_enhancement'),
            (shaman_restoration_spec, 'shaman_restoration')
        ],
        'warlock': [
            (warlock_affliction_spec, 'warlock_affliction'),
            (warlock_demonology_spec, 'warlock_demonology'),
            (warlock_destruction_spec, 'warlock_destruction')
        ],
        'paladin': [
            (paladin_holy_spec, 'paladin_holy'),
            (paladin_protection_spec, 'paladin_protection'),
            (paladin_retribution_spec, 'paladin_retribution')
        ],
        'mage': [
            (mage_arcane_spec, 'mage_arcane'),
            (mage_fire_spec, 'mage_fire'),
            (mage_frost_spec, 'mage_frost')
        ],
        'rogue': [
            (rogue_assassination_spec, 'rogue_assassination'),
            (rogue_combat_spec, 'rogue_combat'),
            (rogue_subtlety_spec, 'rogue_subtlety')
        ],
        'druid': [
            (druid_balance_spec, 'druid_balance'),
            (druid_feral_cat_spec, 'druid_feral_cat'),
            (druid_feral_bear_spec, 'druid_feral_bear'),
            (druid_restoration_spec, 'druid_restoration')
        ],
        'warrior': [
            (warrior_arms_spec, 'warrior_arms'),
            (warrior_fury_spec, 'warrior_fury'),
            (warrior_protection_spec, 'warrior_protection'),
        ],
        'priest': [
            (priest_discipline_spec, 'priest_discipline'),
            (priest_holy_spec, 'priest_holy'),
            (priest_shadow_spec, 'priest_shadow'),
        ],
        'death_knight': [
            (death_knight_blood_spec, 'death_knight_blood'),
            (death_knight_frost_spec, 'death_knight_frost'),
            (death_knight_unholy_spec, 'death_knight_unholy'),
        ]

    }

    # Get the list of spec URLs and names for the given player class
    spec_urls = player_class_urls[player_class]

    # Iterate over the spec URLs and names and call the bis_list function on each one
    for spec_url, spec_name in spec_urls:
        values(spec_url, f"{spec_name}.txt")
