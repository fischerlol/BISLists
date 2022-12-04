import gspread
import time
from gspread_formatting import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from utils.class_specs import *
from utils.class_strings import *

service_account = gspread.service_account(filename='gspread/service_account.json')
sheet = service_account.open("BIS Lists")

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


def format_cells(worksheet, player_spec, spec_count):
    horizontal = cellFormat(horizontalAlignment='CENTER')
    format_cell_range(worksheet, 'A2:D19', horizontal)
    set_column_width(worksheet, 'A', 175)

    if spec_count == 3:
        worksheet.merge_cells('A1:D1')
        set_column_width(worksheet, 'B:D', 275)
        format_cell_range(worksheet, 'B2:D2', horizontal)
        format_cell_range(worksheet, 'A1', horizontal)

        if player_spec == rogue.title():
            worksheet.update('A1', [['Rogue Gear']])
            worksheet.update('A2:D2', [['Slot/Spec', 'Assassination', 'Combat', 'Subtlety']])
        if player_spec == shaman.title():
            worksheet.update('A1', [['Shaman Gear']])
            worksheet.update('A2:D2', [
                ['Slot/Spec', 'Elemental', 'Enhancement', 'Restoration']])
        if player_spec == priest.title():
            worksheet.update('A1', [['Priest Gear']])
            worksheet.update('A2:D2', [
                ['Slot/Spec', 'Discipline', 'Holy', 'Shadow']])
        if player_spec == paladin.title():
            worksheet.update('A1', [['Paladin Gear']])
            worksheet.update('A2:D2 ', [
                ['Slot/Spec', 'Holy', 'Protection', 'Retribution']])
        if player_spec == death_knight.title():
            worksheet.update('A1', [['Death Knight Gear']])
            worksheet.update('A2:D2', [
                ['Slot/Spec', 'Blood', 'Frost', 'Unholy']])

    if spec_count == 4:
        worksheet.merge_cells('A1:E1')
        set_column_width(worksheet, 'B:E', 275)
        format_cell_range(worksheet, 'B2:E19', horizontal)
        format_cell_range(worksheet, 'A1', horizontal)

        if player_spec == hunter.title():
            worksheet.update('A1', [['Hunter Gear']])
            worksheet.update('A2:E2', [
                ['Slot/Spec', 'Beast Mastery', 'Marksmanship', 'Survival Non-Trapweaving',
                 'Survival Trapweaving']])
        if player_spec == druid.title():
            worksheet.update('A1', [['Druid Gear']])
            worksheet.update('A2:E2', [
                ['Slot/Spec', 'Balance', 'Feral DPS', 'Feral Tank',
                 'Restoration']])
        if player_spec == warrior.title():
            worksheet.update('A1', [['Warrior Gear']])
            worksheet.update('A2:E2', [
                ['Slot/Spec', 'Arms', 'Fury', 'Protection Balanced',
                 'Protection Mitigation']])

    if spec_count == 5:
        worksheet.merge_cells('A1:F1')
        set_column_width(worksheet, 'B:F', 275)
        format_cell_range(worksheet, 'B2:F19', horizontal)
        format_cell_range(worksheet, 'A1', horizontal)

        if player_spec == warlock.title():
            worksheet.update('A1', [['Warlock Gear']])
            worksheet.update('A2:F2', [
                ['Slot/Spec', 'Affliction', 'Demonology Support', 'Demonology Balanced',
                 'Demonology Personal',
                 'Destruction']])
        if player_spec == mage.title():
            worksheet.update('A1', [['Mage Gear']])
            worksheet.update('A2:F2', [
                ['Slot/Spec', 'Arcane Gloves as Off-Piece', 'Arcane Chest as Off-Piece',
                 'Arcane Head as Off-Piece',
                 'Fire', 'Frost']])


