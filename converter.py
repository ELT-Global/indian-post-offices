import csv
import json
import re
import sys

def clean_officename(name):
    # Remove trailing "B.O", "BO", "S.O", or "SO" (with optional periods) and extra whitespace.
    # Strip away duplicate whitespace and titlecase the name.
    name = re.sub(' +', ' ', name.strip().title())
    tokens = name.split(' ')
    area = []
    for token in tokens:
        processed_area = token.replace('.', '').replace(' ', '').upper()
        if processed_area in { 'SO', 'BO', 'RS', 'HO' }:
            area.append(processed_area)
        else:
            area.append(token)
    return ' '.join(area)


def titlecase(text):
    return text.strip().title()

def csv_to_json(csv_filename, json_filename):
    data_by_pincode = {}
    
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pincode = int(row['pincode'])
            state = titlecase(row['statename'])
            district = titlecase(row['district'])
            office = clean_officename(row['officename'])
            
            if pincode not in data_by_pincode:
                data_by_pincode[pincode] = {
                    "_id": pincode,
                    "state": state,
                    "district": district,
                    "offices": []
                }
            if office not in data_by_pincode[pincode]["offices"]:
                data_by_pincode[pincode]["offices"].append(office)
    
    json_data = list(data_by_pincode.values())
    
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.csv output.json")
        sys.exit(1)
    csv_filename = sys.argv[1]
    json_filename = sys.argv[2]
    csv_to_json(csv_filename, json_filename)
