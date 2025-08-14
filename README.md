#  Unit Testing and TDD with Python

This project was developed as part of the **Unit Testing and Test-Driven Development (TDD) with Python** course by Alura. It demonstrates how to build reliable and maintainable Python applications using **pytest**, **TDD**, and clean testing practices.

##  Overview

The goal of this project is to apply automated testing to a Python application using the **pytest** framework and the principles of **Test-Driven Development**. It includes:
- Isolated unit tests
- Reusable fixtures
- Coverage reports
- Refactored code following the red-green-refactor cycle

##  Technologies Used

- Python 3.13
- Pytest
- Pytest-cov
- TDD methodology

##  Project Structure

```
├── codigo/               # Application source code
│   └── bytebank.py       # Main business logic
├── tests/                # Unit tests
│   └── test_bytebank.py  # Test cases
├── pytest.ini            # Pytest configuration
├── .coveragerc           # Coverage configuration
└── README.md             # Project documentation
```

##  Running Tests

To run the tests and view coverage:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=codigo tests/ --cov-report term-missing
```

##  Features Tested

- Age calculation based on birth date
- Last name extraction from full name
- Salary reduction logic for specific surnames
- String representation of employee objects
- Bonus calculation logic
- Use of fixtures to isolate test scenarios

##  Coverage

Test coverage is tracked using `pytest-cov`. The goal is to maintain **100% coverage** across all business logic.

##  What I Learned

- Writing clean and maintainable unit tests
- Applying TDD in real-world scenarios
- Using fixtures to reduce duplication
- Refactoring code safely with test coverage
- Configuring pytest and coverage tools

##  Contributing

Feel free to fork this repository, open issues, or submit pull requests to improve the project.

##  License

This project is licensed under the [MIT License](LICENSE).

