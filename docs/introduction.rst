=====================================================
Test-Driven Development with Python
=====================================================

A Comprehensive Guide to Building Robust Applications
======================================================

.. contents:: Table of Contents
   :depth: 3

----

PART I: FOUNDATIONS OF TEST-DRIVEN DEVELOPMENT
===============================================

Chapter 1: Introduction to Test-Driven Development
---------------------------------------------------

* What is Test-Driven Development?
* The TDD Cycle: Red-Green-Refactor
* Benefits and Challenges of TDD
* TDD vs. Traditional Testing Approaches
* When to Use TDD (and When Not To)
* Setting Up Your Python Testing Environment

Chapter 2: Python Testing Fundamentals
---------------------------------------

Overview of Python Testing Ecosystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

unittest: Python's Built-in Testing Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Test Cases and Test Suites
* setUp and tearDown Methods
* Assertions and Test Discovery
* Test Organization and Structure

Introduction to pytest
~~~~~~~~~~~~~~~~~~~~~~

* Why pytest?
* Basic Test Structure
* Running Tests with pytest
* pytest vs unittest: A Comparison

Your First TDD Example: Building a Calculator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter 3: Advanced pytest Features
------------------------------------

Fixtures: Setup and Teardown Done Right
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Function, Class, Module, and Session Scopes
* Fixture Composition and Dependencies
* conftest.py and Fixture Sharing

Parametrized Testing
~~~~~~~~~~~~~~~~~~~~

* @pytest.mark.parametrize
* Parametrizing Fixtures
* Dynamic Test Generation

Markers and Custom Markers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Built-in Markers (skip, xfail, slow)
* Creating Custom Markers
* Marker-Based Test Selection

pytest Configuration
~~~~~~~~~~~~~~~~~~~~

* pytest.ini and pyproject.toml
* Command-Line Options
* Plugins and Extensions

Chapter 4: Test Design and Best Practices
------------------------------------------

The Test Pyramid
~~~~~~~~~~~~~~~~

* Unit Tests
* Integration Tests
* End-to-End Tests
* Balancing Your Test Suite

Test Naming Conventions
~~~~~~~~~~~~~~~~~~~~~~~

The AAA Pattern (Arrange-Act-Assert)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Given-When-Then Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FIRST Principles of Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fast, Independent, Repeatable, Self-Validating, Timely

Writing Maintainable Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Smells and Anti-Patterns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code Coverage: Metrics and Interpretation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

----

PART II: DERIVING AND DESIGNING TEST CASES
===========================================

Chapter 5: Test Case Design Techniques
---------------------------------------

* Equivalence Partitioning
* Boundary Value Analysis
* Decision Table Testing
* State Transition Testing
* Use Case Testing
* Error Guessing and Experience-Based Testing
* Combining Techniques for Comprehensive Coverage

Chapter 6: Testing Strategies for Different Scenarios
------------------------------------------------------

* Testing Pure Functions
* Testing Classes and Object-Oriented Code
* Testing Functions with Side Effects

Testing Asynchronous Code
~~~~~~~~~~~~~~~~~~~~~~~~~~

* async/await Testing
* pytest-asyncio

Additional Testing Strategies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Testing Exceptions and Error Handling
* Testing Edge Cases and Corner Cases
* Testing for Performance and Scalability

Chapter 7: Property-Based Testing with Hypothesis
--------------------------------------------------

* Introduction to Property-Based Testing
* Installing and Setting Up Hypothesis
* Writing Property-Based Tests
* Strategies for Test Data Generation
* Stateful Testing
* Shrinking: Finding Minimal Failing Cases
* Hypothesis with pytest Integration
* Real-World Property-Based Testing Examples

----

PART III: MOCKING AND TEST DOUBLES
===================================

Chapter 8: Understanding Test Doubles
--------------------------------------

Types of Test Doubles
~~~~~~~~~~~~~~~~~~~~~

* Dummy Objects
* Stubs
* Spies
* Mocks
* Fakes

When to Use Each Type
~~~~~~~~~~~~~~~~~~~~~

