
import surfshop
import unittest

class Tests(unittest.TestCase):

  def setUp(self):
        self.cart = surfshop.ShoppingCart()

  def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity = 1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

  def test_add_surfboard2(self):
        message = self.cart.add_surfboards(quantity = 2)
        self.assertEqual(message, f'Successfully added 2 surfboards to cart!')

  @unittest.skip
  def test_toomanyboards5(self):
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  def test_add_surfboardn(self):
        for i in range(2,5):
          with self.subTest(i = i):
            message = self.cart.add_surfboards(i)
            self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
            self.cart = surfshop.ShoppingCart()
  def test   
  @unittest.expectedFailure
  def test_toomanyboards(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

unittest.main()
