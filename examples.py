# Example test cases for BingeTest

from bingetest import BingeTest


def run_examples():
    """Run example test cases"""
    suite = BingeTest("Math and String Tests")
    
    # Math tests
    def test_multiplication():
        suite.assert_equal(3 * 4, 12, "Multiplication should work")
    
    def test_division():
        suite.assert_equal(10 / 2, 5, "Division should work")
    
    def test_subtraction():
        suite.assert_equal(10 - 3, 7, "Subtraction should work")
    
    # String tests
    def test_uppercase():
        suite.assert_equal("hello".upper(), "HELLO", "Uppercase conversion")
    
    def test_lowercase():
        suite.assert_equal("WORLD".lower(), "world", "Lowercase conversion")
    
    def test_string_contains():
        suite.assert_true("test" in "bingetest", "String should contain 'test'")
    
    # Add all tests
    suite.add_test("Multiplication", test_multiplication)
    suite.add_test("Division", test_division)
    suite.add_test("Subtraction", test_subtraction)
    suite.add_test("Uppercase", test_uppercase)
    suite.add_test("Lowercase", test_lowercase)
    suite.add_test("String Contains", test_string_contains)
    
    return suite.run()


if __name__ == "__main__":
    import sys
    sys.exit(run_examples())
