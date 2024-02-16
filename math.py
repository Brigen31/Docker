import unittest

# Classe SimpleMath avec une fonction statique 'addition'
class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

# Classe TestSimpleMath pour tester la fonction 'addition' de SimpleMath
class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(-1, 1), 0)
        self.assertEqual(SimpleMath.addition(-1, -1), -2)

# Exécutez les tests
if __name__ == '__main__':
    unittest.main()
