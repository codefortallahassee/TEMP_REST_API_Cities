# requires
# pip install airtable
# pip install airtable-python-wrapper

import json
import airtable
from airtable import Airtable


key_File = open("../resources/key")
BASE_ID = keyFile.readline().rstrip()  # found in url of API documentation for table

CITIES_TABLE = "USCities"

def create_cities_object():
    return Airtable(BASE_ID, CITIES_TABLE)

def airtable_call():

    airtable_object = Airtable(BASE_ID, CITIES_TABLE)
    records = airtable_object.get_all()

    cities_list = []

    for record in records:

        od = {'Id': []}  # Original Dictionary

        try:
            od['Id'] = record['Cities']['GEO.id']
        except KeyError:
            continue # every record needs an ID, skip if there is not one
        try:
            od['Name'] = record['Cities']['GEO.display-label']
        except KeyError:
            pass

        cities_list.append(od)

    with open("output.json", "w") as f:
        json.dump(service_list, f, indent=2)

    return cities_list
