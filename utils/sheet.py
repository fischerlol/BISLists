import gspread
from gspread_formatting import *
from utils.class_strings import *
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Create a Credentials object using the service account info
creds = ServiceAccountCredentials.from_json_keyfile_name('gspread/service_account.json', scope)

# Use the gspread library to authenticate with the Google Sheets API using the Credentials object
client = gspread.authorize(creds)

# Open the 'BIS Lists' Google Sheets document
document = client.open('BIS Lists')


def create_sheets():
    worksheets = document.worksheets()
    worksheet_titles = [worksheet.title for worksheet in worksheets]
    requests = []

    for classes in classes_3:
        if classes.title() not in worksheet_titles:
            requests.append({
                "addSheet": {
                    "properties": {
                        "title": classes.title(),
                        "gridProperties": {
                            "rowCount": 20,
                            "columnCount": 4
                        }
                    }
                }
            })

    for classes in classes_4:
        if classes.title() not in worksheet_titles:
            requests.append({
                "addSheet": {
                    "properties": {
                        "title": classes.title(),
                        "gridProperties": {
                            "rowCount": 20,
                            "columnCount": 5
                        }
                    }
                }
            })

    for classes in classes_5:
        if classes.title() not in worksheet_titles:
            requests.append({
                "addSheet": {
                    "properties": {
                        "title": classes.title(),
                        "gridProperties": {
                            "rowCount": 20,
                            "columnCount": 6
                        }
                    }
                }
            })

    if requests:
        document.batch_update({"requests": requests})


def equipment_slots():
    # List of consistent equipment slots for all classes
    consistent_equipment_slots = ['Slot/Spec', 'Head', 'Neck', 'Shoulders', 'Back', 'Chest',
                                  'Wrist', 'Hands', 'Waist', 'Legs', 'Feet',
                                  'Ring 1', 'Ring 2', 'Trinket 1', 'Trinket 2', 'Main Hand',
                                  'Off-Hand']

    # Dictionary of additional equipment slots for each class
    additional_slots_by_class = {
        'death knight': ['Relic'],
        'shaman': ['Totem'],
        'paladin': ['Libram'],
        'druid': ['Idol'],
        'rogue': ['Ranged'],
        'priest': ['Ranged'],
        'hunter': ['Ranged'],
        'warrior': ['Ranged'],
        'warlock': ['Ranged'],
        'mage': ['Ranged'],
    }

    # Retrieve all the worksheets in the document at once
    worksheets = document.worksheets()

    # Convert the list of worksheets to a dictionary, with the class name as the key
    worksheets_by_class = {worksheet.title.lower(): worksheet for worksheet in worksheets}

    for class_name in all_classes:
        # Retrieve the worksheet for this class from the dictionary
        worksheet = worksheets_by_class.get(class_name)

        if not worksheet:
            continue

        horizontal = cellFormat(horizontalAlignment='CENTER')
        format_cell_range(worksheet, 'A1:D20', horizontal)
        set_column_width(worksheet, 'A', 175)
        get_slots = worksheet.get('A3:A20')

        if not get_slots:
            # Concatenate the list of consistent equipment slots with the additional slots for this class
            all_slots = consistent_equipment_slots + additional_slots_by_class.get(class_name, [])

            # Convert the list of strings to a list of lists, with each inner list containing a single string
            all_slots = [[slot] for slot in all_slots]

            # Update the worksheet
            worksheet.update('A2:A19', all_slots)
            worksheet.update('A20', 'Date:')


