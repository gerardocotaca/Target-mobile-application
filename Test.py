import unittest
from ClassFile import User, Product, ShoppingCart


class TestProject(unittest.TestCase):
    def test_user_login(self):
        user = User(1, "test_user", "password", "test@example.com")
        self.assertTrue(user.login("password"))  # Provide the correct password for testing

    def test_product_details(self):
        product = Product(1, "Laptop", "Description", 999.99, "electronics")
        self.assertEqual(product.view_details(), "Laptop: Description, $999.99")

    def test_shopping_cart(self):
        cart = ShoppingCart(1, 4.5)
        cart.add_item("Laptop", 999.99)  # Pass name and price as arguments
        self.assertEqual(cart.calculate_total(), 999.99)


if __name__ == '__main__':
    unittest.main()



