from math_func import StudentDB

import pytest


# @pytest.fixture
@pytest.fixture(scope="module")
def db():
  print("---------setup---------")
  db=StudentDB()
  db.connectData('data.json')
  # return db
  # use yield if you want to run both setup and teardown modules 
  yield db 
  print("-----------teardown----------")
  db.close()

def test_Ajeet_data(db):
    ajeet_data = db.get_data('Ajeet')
    assert ajeet_data["id"] == 101
    assert ajeet_data["name"] == "Ajeet"
    assert ajeet_data["result"] == "passed"

def test_Prasu_data(db):
    prasu_data = db.get_data('Prasu')
    assert prasu_data["id"] == 102
    assert prasu_data["name"] == "Prasu"
    assert prasu_data["result"] == "failed"