def populate_sheet(worksheet, player_class, player_spec):
    # beast mastery hunter
    if player_class == hunter.title() and player_spec == beast_mastery:
        bis_list, sheet_list = [], []
        player_spec = session.get(hunter_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')

        for x in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            bis_list.append(x.text)
        for y in worksheet.get_values('B3:B19'):
            sheet_list.append(y)

        bis_list.insert(len(bis_list) - 1, '-')
        illegal_chars = ['[', ']']
        list_x = ''.join(str(bis_list))
        list_y = ''.join(str(sheet_list))

        for characters in illegal_chars:
            list_x = list_x.replace(characters, '')
            list_y = list_y.replace(characters, '')

        print(list_x)
        print(list_y)
        print(len(list_x), len(list_y))

        if len(list_x) == len(list_y):
            pass
        if len(list_x) != len(list_y):
            print('start')
            worksheet.update('B3:B19',
                             [[bis_list[0]], [bis_list[1]], [bis_list[2]], [bis_list[3]], [bis_list[4]],
                              [bis_list[5]], [bis_list[6]], [bis_list[7]], [bis_list[8]], [bis_list[9]],
                              [bis_list[10]], [bis_list[11]], [bis_list[12]], [bis_list[13]],
                              [bis_list[14]], [bis_list[15]], [bis_list[16]]])

    # marksmanship hunter
    if player_class == hunter.title() and player_spec == marksmanship:
        bis_list, sheet_list = [], []
        player_spec = session.get(hunter_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')

        for x in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            bis_list.append(x.text)
        for y in worksheet.get_values('C3:C19'):
            sheet_list.append(y)

        bis_list.insert(len(bis_list) - 1, '-')
        illegal_chars = ['[', ']']
        list_x = ''.join(str(bis_list))
        list_y = ''.join(str(sheet_list))

        for characters in illegal_chars:
            list_x = list_x.replace(characters, '')
            list_y = list_y.replace(characters, '')

        print(list_x)
        print(list_y)
        print(len(list_x), len(list_y))

        if len(list_x) == len(list_y):
            pass
        if len(list_x) != len(list_y):
            print('start')
            worksheet.update('C3:C19',
                             [[bis_list[0]], [bis_list[1]], [bis_list[2]], [bis_list[3]], [bis_list[4]],
                              [bis_list[5]], [bis_list[6]], [bis_list[7]], [bis_list[8]], [bis_list[9]],
                              [bis_list[10]], [bis_list[11]], [bis_list[12]], [bis_list[13]],
                              [bis_list[14]], [bis_list[15]], [bis_list[16]]])

    # survival hunter
    if player_class == hunter.title() and player_spec == survival:
        bis_list, sheet_list = [], []
        player_spec = session.get(hunter_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')

        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            bis_list.append(gear.text)
        for gear in worksheet.get_values('D3:D19'):
            sheet_list.append(gear)
        for gear in worksheet.get_values('E3:E19'):
            sheet_list.append(gear)

        bis_list.insert(len(bis_list) - 1, '-')
        bis_list.insert(len(bis_list) - 18, '-')
        illegal_chars = ['[', ']']

        list_x = ''.join(str(bis_list))
        list_y = ''.join(str(sheet_list))

        for characters in illegal_chars:
            list_x = list_x.replace(characters, '')
            list_y = list_y.replace(characters, '')

        print(list_x)
        print(list_y)
        print(len(list_x), len(list_y))

        if len(list_x) == len(list_y):
            pass
        if len(list_x) != len(list_y):
            print('start')
            worksheet.update('D3:D19', [[bis_list[0]], [bis_list[1]], [bis_list[2]], [bis_list[3]], [bis_list[4]],
                                        [bis_list[5]], [bis_list[6]], [bis_list[7]], [bis_list[8]], [bis_list[9]],
                                        [bis_list[10]], [bis_list[11]], [bis_list[12]], [bis_list[13]],
                                        [bis_list[14]], [bis_list[15]], [bis_list[16]]])
            worksheet.update('E3:E19',
                             [[bis_list[17]], [bis_list[18]], [bis_list[19]], [bis_list[20]], [bis_list[21]],
                              [bis_list[22]], [bis_list[23]], [bis_list[24]], [bis_list[25]], [bis_list[26]],
                              [bis_list[27]], [bis_list[28]], [bis_list[29]], [bis_list[30]],
                              [bis_list[31]], [bis_list[32]], [bis_list[33]]])

    # assassination rogue
    if player_class == rogue.title() and player_spec == assassination:
        gear_list = []
        player_spec = session.get(rogue_specs[0])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)

        worksheet.update('B3:B19', [[gear_list[0]], [gear_list[1]], [gear_list[2]], [gear_list[3]], [gear_list[4]],
                                    [gear_list[5]], [gear_list[6]], [gear_list[7]], [gear_list[8]], [gear_list[9]],
                                    [gear_list[10]], [gear_list[11]], [gear_list[12]], [gear_list[13]],
                                    [gear_list[14]], [gear_list[15]], [gear_list[16]]])

    # combat rogue
    if player_class == rogue.title() and player_spec == combat:
        gear_list = []
        player_spec = session.get(rogue_specs[1])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)

        worksheet.update('C3:C19', [[gear_list[0]], [gear_list[1]], [gear_list[2]], [gear_list[3]], [gear_list[4]],
                                    [gear_list[5]], [gear_list[6]], [gear_list[7]], [gear_list[8]], [gear_list[9]],
                                    [gear_list[10]], [gear_list[11]], [gear_list[12]], [gear_list[13]],
                                    [gear_list[14]], [gear_list[15]], [gear_list[16]]])

    # subtlety rogue
    if player_class == rogue.title() and player_spec == subtlety:
        gear_list = []
        player_spec = session.get(rogue_specs[2])
        player_spec.html.render(timeout=60)
        player_spec = BeautifulSoup(player_spec.html.html, 'html.parser')
        for gear in player_spec.findAll('a', class_="gear-planner-slots-group-slot-link q4"):
            gear_list.append(gear.text)

        worksheet.update('D3:D19', [[gear_list[0]], [gear_list[1]], [gear_list[2]], [gear_list[3]], [gear_list[4]],
                                    [gear_list[5]], [gear_list[6]], [gear_list[7]], [gear_list[8]], [gear_list[9]],
                                    [gear_list[10]], [gear_list[11]], [gear_list[12]], [gear_list[13]],
                                    [gear_list[14]], [gear_list[15]], [gear_list[16]]])


def initial_sheet_setup():
    try:
        for x in classes_3:
            sheet.add_worksheet(title=x.title(), rows='20', cols='4')
        for x in classes_4:
            sheet.add_worksheet(title=x.title(), rows='20', cols='5')
        for x in classes_5:
            sheet.add_worksheet(title=x.title(), rows='20', cols='6')
    except gspread.exceptions.GSpreadException:
        pass

    for x in all_classes:
        # time.sleep(1)
        worksheet = sheet.worksheet(x.title())
        get_values = worksheet.get('A3:A19')
        if not get_values:
            worksheet.update('A3:A19',
                             [['Head'], ['Neck'], ['Shoulders'], ['Back'], ['Chest'],
                              ['Wrist'], ['Hands'], ['Waist'], ['Legs'], ['Feet'],
                              ['Ring 1'], ['Ring 2'], ['Trinket 1'], ['Trinket 2'], ['Main Hand'],
                              ['Off-Hand'], ['Ranged']])
        pass

        match x.title():
            case 'Rogue':
                get_values = worksheet.get('A2:D2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, x.title(), 3)
                pass
                # populate_sheet(worksheet, x.title(), assassination)
                # populate_sheet(worksheet, x.title(), combat)
                # populate_sheet(worksheet, x.title(), subtlety)
            case 'Shaman':
                get_values = worksheet.get('A2:D2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, shaman.title(), 3)
                pass
            case 'Priest':
                get_values = worksheet.get('A2:D2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, priest.title(), 3)
                pass
            case 'Paladin':
                get_values = worksheet.get('A2:D2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, paladin.title(), 3)
                pass
            case 'Death Knight':
                get_values = worksheet.get('A2:D2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, death_knight.title(), 3)
                pass
            case 'Hunter':
                get_values = worksheet.get('A2:E2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, hunter.title(), 4)
                pass
                populate_sheet(worksheet, x.title(), beast_mastery)
                populate_sheet(worksheet, x.title(), marksmanship)
                populate_sheet(worksheet, x.title(), survival)
            case 'Druid':
                get_values = worksheet.get('A2:E2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, druid.title(), 4)
                pass
            case 'Warrior':
                get_values = worksheet.get('A2:E2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, warrior.title(), 4)
                pass
            case 'Warlock':
                get_values = worksheet.get('A2:F2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, warlock.title(), 5)
                pass
            case 'Mage':
                get_values = worksheet.get('A2:F2') and worksheet.get('A1')
                if not get_values:
                    format_cells(worksheet, mage.title(), 5)
                pass
