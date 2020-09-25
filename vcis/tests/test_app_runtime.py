import unittest
import socket
import os
from unittest.mock import patch


class app_runtime_tests(unittest.TestCase):
    """
    python -m unittest -v tests.test_app_runtime.app_runtime_tests
    """
    
    def test_get_host_name(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_host_name
        """
        # Arrange
        from helpers.app_runtime import get_host_name

        # Act
        with patch('helpers.app_runtime.gethostname', return_value='TEST_HOST_NAME') as mock_gethostname:
            hostname = get_host_name()
            mock_gethostname.assert_called_once()
            
        # Assert
        self.assertEqual(hostname, 'TEST_HOST_NAME')
    

    def test_get_config_json_missing_file(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_config_json_missing_file
        """
        # Arrange
        from helpers.app_runtime import get_config_json
        
        # Act
        app_config = get_config_json('')

        # Assert
        self.assertEqual(len(app_config), 1)
        self.assertEqual(True, 'DEVICE_NAME' in app_config.keys())

    def test_get_config_json(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_config_json
        """
        # Arrange
        from helpers.app_runtime import get_config_json
        
        # Act
        app_config = get_config_json()

        # Assert
        self.assertEqual(True, 'DEVICE_NAME' in app_config.keys())

    def test_get_secrets_json_missing_file(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_secrets_json_missing_file 
        """
        # Arrange
        from helpers.app_runtime import get_secrets_json
        
        # Act
        app_secrets = get_secrets_json('')

        # Assert
        self.assertEqual(app_secrets, {})

    