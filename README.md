# Test-Driven Development with Python

A comprehensive guide to Test-Driven Development (TDD) using Python's testing frameworks and tools.

## Table of Contents
- [Introduction to TDD](#introduction-to-tdd)
- [unittest - Python's Built-in Testing Framework](#unittest)
- [nose - Extended Testing Framework](#nose)
- [nose-cov - Coverage Plugin for nose](#nose-cov)
- [rednose - Colored Test Output](#rednose)
- [pytest - Modern Testing Framework](#pytest)

## Introduction to TDD

Test-Driven Development is a software development approach where tests are written before the actual code. The TDD cycle follows three simple steps:

1. **Red** - Write a failing test that defines a desired improvement or new function
2. **Green** - Write the minimum amount of code to make the test pass
3. **Refactor** - Clean up the code while ensuring tests still pass

### Benefits of TDD
- Catches bugs early in development
- Encourages modular, maintainable code
- Serves as living documentation
- Increases confidence when refactoring
- Reduces debugging time

## unittest

Python's built-in testing framework, inspired by JUnit. It comes standard with Python, requiring no additional installation.

### Basic Usage

```python
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Runs before each test method"""
        self.calc = Calculator()
    
    def tearDown(self):
        """Runs after each test method"""
        pass
    
    def test_addition(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Common Assertions
- `assertEqual(a, b)` - Check if a == b
- `assertTrue(x)` - Check if x is True
- `assertFalse(x)` - Check if x is False
- `assertRaises(Exception)` - Check if exception is raised
- `assertIn(a, b)` - Check if a is in b
- `assertIsNone(x)` - Check if x is None

### Running Tests
```bash
# Run a single test file
python -m unittest test_module.py

# Run with verbose output
python -m unittest -v test_module.py

# Auto-discover and run all tests
python -m unittest discover
```

### Key Features
- Object-oriented approach using test classes
- Test fixtures with setUp and tearDown methods
- Test discovery mechanism
- Rich assertion methods
- Test suites for grouping tests

## nose

An extension of unittest that makes testing easier. While nose is now in maintenance mode (last release in 2015), it introduced many features that influenced modern testing tools.

### Installation
```bash
pip install nose
```

### Basic Usage

Nose can run unittest tests and its own tests. It automatically discovers tests without requiring `unittest.main()`:

```python
# test_math.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

class TestMultiplication:
    def test_positive(self):
        assert 2 * 3 == 6
    
    def test_negative(self):
        assert -2 * 3 == -6
```

### Running Tests
```bash
# Run all tests in current directory
nosetests

# Run specific test file
nosetests test_math.py

# Run with verbose output
nosetests -v

# Run tests matching a pattern
nosetests -m "test_add.*"
```

### Key Features
- Automatic test discovery (finds tests without explicit test suites)
- Supports unittest, doctest, and simple assert statements
- Plugin architecture for extensibility
- Generates XML output for CI integration
- Multiprocess test execution

### Configuration
Create a `setup.cfg` or `.noserc` file:

```ini
[nosetests]
verbosity=2
with-doctest=1
doctest-extension=.txt
```

## nose-cov

A coverage plugin for nose that measures code coverage during test execution. It's built on top of the coverage.py library.

### Installation
```bash
pip install nose-cov
```

### Basic Usage

```bash
# Run tests with coverage
nosetests --with-cov

# Specify modules to cover
nosetests --with-cov --cov=mypackage

# Generate HTML coverage report
nosetests --with-cov --cov-report=html

# Set minimum coverage threshold
nosetests --with-cov --cov=mypackage --cov-fail-under=80
```

### Coverage Report Types
- `term` - Terminal output (default)
- `html` - HTML report in htmlcov/ directory
- `xml` - XML report for CI tools
- `annotate` - Annotated source files

### Configuration Example
```ini
[nosetests]
with-cov=1
cov=mypackage
cov-report=term-missing
cov-report=html
```

### Understanding Coverage
- **Statements** - Lines of code executed
- **Branches** - Decision paths taken (if/else)
- **Missing** - Lines not covered by tests

A typical report shows:
```
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
mypackage/__init__.py    10      2    80%   15-16
mypackage/core.py        45      5    89%   23, 67-70
--------------------------------------------------
TOTAL                    55      7    87%
```

## rednose

A colorized test output plugin for nose that makes test results more readable with colored output and real-time feedback.

### Installation
```bash
pip install rednose
```

### Basic Usage

```bash
# Run with colored output
nosetests --rednose

# Combine with other options
nosetests --rednose -v

# Force color output (useful for CI)
nosetests --rednose --force-color
```

### Configuration
Add to `setup.cfg`:
```ini
[nosetests]
rednose=1
```

### Features
- **Green** - Passing tests
- **Red** - Failing tests
- **Yellow** - Errors and skipped tests
- Progress bar showing test completion
- Clear failure messages with context
- Real-time output as tests run

### Visual Improvements
Rednose transforms boring test output into an engaging, easy-to-scan format that helps developers quickly identify issues. It shows a progress indicator, groups failures clearly, and uses color psychology to make test results intuitive at a glance.

## pytest

The modern, feature-rich testing framework that has become the de facto standard for Python testing. It offers powerful features while remaining simple to use.

### Installation
```bash
pip install pytest
pip install pytest-cov  # For coverage
```

### Basic Usage

Pytest uses simple assert statements instead of special assertion methods:

```python
# test_calculator.py
import pytest

def test_addition():
    assert 2 + 2 == 4

def test_division():
    assert 10 / 2 == 5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition_parametrized(a, b, expected):
    assert a + b == expected
```

### Fixtures

Fixtures provide a way to set up test dependencies and share code across tests:

```python
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def database():
    db = Database()
    db.connect()
    yield db
    db.disconnect()

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_database_query(database):
    result = database.query("SELECT * FROM users")
    assert len(result) > 0
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific file
pytest test_calculator.py

# Run specific test
pytest test_calculator.py::test_addition

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=mypackage

# Run only failed tests from last run
pytest --lf

# Run tests matching pattern
pytest -k "addition"

# Stop after first failure
pytest -x

# Show local variables in tracebacks
pytest -l
```

### Markers

Organize and selectively run tests using markers:

```python
@pytest.mark.slow
def test_complex_calculation():
    # Long-running test
    pass

@pytest.mark.integration
def test_api_endpoint():
    # Integration test
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.xfail
def test_known_bug():
    # Test expected to fail
    pass
```

Run specific marked tests:
```bash
pytest -m slow
pytest -m "not slow"
pytest -m "integration and not slow"
```

### Configuration

Create a `pytest.ini` file:
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
addopts = -v --tb=short
```

Or use `pyproject.toml`:
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov=mypackage"
```

### Key Features

- **Simple syntax** - Uses plain assert statements with intelligent introspection
- **Fixtures** - Powerful dependency injection system
- **Parametrization** - Run tests with multiple input sets
- **Plugins** - Rich ecosystem (pytest-django, pytest-asyncio, pytest-mock, etc.)
- **Detailed failure reports** - Shows context and variable values
- **Test discovery** - Automatically finds tests following conventions
- **Parallel execution** - Use pytest-xdist for faster test runs
- **Mocking** - Integrates well with unittest.mock and pytest-mock

### Advanced Features

**Parametrize with fixtures:**
```python
@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_square(number):
    assert number ** 2 > 0
```

**Custom fixtures with scope:**
```python
@pytest.fixture(scope="session")
def expensive_resource():
    # Created once per test session
    return setup_resource()

@pytest.fixture(scope="module")
def shared_data():
    # Created once per test module
    return load_data()
```

**Monkeypatching:**
```python
def test_api_call(monkeypatch):
    def mock_get(*args, **kwargs):
        return {"status": "success"}
    
    monkeypatch.setattr("requests.get", mock_get)
    result = my_api_function()
    assert result["status"] == "success"
```

## Comparison and Recommendations

### When to Use Each Tool

**unittest** - Use when:
- Working on projects requiring no external dependencies
- You prefer object-oriented test structure
- Need compatibility with older Python codebases

**nose** - Generally avoided now:
- Deprecated in favor of pytest
- Only use if maintaining legacy projects

**pytest** - Recommended for most projects:
- Modern syntax and features
- Extensive plugin ecosystem
- Better error messages and debugging
- Actively maintained

Great! I'll help you get started with **nose2**, the Python testing framework.

## Installing nose2

First, install nose2 via pip:

```bash
pip install nose2
```

## Basic Test Structure

nose2 automatically discovers and runs tests. Here's a simple example:## Running Tests

Run your tests with:

```bash
# Run all tests in current directory
nose2

# Run with verbose output
nose2 -v

# Run specific test file
nose2 test_calculator

# Run specific test class
nose2 test_calculator.TestCalculator

# Run specific test method
nose2 test_calculator.TestCalculator.test_addition
```

## Configuration File

Create a `unittest.cfg` or `nose2.cfg` file for configuration:## Key Features

**Test Discovery:** nose2 finds tests based on naming patterns:
- Test files: `test*.py` or `*_test.py`
- Test classes: classes that inherit from `unittest.TestCase`
- Test functions: functions starting with `test_`
- Test methods: methods starting with `test_`

**Useful Plugins:**
- `nose2.plugins.coverage` - Code coverage
- `nose2.plugins.mp` - Multiprocess testing
- `nose2.plugins.junitxml` - JUnit XML output


### Migration Path

If moving from unittest to pytest:
1. Pytest can run unittest tests without modification
2. Gradually refactor to use pytest fixtures and features
3. Take advantage of parametrization for data-driven tests
4. Use pytest plugins to enhance functionality

### Best Practices for TDD

1. **Write tests first** - Define behavior before implementation
2. **Keep tests small** - Each test should verify one thing
3. **Use descriptive names** - Test names should describe what they verify
4. **Aim for high coverage** - Strive for 80%+ coverage, but don't obsess over 100%
5. **Test edge cases** - Include boundary conditions and error scenarios
6. **Keep tests fast** - Slow tests discourage running them frequently
7. **Make tests independent** - Tests should not depend on each other
8. **Use fixtures wisely** - Share setup code without creating tight coupling
