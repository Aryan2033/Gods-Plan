import pytest
from calculator import Calculator

# def test_divide():
#     calc=Calculator()

#     with pytest.raises(ValueError) : #tells pytest to pass the test only if the next line raises a ValueError
#         calc.divide(10,0)


# if __name__=="__main__":
#     try:
#         test_divide()
#         print("test is passed successfully: division by zero raises ValueError")
#     except AssertionError as e:
#         print(f"test failed: {e}")


def test_add():
    calc=Calculator()
    assert calc.add(2,3)==5,"This test will fail because the add function is currently subtracting instead of adding."
