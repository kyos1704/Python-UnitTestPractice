import Scripts.my_math 
import unittest


class TestMyMath(unittest.TestCase):
    def test_add(self):
        result = Scripts.my_math.add(1,2)
        self.assertEqual(result,3)



if __name__ == "__main__":
    unittest.main()