import csv
import json
import pytest

def test_csv_has_12_columns():
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert len(headers) == 12

def test_csv_has_900_rows():
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        rows = list(reader)
        assert len(rows) >= 900

def test_json_has_correct_structure():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert len(data) > 0
        keys = data[0].keys()
        assert len(keys) == 12

def test_json_has_900_rows():
    with open('data.json', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) >= 900