The Dependency Inversion Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter 9: Mocking with unittest.mock
--------------------------------------

The Mock Object
~~~~~~~~~~~~~~~

Creating Mocks and MagicMocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

patch, patch.object, and patch.dict
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Decorators vs Context Managers
* Where to Patch

Mock Specifications and Auto-Speccing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Asserting Mock Calls
~~~~~~~~~~~~~~~~~~~~

* assert_called_with
* assert_called_once_with
* call_args and call_args_list

Side Effects and Return Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mock Properties and Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter 10: Advanced Mocking Techniques
----------------------------------------

* pytest-mock Plugin
* Mocking File I/O Operations
* Mocking Database Connections
* Mocking HTTP Requests with responses
* Mocking Time and Dates with freezegun
* Mocking Environment Variables
* Mocking External APIs

Best Practices for Mocking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Don't Over-Mock
* Mock at the Right Level
* Verify Mock Interactions

Chapter 11: Fixtures and Test Data Management
----------------------------------------------

* Creating Test Data with Factories
* factory_boy: Advanced Fixture Replacement
* Faker: Generating Realistic Test Data
* Managing Test Databases
* Fixture Parametrization
* Shared Fixtures and Fixture Scoping
* Fixture Finalization and Cleanup

----

PART IV: TESTING PYTHON PACKAGES AND MODULES
=============================================

Chapter 12: Structuring Testable Python Projects
-------------------------------------------------

* Project Structure Best Practices
* Separating Tests from Source Code
* The src Layout vs Flat Layout

Making Your Code Testable
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dependency Injection
* Interface Segregation
* Loose Coupling

Additional Topics
~~~~~~~~~~~~~~~~~

* Testing Private Methods and Internal APIs
* Testing Module-Level Code

Chapter 13: Testing Python Packages
------------------------------------

* Setting Up Package Tests
* Testing Package Installation
* Testing Entry Points and CLI Tools
* Testing Package Imports
* Testing Across Python Versions with tox
* Testing with Different Dependencies
* nox: Flexible Test Automation

Continuous Integration for Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* GitHub Actions
* GitLab CI
* CircleCI
* Travis CI

Chapter 14: Code Coverage and Quality Metrics
----------------------------------------------

* Introduction to Code Coverage
* coverage.py: Measuring Coverage
* pytest-cov Integration
* Branch Coverage vs Line Coverage
* Coverage Reports and Visualization
* Setting Coverage Thresholds
* Mutation Testing with mutmut
* Measuring Test Quality Beyond Coverage

Static Analysis and Linting in Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* pylint
* flake8
* mypy for Type Checking Tests

----

PART V: WEB FRAMEWORK TESTING
==============================

Chapter 15: Testing Django Applications
----------------------------------------

* Django Testing Overview
* Django's TestCase vs pytest-django
* Setting Up pytest-django

Testing Django Models
~~~~~~~~~~~~~~~~~~~~~~

* Model Creation and Validation
* Custom Model Methods
* Model Managers and QuerySets

Testing Django Views
~~~~~~~~~~~~~~~~~~~~~

* Function-Based Views
* Class-Based Views
* Testing View Responses

Testing Django Forms
~~~~~~~~~~~~~~~~~~~~~

* Form Validation
* Form Rendering
* Custom Form Logic

Testing Django Templates
~~~~~~~~~~~~~~~~~~~~~~~~~

Testing Django REST Framework APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Testing Serializers
* Testing ViewSets
* Testing Permissions and Authentication

Additional Django Testing Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Django Test Database Management
* Using Fixtures and Factory Boy with Django
* Testing Django Middleware
* Testing Django Management Commands
* Testing Django Signals
* Integration Testing in Django

Chapter 16: Testing Flask Applications
---------------------------------------

* Flask Testing Overview
* Setting Up pytest-flask
* The Flask Test Client
* Testing Flask Routes and Views
* Testing Flask Blueprints
* Testing Flask Request Context
* Testing Flask-SQLAlchemy Models
* Testing Flask Forms with WTForms
* Testing Flask REST APIs

