# bingeTest

A simple, lightweight batch testing framework for Python that allows you to run multiple test cases in sequence and get comprehensive results.

## Features

- Simple and intuitive API
- Built-in assertion methods
- Clear test results with pass/fail indicators
- Summary statistics
- No external dependencies

## Usage

### Basic Example

```python
from bingetest import BingeTest

# Create a test suite
suite = BingeTest("My Test Suite")

# Define test functions
def test_addition():
    suite.assert_equal(2 + 2, 4, "Basic addition should work")

def test_string():
    suite.assert_equal("Hello" + " World", "Hello World")

# Add tests to the suite
suite.add_test("Addition Test", test_addition)
suite.add_test("String Test", test_string)

# Run all tests
exit_code = suite.run()
```

### Running the Examples

Run the built-in example:
```bash
python3 bingetest.py
```

Run additional examples:
```bash
python3 examples.py
```

## Assertion Methods

- `assert_equal(actual, expected, message)` - Assert two values are equal
- `assert_true(condition, message)` - Assert a condition is true
- `assert_false(condition, message)` - Assert a condition is false

## Output

BingeTest provides clear, formatted output:
- ✓ for passed tests
- ✗ for failed tests
- Detailed summary with pass/fail counts and success rate

## Requirements

- Python 3.6 or higher
- No external dependencies
