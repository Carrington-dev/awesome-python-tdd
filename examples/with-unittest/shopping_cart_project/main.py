import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('ShoppingCartLogger')

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"

class DiscountInterface(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(DiscountInterface):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        discount_amount = total * (self.percentage / 100)
        return total - discount_amount

class ShoppingCart:
    def __init__(self, discount_strategy: DiscountInterface = None):
        self.products = {}
        self.discount_strategy = discount_strategy
        self.logger = logger
        self.logger.info("Initialized ShoppingCart with discount strategy: %s", 
                         type(discount_strategy).__name__ if discount_strategy else "None")
    
    def add_product(self, name: str, price: float):
        if name.lower() in self.products:
            self.products[name.lower()]["quantity"] += 1
        else:
            self.products[name.lower()] = {
                "product": Product(name.lower(), price),
                "quantity": 1
            }
        self.logger.info("Added product: %s with price: %.2f", name.lower(), price)