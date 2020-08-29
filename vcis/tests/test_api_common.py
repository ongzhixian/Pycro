import unittest
import requests 

class api_common_tests(unittest.TestCase):
    """
    python -m unittest tests.test_api_common.api_common_tests
    """
    
    def test_get_api_common_utc(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_get_api_common_utc
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/utc"

        # Act
        req = requests.get(url = url)
        jsonData = req.json()

        # Assert
        self.assertEqual(jsonData['name'], '/api/common/utc')
        self.assertEqual(jsonData['result'], 'success')

    def test_post_api_common_utc(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_post_api_common_utc
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/utc"
        req = requests.post(url = url)

        # Act
        jsonData = req.json()
        
        # Assert
        # res = isinstance(test_string, str) 
        self.assertEqual(jsonData['name'], '/api/common/utc')
        self.assertEqual(jsonData['result'], 'success')

    def test_get_api_common_name(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_get_api_common_name
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/name"

        # Act
        req = requests.get(url = url)
        jsonData = req.json()

        # Assert
        self.assertEqual(jsonData['name'], '/api/common/name')
        self.assertEqual(jsonData['result'], 'success')

    def test_post_api_common_name(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_post_api_common_name
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/name"
        req = requests.post(url = url)

        # Act
        jsonData = req.json()
        
        # Assert
        # res = isinstance(test_string, str) 
        self.assertEqual(jsonData['name'], '/api/common/name')
        self.assertEqual(jsonData['result'], 'success')

    def test_get_api_common_version(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_get_api_common_version
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/version"

        # Act
        req = requests.get(url = url)
        jsonData = req.json()

        # Assert
        self.assertEqual(jsonData['name'], '/api/common/version')
        self.assertEqual(jsonData['result'], 'success')

    def test_post_api_common_version(self):
        """
        python -m unittest tests.test_api_common.api_common_tests.test_post_api_common_version
        """
        # Arrange
        url = "http://127.0.0.1:8080/api/common/version"
        req = requests.post(url = url)

        # Act
        jsonData = req.json()
        
        # Assert
        # res = isinstance(test_string, str) 
        self.assertEqual(jsonData['name'], '/api/common/version')
        self.assertEqual(jsonData['result'], 'success')


if __name__ == '__main__':
    unittest.main()