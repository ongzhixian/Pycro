import unittest

class app_runtime_tests(unittest.TestCase):
    
    def get_host_name_test(self):
        """
        python -m unittest tests.test_app_runtime.app_runtime_tests.get_host_name_test
        """
        # Arrange
        from helpers.app_runtime import get_host_name

        # Act
        hostname = get_host_name()

        # Assert
        self.assertEqual(hostname, 'ACADIAN')

if __name__ == '__main__':
    unittest.main()