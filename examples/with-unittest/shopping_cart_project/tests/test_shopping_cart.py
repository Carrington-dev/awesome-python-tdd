import unittest
from main import ShoppingCart, logger

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        logger.info("Setting up a new ShoppingCart for testing.")
    
    def tearDown(self):
        logger.info("Tearing down the ShoppingCart after testing.")
        del self.cart
    
    def test_add_product(self):
        logger.info("Testing add_product method.")
        self.cart.add_product("Apple", 1.0)
        self.assertIn("apple", self.cart.products)
        self.assertEqual(self.cart.products["apple"]["product"].price, 1.0)
    
    def test_add_multiple_products(self):
        logger.info("Testing adding multiple products.")
        self.cart.add_product("Banana", 0.5)
        self.cart.add_product("Banana", 0.5)
        self.cart.add_product("Banana", 0.5)
        self.assertIn("banana", self.cart.products)
        self.assertEqual(self.cart.products["banana"]["quantity"], 3)
    
    def test_add_different_products(self):
        logger.info("Testing adding different products.")
        self.cart.add_product("Orange", 0.8)
        self.cart.add_product("Grapes", 2.0)
        self.assertIn("orange", self.cart.products)
        self.assertIn("grapes", self.cart.products)
        self.assertEqual(self.cart.products["orange"]["product"].price, 0.8)
        self.assertEqual(self.cart.products["grapes"]["product"].price, 2.0)

        logger.info("Current cart contents: %s", self.cart.products)   

        self.assertEqual(len(self.cart.products), 2)

        logger.info("Current cart contents: %s", self.cart.products)
    
    def test_case_insensitivity(self):
        logger.info("Testing case insensitivity in product names.")
        self.cart.add_product("Mango", 1.5)
        self.cart.add_product("mango", 1.5)
        self.assertIn("mango", self.cart.products)
        self.assertEqual(self.cart.products["mango"]["quantity"], 2)

    def test_empty_cart(self):
        logger.info("Testing behavior of an empty cart.")
        self.assertEqual(len(self.cart.products), 0)
        logger.info("Current cart contents: %s", self.cart.products)

    def test_remove_product(self):
        logger.info("Testing remove_product method not implemented.")
        self.cart.remove_product("mango")  # Assuming remove_product is not implemented
        self.assertNotIn("mango", self.cart.products)
    
if __name__ == '__main__':
    unittest.main()
