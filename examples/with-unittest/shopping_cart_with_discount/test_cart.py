import unittest
from cart import (BuyOneGetOneFreeStrategy, BuyXGetYFreeStrategy, 
                  FixedAmountDiscountStrategy, 
                  PercentageDiscountStrategy,
                  ShoppingCart, 
                  Product,  
                  logger,)


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.products = {
            "apple": Product(**{"price": 1.0, "name": "apple"}),
            "banana": Product(**{"price": 0.5, "name": "banana"})
        }
        

    def test_add_product(self):
        self.cart.add_product("apple", 3)
        logger.info(f"Cart items after adding apple: {self.cart.items}")
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"]['quantity'], 3)

    def test_remove_product(self):
        self.cart.add_product("apple", 2)
        self.cart.remove_product("apple", 1)
        logger.info(f"Cart items after removing apple: {self.cart.items}")
        self.assertEqual(self.cart.items["apple"]['quantity'], 1)
        self.cart.remove_product("apple", 1)
        self.assertNotIn("apple", self.cart.items)

    def test_total_price(self):
        self.cart.add_product("apple", 2)  # 2 * 1.0 = 2.0
        self.cart.add_product("banana", 4)  # 4 * 0.5 = 2.0
        total = self.cart.total_price()
        logger.debug(f"Total price in test: {total}")
        self.assertEqual(total, 4.0)

    def test_empty_cart(self):
        total = self.cart.total_price()
        self.assertEqual(total, 0.0)
        self.assertEqual(len(self.cart.items), 0)

class TestPercentageDiscountStrategy(unittest.TestCase):
    def setUp(self):
        self.discount_strategy = PercentageDiscountStrategy()
        self.cart = ShoppingCart()

    def tearDown(self):
        self.discount_strategy = None

    def test_apply_discount(self):
        self.cart.add_product("apple", 100)  # 100 * 1.0 = 100.0
        discount_percentage = 10.0
        discounted_price = self.discount_strategy.apply_discount(self.cart, discount_percentage)
        expected_price = 90.0
        self.assertEqual(discounted_price, expected_price)

    
    def test_no_discount(self):
        self.cart.add_product("apple", 50)  # 50 * 1.0 = 50.0
        discount_percentage = 0.0
        discounted_price = self.discount_strategy.apply_discount(self.cart, discount_percentage)
        expected_price = 50.0
        self.assertEqual(discounted_price, expected_price)

    def test_full_discount(self):
        self.cart.add_product("apple", 100)
        discount_percentage = 100.0
        discounted_price = self.discount_strategy.apply_discount(self.cart, discount_percentage)
        expected_price = 0.0
        self.assertEqual(discounted_price, expected_price)

    def test_invalid_discount(self):
        self.cart.add_product("apple", 60)  # 60 * 1.0 = 60.0
        discount_percentage = -10.0
        with self.assertRaises(ValueError):
            self.discount_strategy.apply_discount(self.cart, discount_percentage)
    
    def test_excessive_discount(self):
        self.cart.add_product("apple", 70)  # 70 * 1.0 = 70.0
        discount_percentage = 150.0
        with self.assertRaises(ValueError):
            self.discount_strategy.apply_discount(self.cart, discount_percentage)
    
    def test_zero_price(self):
        self.cart.add_product("apple", 0)  # 0 * 1.0 = 0.0
        discount_percentage = 20.0
        discounted_price = self.discount_strategy.apply_discount(self.cart, discount_percentage)
        expected_price = 0.0
        self.assertEqual(discounted_price, expected_price)
        
class TestFixedAmountDiscountStrategy(unittest.TestCase):
    def setUp(self):
        self.discount_strategy = FixedAmountDiscountStrategy()
        self.cart = ShoppingCart()

    def tearDown(self):
        self.discount_strategy = None

    def test_apply_fixed_amount_discount(self):
        self.cart.add_product("apple", 100)  # 100 * 1.0 = 100.0
        discount_amount = 20.0
        discounted_price = self.discount_strategy.apply_discount(self.cart, discount_amount)
        expected_price = 80.0
        logger.debug(f"Discounted price: {discounted_price}, Expected price: {expected_price}")
        self.assertEqual(discounted_price, expected_price)
    
    def test_where_fixed_amount_discount_not_applied(self):
        self.cart.add_product("apple", 10)  # 10 * 1.0 = 10.0
        discount_amount = 20.0
        with self.assertRaises(ValueError):
            self.discount_strategy.apply_discount(self.cart, discount_amount)
    
    def test_invalid_fixed_amount_discount(self):
        self.cart.add_product("apple", 50)  # 50 * 1.0 = 50.0
        discount_amount = -10.0
        with self.assertRaises(ValueError):
            self.discount_strategy.apply_discount(self.cart, discount_amount)

class TestBuyOneGetOneFreeStrategy(unittest.TestCase):
    def setUp(self):
        self.discount_strategy = BuyOneGetOneFreeStrategy()
        self.cart = ShoppingCart()

    def tearDown(self):
        self.discount_strategy = None

    def test_apply_bogo_discount(self):
        self.cart.add_product("apple", 3)  # 3 apples
        # Implementation for testing BOGO discount would go here
        expected_price = 2.0  # Pay for 2 apples, get 1 free
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)

    def test_remove_bogo_discount(self):
        self.cart.add_product("apple", 4)  # 4 apples
        # Implementation for testing removal of BOGO discount would go here
        excepted_price = 4.0  # Pay for all 4 apples
        price_after_removal = self.discount_strategy.remove_discount(self.cart)
        self.assertEqual(price_after_removal, excepted_price)
    
    def test_bogo_with_odd_number_of_items(self):
        self.cart.add_product("banana", 5)  # 5 bananas
        expected_price = 1.5  # Pay for 3 bananas, get 2 free
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)
    
    def test_bogo_with_multiple_products(self):
        self.cart.add_product("apple", 2)   # 2 apples
        self.cart.add_product("banana", 3)  # 3 bananas
        self.cart.add_product("guava", 13)  # 13 guavas
        expected_price =   19.5 # Pay for 1 apple + 2 bananas + 7 guavas
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)

    def test_bogo_with_no_items(self):
        expected_price = 0.0
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)

class TestBuyXGetYFree(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.discount_strategy = BuyXGetYFreeStrategy(self.cart)
        
    def test_apply_buy_x_get_y_discount(self):
        self.cart.add_product("apple", 3)  # 3 apples
        # Implementation for testing BOGO discount would go here
        expected_price = 2.0  # Pay for 2 apples, get 1 free
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)

    def test_apply_buy_x_get_y_discount_two(self):
        self.cart.add_product("apple", 17)  # 3 apples
        # Implementation for testing BOGO discount would go here
        expected_price = 12.0  # Pay for 2 apples, get 1 free
        self.discount_strategy.x = 2
        self.discount_strategy.y = 1
        discounted_price = self.discount_strategy.apply_discount(self.cart)
        self.assertEqual(discounted_price, expected_price)


if __name__ == '__main__':
    unittest.main()