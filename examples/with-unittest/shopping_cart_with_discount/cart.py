from abc import abstractmethod, ABC
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    # add streamHandler or fileHandler if needed
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler('logs/cart.log')  # Uncomment to log to a file
    ]
)

logger = logging.getLogger(__name__)

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, cart, percentage_discount = 0):
        pass

    @abstractmethod
    def remove_discount(self, cart, percentage_discount = 0):
        pass

class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, cart=None):
        self.cart = cart


    def apply_discount(self, cart, percentage_discount=0):
        if percentage_discount < 0 or percentage_discount > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        total_price = cart.total_price()
        discount_amount = total_price * (percentage_discount / 100)
        final_price = total_price - discount_amount
        return final_price
    
    def remove_discount(self, cart, percentage_discount=0):
        # final_price = cart.total_price() 
        # Since removing discount means going back to original price
        # removing discount means final_price = 90 * (100 / 90)
        # which is 100 * 1 = 100 (approximately original price)
        total_price = cart.total_price()
        final_price = total_price * (100 / ( 100 - percentage_discount))
        return final_price
    
class BuyOneGetOneFreeStrategy(DiscountStrategy):
    def __init__(self, cart=None):
        self.cart = cart

    def apply_discount(self, cart):
        # Implementation for BOGO discount
        total_price = 0
        for item in cart.items.values():
            quantity = item['quantity']
            free_items = quantity // 2
            total_price_per_item = item['product'].price * (quantity - free_items)
            total_price += total_price_per_item
        return total_price

        

    def remove_discount(self, cart,):
        # Implementation to remove BOGO discount
        return cart.total_price()

class BuyXGetYFreeStrategy(DiscountStrategy):
    def __init__(self, cart=None, x=1, y=1):
        self.cart = cart
        self.x = x
        self.y = y
    
    def apply_discount(self, cart):
        """Implementation for Buy X Get Y Free discount"""

        total_price = 0
        for item in cart.items.values():
            quantity = item['quantity']
            free_items = quantity // (self.x + self.y)
            total_price_per_item = item['product'].price * (quantity - free_items)
            total_price += total_price_per_item
        return total_price
    
    def remove_discount(self, cart = None):
        return self.cart.total_price() if cart else 0
            

    

class FixedAmountDiscountStrategy(DiscountStrategy):
    NUMBER_OF_ITEMS = 20  # Example fixed amount


    def apply_discount(self, cart, amount=0):
        # Implementation for fixed amount discount
        total_price = cart.total_price()
        if amount < 0:
            raise ValueError("Discount amount must be non-negative.")
        elif total_price < amount:
            raise ValueError("Discount amount cannot exceed total price.")
        elif (cart.total_number_of_items()) > self.NUMBER_OF_ITEMS and total_price > amount:
            logger.debug(f"Applying fixed amount discount of {amount} for more than {self.NUMBER_OF_ITEMS} items.")
            final_price = total_price - amount
            return final_price
        return total_price        


    def remove_discount(self, cart, amount=0):
        # Implementation to remove fixed amount discount
        total_price = cart.total_price()
        if amount < 0:
            raise ValueError("Discount amount must be non-negative.")
        elif total_price < amount:
            raise ValueError("Discount amount cannot exceed total price.")
        elif (cart.total_number_of_items()) > self.NUMBER_OF_ITEMS and total_price > amount:
            logger.debug(f"Applying fixed amount discount of {amount} for more than {self.NUMBER_OF_ITEMS} items.")
            final_price = total_price + amount
            return final_price
        return total_price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logger.debug(f"Created product: {self.name} with price {self.price}")

class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.products = {
            "apple": Product(**{"price": 1.0, "name": "apple"}),
            "banana": Product(**{"price": 0.5, "name": "banana"}),
            "guava": Product(**{"price": 2.5, "name": "guava"}),
        }
        logger.debug("Initialized an empty shopping cart.")


    def add_product(self, product_name, quantity=1):
        if product_name in self.items:
            self.items[product_name]['quantity'] += quantity
            logger.debug(f"Updated {product_name} quantity to {self.items[product_name]['quantity']}.")
        else:
            self.items[product_name] = {'product': self.products[product_name], 'quantity': quantity}
            logger.debug(f"Added {product_name} to cart with quantity {quantity}.")

    def remove_product(self, product_name, quantity=1):
        if product_name in self.items:
            if self.items[product_name]['quantity'] > 1:
                self.items[product_name]['quantity'] -= quantity
                logger.debug(f"Reduced {product_name} quantity to {self.items[product_name]['quantity']}.")
            else:
                del self.items[product_name]
                logger.debug(f"Removed {product_name} from cart.", self.items)

        else:
            logger.warning(f"Attempted to remove {product_name} which is not in the cart.")

    def total_price(self):
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        logger.debug(f"Total price calculated: {total}")
        return total
    
    def final_price_after_discount(self, discount_strategy: DiscountStrategy, discount_value=0):
        if isinstance(discount_strategy, DiscountStrategy):
            discounted_price = discount_strategy.apply_discount(self, discount_value)
            logger.debug(f"Final price after applying discount: {discounted_price}")
            return discounted_price
        return self.total_price()
    
    def total_number_of_items(self):
        total = 0
        for item in self.items.values():
            total += item['quantity']
        return total