Testing Flask Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~

* Flask-Login
* Flask-JWT-Extended
* Flask-Mail

Additional Flask Testing Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Application Factories and Testing
* Testing Flask Configuration
* Testing Flask Error Handlers
* Mocking in Flask Applications

Chapter 17: Testing FastAPI Applications
-----------------------------------------

* FastAPI Testing Overview
* TestClient and HTTPX
* Setting Up FastAPI Tests with pytest

Testing FastAPI Endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~

* GET, POST, PUT, DELETE Requests
* Query Parameters and Path Parameters
* Request Bodies and Validation

Testing Pydantic Models
~~~~~~~~~~~~~~~~~~~~~~~~

Testing Dependency Injection in FastAPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Testing FastAPI Middleware
* Testing WebSocket Endpoints
* Testing Background Tasks

Testing FastAPI Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* OAuth2 Testing
* JWT Token Testing

Async Testing with FastAPI
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Testing Database Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* SQLAlchemy with FastAPI
* Async Database Testing

Additional FastAPI Testing Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Testing File Uploads
* Integration Testing FastAPI Applications

Chapter 18: Testing Django Ninja API
-------------------------------------

* Introduction to Django Ninja
* Setting Up Django Ninja Tests
* Testing Ninja API Endpoints
* Testing Ninja Schemas

Testing Ninja Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* API Key Authentication
* JWT Authentication

Additional Ninja Testing Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Testing Ninja Routers
* Testing Request/Response Models
* Testing Ninja Pagination
* Testing File Uploads in Ninja
* Error Handling and Validation Testing
* Integration with Django Testing Tools
* Performance Testing Ninja APIs

----

PART VI: SPECIALIZED TESTING TECHNIQUES
========================================

Chapter 19: API Testing
-----------------------

* REST API Testing Principles
* Testing API Contracts
* Testing API Versioning
* Testing API Rate Limiting
* Testing API Caching
* Testing API Error Responses
* Contract Testing with Pact
* API Load Testing with Locust
* Recording and Replaying API Calls with vcr.py
* Testing GraphQL APIs

Chapter 20: Database Testing
-----------------------------

* Database Testing Strategies
* Testing Database Migrations
* Transaction Management in Tests
* Using Test Databases
* In-Memory Databases for Testing
* Testing Raw SQL Queries
* Testing Stored Procedures
* Testing Database Constraints
* Performance Testing Database Queries
* Testing Data Integrity

Chapter 21: Testing Asynchronous Code
--------------------------------------

* Challenges of Testing Async Code
* pytest-asyncio Basics
* Testing Asyncio Coroutines
* Testing Async Context Managers
* Testing Async Generators
* Mocking Async Functions
* Testing Event Loops
* Testing Concurrent Operations
* Testing Async Database Operations
* Testing Async HTTP Requests

Chapter 22: Integration and End-to-End Testing
-----------------------------------------------

* Integration Testing Strategies
* Testing System Integration Points
* Testing Third-Party API Integration
* Docker for Integration Testing
* Testing with Docker Compose
* Browser Automation with Selenium
* Modern Browser Testing with Playwright
* Testing User Flows
* Visual Regression Testing
* Performance Monitoring in E2E Tests

Chapter 23: Security Testing
-----------------------------

* Security Testing Principles
* Testing Authentication and Authorization
* Testing Input Validation
* SQL Injection Testing
* XSS (Cross-Site Scripting) Testing
* CSRF Protection Testing
* Testing Password Security
* Testing Secure Headers
* Dependency Vulnerability Scanning
* Static Application Security Testing (SAST)

Chapter 24: Performance and Load Testing
-----------------------------------------

* Performance Testing Principles
* Benchmarking with pytest-benchmark
* Profiling Test Execution

Load Testing with Locust
~~~~~~~~~~~~~~~~~~~~~~~~~

* Writing Locust Tests
* Distributed Load Testing
* Analyzing Load Test Results

