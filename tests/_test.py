import pytest


#Function to test square
def test_square(n):
    return n ** 2

#Function to test cube
def test_cube(n):
    return n ** 3

#Function to test fourth power
def test_fourth_power(n):   
    return n ** 4       

#Function to test fifth power
def test_fifth_power(n):
    return n ** 5   

#testing the Square function
def test_square():
    assert test_square(2) == 4 ,"Test Failed: 2 squared should be 4"
    assert test_square(3) == 9 ,"Test Failed: 3 squared should be 9"
    assert test_square(4) == 16,"Test Failed: 4 squared should be 16"
    assert test_square(5) == 25,"Test Failed: 5 squared should be 25"
    
#testing the Cube function
def test_cube():
    assert test_cube(2) == 8 ,"Test Failed: 2 cubed should be 8"
    assert test_cube(3) == 27,"Test Failed: 3 cubed should be 27"
    assert test_cube(4) == 64,"Test Failed: 4 cubed should be 64"
    assert test_cube(5) == 125,"Test Failed: 5 cubed should be 125"
    
#testing the Fourth Power function
def test_fourth_power():
    assert test_fourth_power(2) == 16  ,"Test Failed: 2 to the power of 4 should be 16"
    assert test_fourth_power(3) == 81  ,"Test Failed: 3 to the power of 4 should be 81"
    assert test_fourth_power(4) == 256 ,"Test Failed: 4 to the power of 4 should be 256"
    assert test_fourth_power(5) == 625 ,"Test Failed: 5 to the power of 4 should be 625"

#testing the Fifth Power function
def test_fifth_power():
    assert test_fifth_power(2) == 32   ,"Test Failed: 2 to the power of 5 should be 32"
    assert test_fifth_power(3) == 243  ,"Test Failed: 3 to the power of 5 should be 243"
    assert test_fifth_power(4) == 1024 ,"Test Failed: 4 to the power of 5 should be 1024"
    assert test_fifth_power(5) == 3125 ,"Test Failed: 5 to the power of 5 should be 3125"

#Test for invalid input

def test_invalid_input():
    with pytest.raises(TypeError):
        test_square("string")
        
    with pytest.raises(TypeError):
        test_cube("string") 
        
    with pytest.raises(TypeError):
        test_fourth_power("string") 
        
        
    with pytest.raises(TypeError):
        test_fifth_power("string")
        