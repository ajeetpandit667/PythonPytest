from math_func import StudentDB
import pytest

def test_Ajeet_data():
    db = StudentDB()
    db.connectData('data.json')
    ajeet_data = db.get_data('Ajeet')
    assert ajeet_data["id"] == 101
    assert ajeet_data["name"] == "Ajeet"
    assert ajeet_data["result"] == "passed"

def test_Prasu_data():
    db = StudentDB()
    db.connectData('data.json')
    prasu_data = db.get_data('Prasu')
    assert prasu_data["id"] == 102
    assert prasu_data["name"] == "Prasu"
    assert prasu_data["result"] == "failed"
