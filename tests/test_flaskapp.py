import unittest

def hello():
    return "Hello World!"


def multiply(x,y):
    return x * y


def touppercase(s):
    return s.upper()


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        pass


    def test_multiply(self):
        x = 10
        y = 12

        answer = multiply(x,y)

        self.assertEqual(answer, 120)

    def test_upper(self):
        string = "test"

        answer = touppercase(string)

        self.assertEqual(answer, "TEST")

if __name__ == '__main__':
    unittest.main()
