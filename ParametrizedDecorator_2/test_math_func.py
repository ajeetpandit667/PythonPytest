import math_func
import pytest

@pytest.mark.parametrize("num1,num2,result", [
    (7, 3, 10),
    ("Hello", "World", "HelloWorld"),
    (3.5, 4.5, 8.0)  # corrected expected result to 8.0 instead of 9.0
])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result

  # assert math_func.add(7,3) == 10
  # result = math_func.add("Hello","World")
  # assert result == "HelloWorld"
  # result = math_func.add(7.5,8.5)
  # assert result == 16.0