from math_func import StudentDB
import pytest


db = None
def setup_module(module):
  print("------------setup-----------")
  global db
  db=StudentDB()
  db.connectData('data.json')
  
def teardown_module(module):
  print("------------teardown-----------")
  db.close()
    

def test_Ajeet_data():
    ajeet_data = db.get_data('Ajeet')
    assert ajeet_data["id"] == 101
    assert ajeet_data["name"] == "Ajeet"
    assert ajeet_data["result"] == "passed"

def test_Prasu_data():
    prasu_data = db.get_data('Prasu')
    assert prasu_data["id"] == 102
    assert prasu_data["name"] == "Prasu"
    assert prasu_data["result"] == "failed"
