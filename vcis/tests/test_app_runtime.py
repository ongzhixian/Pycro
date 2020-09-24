import unittest

class app_runtime_tests(unittest.TestCase):
    
    def test_get_host_name(self):
        """
        python -m unittest tests.test_app_runtime.app_runtime_tests.test_get_host_name
        """
        # Arrange
        from helpers.app_runtime import get_host_name

        # Act
        hostname = get_host_name()

        # Assert
        self.assertEqual(hostname, 'ACADIAN')

if __name__ == '__main__':
    unittest.main()