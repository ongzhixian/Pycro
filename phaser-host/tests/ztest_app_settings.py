import unittest

# TODO: testing for app.settings

def fun(x):
    return x + 1

#get_config_json

class AppConfigTest(unittest.TestCase):
    
    def test(self):
        from app import settings
        self.assertEqual(fun(3), 4)

    # def test2(self):
    #     self.assertEqual(fun(5), 4)
    # def test_sum(self):
    #     self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

class DummyTest(unittest.TestCase):
    def test3(self):
        self.assertEqual(fun(6), 7)

    def test4(self):
        self.assertEqual(fun(7), 8)



if __name__ == '__main__':
    unittest.main()