from requests_html import HTMLSession
from bs4 import BeautifulSoup
from utils.class_specs import *
from utils.class_strings import *

session = HTMLSession()


def print_bis_list(player_class, player_spec):
    # beast mastery hunter
    if player_class == hunter and player_spec == beast_mastery:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(hunter_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # marksmanship hunter
    if player_class == hunter and player_spec == marksmanship:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(hunter_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # survival hunter
    if player_class == hunter and player_spec == survival:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(hunter_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "Non-Trapweaving BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(0, 16):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Trapweaving BIS:")
        for x in range(16, 32):
            print(gear_list[x])
        print()

    # affliction warlock
    if player_class == warlock and player_spec == affliction:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(warlock_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(17, 34):
            print(gear_list[x])
        print()

    # demonology warlock
    if player_class == warlock and player_spec == demonology:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(warlock_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "Support BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(0, 17):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Balanced DPS BIS:")
        for x in range(17, 34):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Personal DPS BIS:")
        for x in range(34, 51):
            print(gear_list[x])
        print()

    # destruction warlock
    if player_class == warlock and player_spec == destruction:
        p_class = player_class.title()
        p_spec = player_spec.title()
        gear_list = []
        player_spec = session.get(warlock_specs[2])
        player_spec.html.render(timeout=50)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(17, 34):
            print(gear_list[x])
        print()

    # assassination rogue
    if player_class == rogue and player_spec == assassination:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(rogue_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # combat rogue
    if player_class == rogue and player_spec == combat:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(rogue_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # subtlety rogue
    if player_class == rogue and player_spec == subtlety:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(rogue_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # elemental shaman
    if player_class == shaman and player_spec == elemental:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(shaman_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # enhancement shaman
    if player_class == shaman and player_spec == enhancement:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(shaman_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 12):
            print(gear_list[x])
        for x in range(16, 17):
            print(gear_list[x])
        for x in range(12, 16):
            print(gear_list[x])
        print()

    # restoration shaman
    if player_class == shaman and player_spec == restoration:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(shaman_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # balance druid
    if player_class == druid and player_spec == balance:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(druid_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(0, 17):
            print(gear_list[x])
        print()

    # feral druid dps
    if player_class == druid and player_spec == feral_cat:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(druid_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # feral druid tank
    if player_class == druid and player_spec == feral_bear:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(druid_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 13):
            print(gear_list[x])
        for x in range(28, 29):
            print(gear_list[x])
        for x in range(13, 14):
            print(gear_list[x])
        for x in range(29, 30):
            print(gear_list[x])
        print()

    # restoration druid
    if player_class == druid and player_spec == restoration:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(druid_specs[3])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # discipline priest
    if player_class == priest and player_spec == discipline:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(priest_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(17, 34):
            print(gear_list[x])
        print()

    # holy priest
    if player_class == priest and player_spec == holy:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(priest_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(14, 30):
            print(gear_list[x])
        print()

    # shadow priest
    if player_class == priest and player_spec == shadow:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(priest_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # holy paladin
    if player_class == paladin and player_spec == holy:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(paladin_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(15, 28):
            print(gear_list[x])
        for x in range(32, 33):
            print(gear_list[x])
        for x in range(28, 31):
            print(gear_list[x])
        print()

    # protection paladin
    if player_class == paladin and player_spec == protection:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(paladin_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 12):
            print(gear_list[x])
        for x in range(15, 17):
            print(gear_list[x])
        for x in range(12, 15):
            print(gear_list[x])
        print()

    # retribution paladin
    if player_class == paladin and player_spec == retribution:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(paladin_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(16, 32):
            print(gear_list[x])
        print()

    # arms warrior
    if player_class == warrior and player_spec == arms:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(warrior_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(16, 32):
            print(gear_list[x])
        print()

    # fury warrior
    if player_class == warrior and player_spec == fury:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(warrior_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(17, 34):
            print(gear_list[x])
        print()

    # protection warrior
    if player_class == warrior and player_spec == protection:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(warrior_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "Balanced Set BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 13):
            print(gear_list[x])
        for x in range(32, 34):
            print(gear_list[x])
        for x in range(13, 15):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Mitigation Set BIS:")
        for x in range(16, 29):
            print(gear_list[x])
        for x in range(32, 33):
            print(gear_list[x])
        for x in range(29, 32):
            print(gear_list[x])
        print()

    # arcane mage
    if player_class == mage and player_spec == arcane:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(mage_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "Gloves as Off-Piece BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for x in range(0, 17):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Chest as Off-Piece BIS:")
        for x in range(17, 34):
            print(gear_list[x])
        print("\n" + p_spec, p_class, "Head as Off-Piece BIS:")
        for x in range(34, 51):
            print(gear_list[x])
        print()

    # fire mage
    if player_class == mage and player_spec == fire:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(mage_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # frost mage
    if player_class == mage and player_spec == frost:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(mage_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # blood death knight
    if player_class == death_knight and player_spec == blood:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(death_knight_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 11):
            print(gear_list[x])
        for x in range(14, 16):
            print(gear_list[x])
        for x in range(12, 14):
            print(gear_list[x])
        for x in range(16, 17):
            print(gear_list[x])
        print()

    # frost death knight
    if player_class == death_knight and player_spec == frost:
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(death_knight_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            print(gear.text)
        print()

    # unholy death knight
    if player_class == death_knight and player_spec == unholy:
        gear_list = []
        p_class = player_class.title()
        p_spec = player_spec.title()
        player_spec = session.get(death_knight_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        print(p_spec, p_class, "BIS:")
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q3"):
            gear_list.append(gear.text)
        for x in range(0, 12):
            print(gear_list[x])
        for x in range(16, 17):
            print(gear_list[x])
        for x in range(12, 16):
            print(gear_list[x])
        print()
