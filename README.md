# Awesome Python TDD

A curated list of awesome Python Test-Driven Development (TDD) resources, libraries, tools, and best practices.

## Contents

- [Testing Frameworks](#testing-frameworks)
- [Mocking and Fixtures](#mocking-and-fixtures)
- [Property-Based Testing](#property-based-testing)
- [Coverage Tools](#coverage-tools)
- [Test Runners and Automation](#test-runners-and-automation)
- [Behavior-Driven Development (BDD)](#behavior-driven-development-bdd)
- [Mutation Testing](#mutation-testing)
- [Web Testing](#web-testing)
- [API Testing](#api-testing)
- [Performance Testing](#performance-testing)
- [Continuous Integration](#continuous-integration)
- [Books and Learning Resources](#books-and-learning-resources)
- [Best Practices](#best-practices)

## Testing Frameworks

**Core Testing Libraries**

- **pytest** - The most popular Python testing framework with powerful fixtures, parametrization, and plugin ecosystem
  - Supports fixtures for setup/teardown
  - Parametrized testing for multiple test cases
  - Rich plugin architecture
  - Better assertion introspection than unittest

- **unittest** - Python's built-in testing framework (xUnit style)
  - Part of standard library (no installation needed)
  - Class-based test organization
  - setUp/tearDown methods for test fixtures
  - Compatible with pytest

- **nose2** - Successor to nose, extends unittest with plugins
  - Test discovery and execution
  - Plugin-based architecture
  - Backward compatible with nose

- **doctest** - Tests embedded in docstrings
  - Ensures documentation examples work
  - Simple syntax for basic tests
  - Great for documentation-driven development

## Mocking and Fixtures

**Mocking Libraries**

- **unittest.mock** - Built-in mocking library (Python 3.3+)
  - Mock objects and patch decorators
  - Spec-based mocking for type safety
  - Call assertions and side effects

- **pytest-mock** - Thin wrapper around unittest.mock for pytest
  - Cleaner fixture-based mocking
  - Automatic cleanup
  - Better integration with pytest

- **responses** - Mock HTTP requests library
  - Mock requests library calls
  - Perfect for API testing
  - Pattern matching for URLs

- **freezegun** - Mock datetime and time
  - Freeze time for consistent testing
  - Travel through time in tests
  - Works with multiple date/time libraries

- **faker** - Generate fake data for testing
  - Realistic test data generation
  - Multiple locales supported
  - Extensible providers

**Fixture Management**

- **pytest-fixtures** - Collection of useful pytest fixtures
- **factory_boy** - Fixtures replacement based on thoughtbot's factory_girl
- **model_bakery** - Smart object creation for Django tests
- **pytest-factoryboy** - Integration of factory_boy with pytest

## Property-Based Testing

- **Hypothesis** - Generate test cases based on properties
  - Automatic test case generation
  - Shrinking to find minimal failing examples
  - Stateful testing support
  - Database of previously found bugs

- **pytest-hypothesis** - Hypothesis integration for pytest
- **schemathesis** - Property-based testing for web APIs

## Coverage Tools

- **coverage.py** - Code coverage measurement for Python
  - Line and branch coverage
  - HTML/XML/JSON reports
  - Integration with CI systems

- **pytest-cov** - Coverage plugin for pytest
  - Seamless pytest integration
  - Parallel test support
  - Fail under threshold option

- **codecov** - Cloud-based coverage reporting
- **coveralls** - Coverage history and statistics

## Test Runners and Automation

- **tox** - Automated testing in multiple environments
  - Test against multiple Python versions
  - Isolated virtual environments
  - Configuration-driven testing

- **nox** - Python-based alternative to tox
  - Python code for configuration
  - More flexible than tox
  - Session-based testing

- **pytest-xdist** - Parallel test execution for pytest
  - Distribute tests across CPUs
  - Remote test execution
  - Load balancing

- **green** - Clean, colorful test runner
- **ward** - Modern Python test framework with descriptive syntax

## Behavior-Driven Development (BDD)

- **behave** - BDD framework using Gherkin syntax
  - Natural language test scenarios
  - Step definitions in Python
  - Good for stakeholder communication

- **pytest-bdd** - BDD plugin for pytest
  - Gherkin feature files
  - Pytest fixture integration
  - Step reuse across scenarios

- **lettuce** - Cucumber-inspired BDD framework
- **radish** - BDD framework with extensible step definitions

## Mutation Testing

- **mutmut** - Mutation testing system
  - Automated mutation generation
  - Measures test suite quality
  - Integration with pytest/unittest

- **cosmic-ray** - Mutation testing tool
  - Multiple mutation operators
  - Distributed execution support

## Web Testing

**Browser Automation**

- **Selenium** - Browser automation framework
  - Multiple browser support
  - WebDriver protocol
  - Headless testing support

- **Playwright** - Modern browser automation
  - Fast and reliable
  - Multiple browser engines
  - Auto-wait features

- **Cypress** (via pytest-cypress) - Fast web testing
- **Splinter** - High-level browser automation wrapper

**Web Framework Testing**

- **pytest-django** - Django testing with pytest
  - Database fixtures
  - Client fixture for requests
  - Live server support

- **pytest-flask** - Flask testing with pytest
  - Application fixtures
  - Client for making requests

- **WebTest** - WSGI application testing
  - Test any WSGI application
  - Form filling helpers
  - Cookie handling

## API Testing

- **requests-mock** - Mock requests library responses
- **pytest-httpserver** - HTTP server fixture for pytest
- **tavern** - Automated REST API testing
- **gabbi** - Declarative HTTP testing
- **pact-python** - Consumer-driven contract testing
- **vcr.py** - Record and replay HTTP interactions

## Performance Testing

- **locust** - Load testing framework
  - Python-based scenarios
  - Distributed load generation
  - Web UI for monitoring

- **pytest-benchmark** - Benchmark testing for pytest
  - Statistical analysis
  - Comparison between runs
  - Performance regression detection

- **pytest-timeout** - Test timeout management
- **pytest-profiling** - Profile test execution

## Continuous Integration

**CI/CD Integration Tools**

- **pytest-ci** - CI-specific pytest plugins
- **pytest-github-actions-annotate-failures** - GitHub Actions integration
- **pytest-azurepipelines** - Azure Pipelines reporting
- **pytest-circleci-parallelized** - CircleCI parallel testing

**Quality Assurance**

- **pylint** - Code analysis and linting
- **flake8** - Style guide enforcement
- **mypy** - Static type checking
- **black** - Code formatting
- **isort** - Import sorting
- **bandit** - Security issue detection

## Books and Learning Resources

**Books**

- "Test Driven Development with Python" by Harry Percival
- "Python Testing with pytest" by Brian Okken
- "Test-Driven Development: By Example" by Kent Beck
- "Growing Object-Oriented Software, Guided by Tests" by Freeman & Pryce

**Online Resources**

- pytest documentation (docs.pytest.org)
- Real Python testing tutorials
- TestDriven.io courses
- Full Stack Python - Testing chapter

**Video Courses**

- Talk Python Training - Testing courses
- Pluralsight Python testing paths
- Test & Code podcast by Brian Okken

## Best Practices

### TDD Cycle (Red-Green-Refactor)

1. **Red** - Write a failing test
2. **Green** - Write minimal code to pass
3. **Refactor** - Improve code while keeping tests green

### Test Organization

- **Arrange-Act-Assert (AAA)** pattern
  - Arrange: Set up test data and conditions
  - Act: Execute the code being tested
  - Assert: Verify the results

- **Given-When-Then** (BDD style)
  - Given: Initial context
  - When: Event occurs
  - Then: Expected outcome

### Testing Principles

- **FIRST** principles
  - Fast: Tests should run quickly
  - Independent: Tests shouldn't depend on each other
  - Repeatable: Same results every time
  - Self-validating: Pass or fail, no manual inspection
  - Timely: Write tests at the right time (before code in TDD)

- **Test Pyramid**
  - Many unit tests (fast, isolated)
  - Fewer integration tests (moderate speed)
  - Few end-to-end tests (slow, comprehensive)

### Naming Conventions

- `test_<feature>_<scenario>_<expected_outcome>`
- `test_should_<expected_behavior>_when_<condition>`
- Use descriptive names that explain what's being tested

### Fixture Best Practices

- Keep fixtures small and focused
- Use fixture parametrization for variations
- Prefer composition over complex fixtures
- Use `conftest.py` for shared fixtures

### Common Patterns

- **Dummy** - Objects passed but never used
- **Stub** - Provides predefined answers
- **Spy** - Records information about calls
- **Mock** - Pre-programmed expectations
- **Fake** - Working implementation but simplified

### Code Coverage Goals

- Aim for 80%+ coverage but focus on quality
- 100% coverage doesn't guarantee bug-free code
- Cover edge cases and error conditions
- Use mutation testing to verify test quality

### Test Data Management

- Use factories for object creation
- Separate test data from test logic
- Use fixtures for common test data
- Consider database fixtures for integration tests

### Continuous Testing

- Run tests on every commit
- Use pre-commit hooks for fast tests
- Implement parallel test execution
- Monitor test execution time
- Set up coverage thresholds in CI

---

## Contributing

Contributions welcome! Please read the contribution guidelines first.

## License

CC0 - Public Domain