def class_specializations():
    class_data = {
        'death knight': ['Blood', 'Frost', 'Unholy'],
        'druid': ['Balance', 'Feral', 'Guardian', 'Restoration'],
        'hunter': ['Beast Mastery', 'Marksmanship', 'Survival'],
        'mage': ['Arcane', 'Fire', 'Frost'],
        'paladin': ['Holy', 'Protection', 'Retribution'],
        'priest': ['Discipline', 'Holy', 'Shadow'],
        'rogue': ['Assassination', 'Combat', 'Subtlety'],
        'shaman': ['Elemental', 'Enhancement', 'Restoration'],
        'warlock': ['Affliction', 'Demonology', 'Destruction'],
        'warrior': ['Arms', 'Fury', 'Protection']
    }

    for class_name in all_classes:
        worksheet = document.worksheet(class_name.title())

        # Create a list of requests to be executed in a single batch update
        requests = []  # noqa

        # Merge the A, B, C and D together in row 1
        requests.append({
            "mergeCells": {
                "range": {
                    "sheetId": worksheet.id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 3
                },
                "mergeType": "MERGE_ALL"
            }
        })

        # Update the first cell with the class name
        requests.append({
            "updateCells": {
                "range": {
                    "sheetId": worksheet.id,
                    "startRowIndex": 0,
                    "endRowIndex": 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "rows": [
                    {
                        "values": [
                            {
                                "userEnteredValue": {
                                    "stringValue": class_name.title() + ' Gear'
                                }
                            }
                        ]
                    }
                ],
                "fields": "userEnteredValue"
            }
        })

        # Update the specializations for the current class
        specializations = class_data.get(class_name)
        if specializations:
            requests.append({
                "updateCells": {
                    "range": {
                        "sheetId": worksheet.id,
                        "startRowIndex": 1,
                        "endRowIndex": 2,
                        "startColumnIndex": 1,
                        "endColumnIndex": 5
                    },
                    "rows": [
                        {
                            "values": [
                                {
                                    "userEnteredValue": {
                                        "stringValue": spec
                                    }
                                } for spec in specializations
                            ]
                        }
                    ],
                    "fields": "userEnteredValue"
                }
            })

        # Execute the batch update
        if requests:
            document.batch_update({"requests": requests})


def get_local_list(local_file):
    with open('local/' + str(local_file)) as f:
        local_list = f.read()

    local_list = [item.strip() for item in local_list.split(',')]

    return local_list


def add_local_list_to_google_sheets(local_list, player_class, spec):
    col_mapping = {
        'Rogue': {
            'Assassination': 2,
            'Combat': 3,
            'Subtlety': 4,
        },
        'Shaman': {
            'Elemental': 2,
            'Enhancement': 3,
            'Restoration': 4,
        },
        'Priest': {
            'Discipline': 2,
            'Holy': 3,
            'Shadow': 4,
        },
        'Paladin': {
            'Holy': 2,
            'Protection': 3,
            'Retribution': 4,
        },
        'Death Knight': {
            'Blood': 2,
            'Frost': 3,
            'Unholy': 4,
        },
        'Hunter': {
            'Beast Mastery': 2,
            'Marksmanship': 3,
            'Survival': 4,
        },
        'Druid': {
            'Balance': 2,
            'Feral': 3,
            'Guardian': 4,
            'Restoration': 5,
        },
        'Warrior': {
            'Arms': 2,
            'Fury': 3,
            'Protection': 4,
        },
        'Warlock': {
            'Affliction': 2,
            'Demonology': 3,
            'Destruction': 4,
        },
        'Mage': {
            'Arcane': 2,
            'Fire': 3,
            'Frost': 4,
        }
    }

    col = col_mapping[player_class].get(spec)
    if not col:
        return
    local_list = get_local_list(local_list)

    worksheet = document.worksheet(player_class.title())

    cell_updates = []
    for i, item in enumerate(local_list):
        item = item.replace("'", "").replace('"', '')
        cell_updates.append(gspread.Cell(i + 3, col, value=item))
    worksheet.update_cells(cell_updates)


def populate_sheet():
    # rogue
    add_local_list_to_google_sheets('rogue_assassination.txt', 'Rogue', 'Assassination')
    add_local_list_to_google_sheets('rogue_combat.txt', 'Rogue', 'Combat')
    add_local_list_to_google_sheets('rogue_subtlety.txt', 'Rogue', 'Subtlety')

    # shaman
    add_local_list_to_google_sheets('shaman_elemental.txt', 'Shaman', 'Elemental')
    add_local_list_to_google_sheets('shaman_enhancement.txt', 'Shaman', 'Enhancement')
    add_local_list_to_google_sheets('shaman_restoration.txt', 'Shaman', 'Restoration')

    # priest
    add_local_list_to_google_sheets('priest_discipline.txt', 'Priest', 'Discipline')
    add_local_list_to_google_sheets('priest_holy.txt', 'Priest', 'Holy')
    add_local_list_to_google_sheets('priest_shadow.txt', 'Priest', 'Shadow')

    # paladin
    add_local_list_to_google_sheets('paladin_holy.txt', 'Paladin', 'Holy')
    add_local_list_to_google_sheets('paladin_protection.txt', 'Paladin', 'Protection')
    add_local_list_to_google_sheets('paladin_retribution.txt', 'Paladin', 'Retribution')

    # death knight
    add_local_list_to_google_sheets('death_knight_blood.txt', 'Death Knight', 'Blood')
    add_local_list_to_google_sheets('death_knight_frost.txt', 'Death Knight', 'Frost')
    add_local_list_to_google_sheets('death_knight_unholy.txt', 'Death Knight', 'Unholy')

    # hunter
    add_local_list_to_google_sheets('hunter_beast_mastery.txt', 'Hunter', 'Beast Mastery')
    add_local_list_to_google_sheets('hunter_marksmanship.txt', 'Hunter', 'Marksmanship')
    add_local_list_to_google_sheets('hunter_survival.txt', 'Hunter', 'Survival')

    # druid
    add_local_list_to_google_sheets('druid_balance.txt', 'Druid', 'Balance')
    add_local_list_to_google_sheets('druid_balance.txt', 'Druid', 'Feral')
    add_local_list_to_google_sheets('druid_balance.txt', 'Druid', 'Guardian')
    add_local_list_to_google_sheets('druid_balance.txt', 'Druid', 'Restoration')

    # warrior
    add_local_list_to_google_sheets('warrior_arms.txt', 'Warrior', 'Arms')
    add_local_list_to_google_sheets('warrior_fury.txt', 'Warrior', 'Fury')
    add_local_list_to_google_sheets('warrior_protection.txt', 'Warrior', 'Protection')

    # warlock
    add_local_list_to_google_sheets('warlock_affliction.txt', 'Warlock', 'Affliction')
    add_local_list_to_google_sheets('warlock_demonology.txt', 'Warlock', 'Demonology')
    add_local_list_to_google_sheets('warlock_destruction.txt', 'Warlock', 'Destruction')

    # mage
    add_local_list_to_google_sheets('mage_arcane.txt', 'Mage', 'Arcane')
    add_local_list_to_google_sheets('mage_fire.txt', 'Mage', 'Fire')
    add_local_list_to_google_sheets('mage_frost.txt', 'Mage', 'Frost')


def initial_setup():
    create_sheets()
    equipment_slots()
    class_specializations()
