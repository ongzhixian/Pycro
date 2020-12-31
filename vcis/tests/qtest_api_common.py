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
        from api.common import api_common_utc_get

        x = api_common_utc_get()

        # # Arrange
        # url = "http://127.0.0.1:8080/api/common/utc"

        # # Act

        # req = requests.get(url = url)
        # jsonData = req.json()

        # # Assert
        # self.assertEqual(jsonData['name'], '/api/common/utc')
        # self.assertEqual(jsonData['result'], 'success')
