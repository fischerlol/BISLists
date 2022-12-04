from utils.class_strings import *
from utils.functions import print_bis_list
from utils.functions import initial_sheet_setup


def main():
    print("Scraping bis lists from Wowhead...\n")

    # hunter bis list
    # print_bis_list(hunter, survival)
    # print_bis_list(hunter, marksmanship)
    # print_bis_list(hunter, beast_mastery)

    # warlock bis list
    # print_bis_list(warlock, affliction)
    # print_bis_list(warlock, demonology)
    # print_bis_list(warlock, destruction)

    # rogue bis list
    # print_bis_list(rogue, assassination)
    # print_bis_list(rogue, combat)
    # print_bis_list(rogue, subtlety)

    # shaman bis list
    # print_bis_list(shaman, elemental)
    # print_bis_list(shaman, enhancement)
    # print_bis_list(shaman, restoration)

    # druid bis list
    # print_bis_list(druid, balance)
    # print_bis_list(druid, feral_cat)
    # print_bis_list(druid, feral_bear)
    # print_bis_list(druid, restoration)

    # priest bis list
    # print_bis_list(priest, discipline)
    # print_bis_list(priest, holy)
    # print_bis_list(priest, shadow)

    # paladin bis list
    # print_bis_list(paladin, holy)
    # print_bis_list(paladin, protection)
    # print_bis_list(paladin, retribution)

    # warrior bis list
    # print_bis_list(warrior, arms)
    # print_bis_list(warrior, fury)
    # print_bis_list(warrior, protection)

    # mage bis list
    # print_bis_list(mage, arcane)
    # print_bis_list(mage, fire)
    # print_bis_list(mage, frost)

    # death knight bis list
    # print_bis_list(death_knight, blood)
    # print_bis_list(death_knight, frost)
    # print_bis_list(death_knight, unholy)

    # test
    # send_data_to_sheet(hunter)
    initial_sheet_setup()


if __name__ == "__main__":
    main()
