import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf)
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as jsonf:
        json.dump(rows, jsonf, indent=4)

if __name__ == "__main__":
    convert_csv_to_json('profiles1.csv', 'data.json')

