# Python Calculator with Docker

A simple command-line calculator implemented in Python and containerized with Docker. This calculator supports basic arithmetic operations and includes comprehensive error handling.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Input validation and error handling
- Docker containerization
- Comprehensive unit tests
- Clean and modular code structure

## Project Structure

```
python-calculator-docker/
├── calculator/
│   ├── __init__.py
│   ├── main.py        # CLI interface
│   ├── operations.py  # Arithmetic operations
│   ├── utils.py       # Input validation
├── tests/
│   ├── test_operations.py
│   ├── test_utils.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Installation

### Local Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd python-calculator-docker
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the calculator:
   ```bash
   python -m calculator.main
   ```

### Docker Installation

1. Build the Docker image:
   ```bash
   docker build -t python-calculator .
   ```

2. Run the calculator in a container:
   ```bash
   docker run --rm -it python-calculator
   ```

## Usage

The calculator provides a simple command-line interface:

1. Enter the first number
2. Choose an operator (+, -, *, /)
3. Enter the second number
4. View the result
5. Enter 'q' at any prompt to quit

Example:
```
Welcome to Python Calculator!
Enter 'q' to quit

Enter first number: 5
Enter operator (+, -, *, /): +
Enter second number: 3

Result: 5 + 3 = 8
```

## Running Tests

Run the test suite using pytest:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- Support for advanced mathematical operations
- GUI interface
- History of calculations
- Scientific calculator features
- Configuration options 