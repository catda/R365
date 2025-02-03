# String Calculator

A TDD kata implementation of a string calculator that supports various input formats and delimiter styles.

## Features

- Addition of numbers provided as strings
- Support for various delimiter formats:
  - Default delimiters (comma, newline)
  - Custom single-character delimiter: `//{delimiter}\n{numbers}`
  - Custom length delimiter: `//[{delimiter}]\n{numbers}`
  - Multiple delimiters: `//[{delimiter1}][{delimiter2}]...\n{numbers}`
- Numbers greater than 1000 are ignored
- Negative numbers trigger an exception
- Invalid numbers are treated as 0

## Requirements

- Python 3.8+
- pytest

## Installation

```bash
pip install -r requirements.txt
```

## Running Tests

```bash
python -m pytest tests/
```

## Usage

```python
from calculator.string_calculator import StringCalculator

calc = StringCalculator()

# Basic usage
result = calc.add("1,2,3")  # Returns 6

# Using custom delimiter
result = calc.add("//#\n2#5")  # Returns 7

# Using multiple delimiters
result = calc.add("//[*][!!][r9r]\n11r9r22*33!!44")  # Returns 110
```