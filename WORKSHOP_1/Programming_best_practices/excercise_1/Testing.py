import unittest
from palindrome import is_palindrome

class test_palindrome(unittest.TestCase):

    def test_is_palindrome(self):
        """
        Test palindrome function with a correct result
        """
        self.assertEqual(is_palindrome("a ti no bonita"), True)
        self.assertEqual(is_palindrome("Lavan Esa Base Naval"), True)
        self.assertEqual(is_palindrome("SoMetamos o maTemos"), True)

        



if __name__=='__main__':
    unittest.main()
