import BasicCommand.math_func as math_func
import pytest 
import sys

# @pytest.mark.number
# @pytest.mark.skip("i dont want to check this")
@pytest.mark.skipIf(sys.version_info < (3,3) ,reason="just skip it ") 
def test_add():
  assert math_func.add(7,3) == 10
  assert math_func.add(7) == 9
  print(math_func.add(7),"--------------------")

# @pytest.mark.number 

def test_product():
  assert math_func.product(5,5)==25
  assert math_func.product(4)==8

# @pytest.mark.string  
def test_add_str():
  result = math_func.add_str("hello")
  assert result == "helloworld"
  assert type(result) is str
  assert "hello" in result

# @pytest.mark.string  
def test_product_str():
  result = math_func.product_str("hello") 
  assert result == "hellohello"
  assert type(result) is str
  assert "hello" in result