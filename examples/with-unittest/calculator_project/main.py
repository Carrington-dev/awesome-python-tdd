import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/calculator_tests.log"),
    ]
)

logger = logging.getLogger(__name__)

class Calculator:
    logger.info("Calculator initialized")

    def add(self, a, b):
        if not (isinstance(a, (int, float,)) and isinstance(b, (int, float))):
            logger.error("Addition error: parameters must be numbers")
            raise TypeError("Parameters must be numbers")
        return a + b

    def subtract(self, a, b):
        if not (isinstance(a, (int, float,)) and isinstance(b, (int, float))):
            logger.error("Subtraction error: parameters must be numbers")
            raise TypeError("Parameters must be numbers")
        return a - b

    def multiply(self, a, b):
        if not (isinstance(a, (int, float,)) and isinstance(b, (int, float))):
            logger.error("Multiplication error: parameters must be numbers")
            raise TypeError("Parameters must be numbers")
        return a * b
    
    def divide(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            logger.error("Division error: parameters must be numbers")
            raise TypeError("Parameters must be numbers")
        if b == 0:
            logger.error("Division error: division by zero")
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b