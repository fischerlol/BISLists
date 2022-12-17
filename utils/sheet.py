import time
import gspread
from gspread.exceptions import APIError
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
                            "columnCount": 40
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
                            "columnCount": 50
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
                            "columnCount": 60
                        }
                    }
                }
            })

    if requests:
        document.batch_update({"requests": requests})


def equipment_slots1():
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

    for class_name in all_classes:
        worksheet = document.worksheet(class_name.title())
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

            # Pause execution for 1 second to allow API quota to reset
            time.sleep(1)


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


def populate_sheet():
    pass


def initial_setup():
    create_sheets()
    equipment_slots()
    class_specializations()
