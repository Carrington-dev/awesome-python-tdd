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