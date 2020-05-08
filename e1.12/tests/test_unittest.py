import index
from index import words
import unittest

class NameTestCase(unittest.TestCase):

	'''test visel'''
	def test_letter_first(self):
 	   self.assertIn('s', "skillfactory")

	def test_letter_second(self):
	    self.assertIn('f', "skillfactory")


	def test_letter_third(self):
		self.assertIn("skillfactory", words)

	def test_letter_four(self):
		self.assertIn("testing",words) 

# if __name__ == "__name__":
# 	unittest.main()
