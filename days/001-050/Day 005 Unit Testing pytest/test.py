import pytest
from calculator import add

def test_add():
    assert add(2,3)==5 ,"This test will fail because the add function is currently subtracting instead of adding."

if __name__=="__main__":
    try:
        test_add()
        print(f"test is passed successfully: 2+3 returns {add(2,3)}")
    except AssertionError as e: # Catches the exception if assert fails
        print(f"test failed: {e}   ")
    
from calculator import Calculator

def test_add():
    calc=Calculator()
    assert calc.add(2,3)==5,"This test will fail because the add function is currently subtracting instead of adding."

if __name__=="__main__":
    try:
        test_add()
        print(f"test is passed successfully: 2+3 returns {Calculator().add(2,3)}")
    except AssertionError as e:
        print(f"test failed: {e}")

def test_divide():
    calc1=Calculator()
    assert calc1.divide(10,2)==5.0, "This test will fail because the divide function is currently multiplying instead of dividing."

if __name__=="__main__":
    try:
        test_divide()
        print(f"test is passed successfully: 10/2 returns {Calculator().divide(10,2)}")

    except AssertionError as e:
        print(f"test failed: {e}")