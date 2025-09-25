import pytest
import subprocess
# Functions to test
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fourth_power(n):   
    return n ** 4       

def fifth_power(n):
    return n ** 5   

# Tests for Square function
def test_square():
    assert square(2) == 4, "Test Failed: 2 squared should be 4"
    assert square(3) == 9, "Test Failed: 3 squared should be 9"
    assert square(4) == 16, "Test Failed: 4 squared should be 16"
    assert square(5) == 25, "Test Failed: 5 squared should be 25"
    
# Tests for Cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: 2 cubed should be 8"
    assert cube(3) == 27, "Test Failed: 3 cubed should be 27"
    assert cube(4) == 64, "Test Failed: 4 cubed should be 64"
    assert cube(5) == 125, "Test Failed: 5 cubed should be 125"
    
# Tests for Fourth Power function
def test_fourth_power():
    assert fourth_power(2) == 16, "Test Failed: 2 to the power of 4 should be 16"
    assert fourth_power(3) == 81, "Test Failed: 3 to the power of 4 should be 81"
    assert fourth_power(4) == 256, "Test Failed: 4 to the power of 4 should be 256"
    assert fourth_power(5) == 625, "Test Failed: 5 to the power of 4 should be 625"

# Tests for Fifth Power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: 2 to the power of 5 should be 32"
    assert fifth_power(3) == 243, "Test Failed: 3 to the power of 5 should be 243"
    assert fifth_power(4) == 1024, "Test Failed: 4 to the power of 5 should be 1024"
    assert fifth_power(5) == 3125, "Test Failed: 5 to the power of 5 should be 3125"

# Tests for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
        
    with pytest.raises(TypeError):
        cube("string") 
        
    with pytest.raises(TypeError):
        fourth_power("string") 
        
    with pytest.raises(TypeError):
        fifth_power("string")





# --- Flake8 Test ---
def test_flake8():
    """Check code style using flake8"""
    result = subprocess.run(
        ["flake8", "--max-line-length=100", "."],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Flake8 issues found:\n{result.stdout}")


# --- Pylint Test ---
def test_pylint():
    """Check code style using pylint"""
    result = subprocess.run(
        ["pylint", "--disable=R,C", "."],  # disabling Refactor & Convention to focus on errors/warnings
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Pylint issues found:\n{result.stdout}")


# --- Black Test ---
def test_black_formatting():
    """Check formatting with Black"""
    result = subprocess.run(
        ["black", "--check", "."],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        pytest.fail(f"Black formatting issues found:\n{result.stdout}")
