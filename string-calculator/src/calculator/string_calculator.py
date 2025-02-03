import pytest

# Req1: Basic calculator with 2 number limit

# Tests for the StringCalculator class
def test_empty_string():
    calc = StringCalculator()
    assert calc.add("") == 0
    
def test_single_number():
    calc = StringCalculator()
    assert calc.add("20") == 20
    
def test_two_numbers():
    calc = StringCalculator()
    assert calc.add("1,5000") == 5001
    
def test_negative_numbers():
    calc = StringCalculator()
    assert calc.add("4,-3") == 1
    
def test_invalid_numbers():
    calc = StringCalculator()
    assert calc.add("5,tytyt") == 5
    
def test_too_many_numbers():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="More than 2 numbers provided"):
        calc.add("1,2,3")

class StringCalculator:
    def add(self, numbers: str) -> int:
        """
        Add up to two numbers provided in a string format.
        
        Args:
            numbers: String containing up to two numbers separated by comma
            
        Returns:
            Sum of the numbers, with empty or invalid numbers treated as 0
            
        Raises:
            ValueError: If more than 2 numbers are provided
        """
        if not numbers:
            return 0
            
        # Split numbers by comma
        nums = numbers.split(',')
        
        # Check for too many numbers
        if len(nums) > 2:
            raise ValueError("More than 2 numbers provided")
            
        # Convert and sum numbers, treating invalid as 0
        total = 0
        for num in nums:
            try:
                total += int(num)
            except ValueError:
                total += 0
                
        return total