Additional Performance Testing Topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Stress Testing
* Spike Testing
* Endurance Testing
* Performance Regression Testing

----

PART VII: ADVANCED TDD PRACTICES
=================================

Chapter 25: Behavior-Driven Development (BDD)
----------------------------------------------

* Introduction to BDD
* BDD vs TDD
* Writing Gherkin Feature Files

pytest-bdd Framework
~~~~~~~~~~~~~~~~~~~~

* Given-When-Then Steps
* Step Definitions
* Scenario Outlines

Additional BDD Topics
~~~~~~~~~~~~~~~~~~~~~

* behave Framework
* Cucumber-Style Testing
* Collaboration with Non-Technical Stakeholders
* Living Documentation

Chapter 26: Test-Driven Development in Practice
------------------------------------------------

* TDD Workflow and Discipline
* Starting with the Simplest Test
* Triangulation Technique
* Fake It Till You Make It
* Obvious Implementation
* Refactoring Under Test
* Outside-In TDD (London School)
* Inside-Out TDD (Detroit School)
* TDD for Legacy Code
* Test-Driven Bug Fixes
* TDD in Team Environments

Chapter 27: Continuous Integration and Deployment
--------------------------------------------------

* CI/CD Principles
* Setting Up GitHub Actions for Testing
* GitLab CI/CD Configuration
* Testing in Jenkins
* Pre-commit Hooks
* Running Tests in Docker
* Parallel Test Execution
* Test Result Reporting
* Code Coverage in CI
* Quality Gates and Test Thresholds
* Deployment Testing Strategies

Chapter 28: Maintaining Test Suites
------------------------------------

* Test Suite Performance Optimization
* Identifying Slow Tests
* Parallel Test Execution with pytest-xdist
* Test Flakiness and How to Fix It
* Refactoring Tests
* Test Debt Management
* Archiving Obsolete Tests
* Test Documentation
* Test Code Reviews
* Measuring Test ROI

----

PART VIII: REAL-WORLD CASE STUDIES
===================================

Chapter 29: Case Study: Building a Blog Platform with TDD
----------------------------------------------------------

* Requirements and Planning
* Setting Up the Project
* TDD Workflow for User Authentication
* TDD for Blog Post CRUD Operations
* Testing Comment System
* Testing Search Functionality
* Testing User Permissions
* Integration Testing
* Deployment and Production Testing

Chapter 30: Case Study: E-Commerce API with FastAPI
----------------------------------------------------

* System Architecture
* Testing Product Catalog
* Testing Shopping Cart Logic
* Testing Payment Integration
* Testing Order Processing
* Testing Inventory Management
* Testing User Reviews
* Performance Testing for Black Friday
* Security Testing

Chapter 31: Case Study: Microservices Testing
----------------------------------------------

* Microservices Architecture Overview
* Testing Individual Services
* Contract Testing Between Services
* Testing Service Communication
* Testing Event-Driven Architecture
* Testing Service Resilience
* End-to-End Testing Microservices
* Monitoring and Observability

----

PART IX: APPENDICES
====================

Appendix A: Testing Tools Quick Reference
------------------------------------------

* pytest Commands and Options
* unittest Commands and Options
* Common pytest Plugins
* Useful Testing Libraries

Appendix B: Testing Patterns Catalog
-------------------------------------

* Arrange-Act-Assert Template
* Four-Phase Test Template
* Test Data Builders
* Object Mother Pattern
* Test Fixture Patterns

Appendix C: Setting Up Development Environments
------------------------------------------------

* Virtual Environments
* Poetry for Dependency Management
* Docker Development Environments
* VS Code Testing Setup
* PyCharm Testing Configuration

Appendix D: Common Testing Pitfalls
------------------------------------

* Testing Anti-Patterns
* Common Mistakes in TDD
* Mock Abuse
* Overspecification
* Test Interdependencies

Appendix E: Resources and Further Reading
------------------------------------------

* Books on Testing
* Online Courses
* Blogs and Websites
* Conference Talks
* Python Testing Community

----

Index
=====

About the Author
================