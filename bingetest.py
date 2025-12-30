#!/usr/bin/env python3
"""
BingeTest - A simple batch testing framework
Run multiple test cases in sequence and report results
"""

import sys
from typing import List, Callable, Tuple


class BingeTest:
    """Main test runner for batch/binge testing"""
    
    def __init__(self, name: str = "BingeTest Suite"):
        self.name = name
        self.tests: List[Tuple[str, Callable]] = []
        self.passed = 0
        self.failed = 0
        self.results = []
    
    def add_test(self, name: str, test_func: Callable) -> None:
        """Add a test case to the suite"""
        self.tests.append((name, test_func))
    
    def assert_equal(self, actual, expected, message: str = ""):
        """Assert that two values are equal"""
        if actual != expected:
            msg = message or f"Expected {expected}, got {actual}"
            raise AssertionError(msg)
    
    def assert_true(self, condition: bool, message: str = ""):
        """Assert that a condition is true"""
        if not condition:
            msg = message or "Condition was false"
            raise AssertionError(msg)
    
    def assert_false(self, condition: bool, message: str = ""):
        """Assert that a condition is false"""
        if condition:
            msg = message or "Condition was true"
            raise AssertionError(msg)
    
    def run(self) -> int:
        """Run all tests and return exit code (0 for success, 1 for failures)"""
        print(f"\n{'='*60}")
        print(f"Running {self.name}")
        print(f"{'='*60}\n")
        
        for test_name, test_func in self.tests:
            try:
                print(f"Running: {test_name}...", end=" ")
                test_func()
                print("✓ PASSED")
                self.passed += 1
                self.results.append((test_name, "PASSED", None))
            except AssertionError as e:
                print(f"✗ FAILED")
                print(f"  Error: {str(e)}")
                self.failed += 1
                self.results.append((test_name, "FAILED", str(e)))
            except Exception as e:
                print(f"✗ ERROR")
                print(f"  Error: {str(e)}")
                self.failed += 1
                self.results.append((test_name, "ERROR", str(e)))
        
        self._print_summary()
        
        return 0 if self.failed == 0 else 1
    
    def _print_summary(self) -> None:
        """Print test results summary"""
        print(f"\n{'='*60}")
        print(f"Test Summary")
        print(f"{'='*60}")
        print(f"Total tests: {len(self.tests)}")
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        if len(self.tests) > 0:
            print(f"Success rate: {(self.passed / len(self.tests) * 100):.1f}%")
        else:
            print(f"Success rate: N/A (no tests run)")
        print(f"{'='*60}\n")


def main():
    """Example usage of BingeTest"""
    suite = BingeTest("Example Test Suite")
    
    # Example test cases
    def test_addition():
        suite.assert_equal(2 + 2, 4, "Basic addition should work")
    
    def test_string_concatenation():
        suite.assert_equal("Hello" + " " + "World", "Hello World")
    
    def test_list_length():
        suite.assert_equal(len([1, 2, 3]), 3)
    
    def test_boolean_true():
        suite.assert_true(True, "True should be true")
    
    def test_boolean_false():
        suite.assert_false(False, "False should be false")
    
    # Add tests to suite
    suite.add_test("Addition Test", test_addition)
    suite.add_test("String Concatenation Test", test_string_concatenation)
    suite.add_test("List Length Test", test_list_length)
    suite.add_test("Boolean True Test", test_boolean_true)
    suite.add_test("Boolean False Test", test_boolean_false)
    
    # Run tests
    exit_code = suite.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
