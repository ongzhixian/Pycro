import json
import unittest
from unittest.mock import patch, mock_open

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
    
    """
    Tests for get_config_json
    Test conditions:
    1.  file does not exists        test_get_config_json_not_exists
    2.  file exists
        1.  file is valid json      test_get_config_json_valid_json
        2.  file is invalid json    test_get_config_json_invalid_json
    """

    def test_get_config_json_not_exists(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_config_json_not_exists
        """
        # Arrange
        from helpers.app_runtime import get_config_json

        # Act
        with patch("helpers.app_runtime.path.exists", return_value=False) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data="{}")) as mock_func_open:
            app_config = get_config_json()
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_not_called()
        self.assertEqual(len(app_config), 2)
        self.assertEqual(True, 'DEVICE_NAME' in app_config.keys())

    def test_get_config_json_valid_json(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_config_json_valid_json
        """
        # Arrange
        from helpers.app_runtime import get_config_json

        # Act
        dummy_data = {
            "AUTH_MODE" : "DB"
        }
        with patch("helpers.app_runtime.path.exists", return_value=True) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data=json.dumps(dummy_data))) as mock_func_open:
            app_config = get_config_json()
            #assert open("path/to/open").read() == "data"
            #mock_file.assert_called_with("path/to/open")
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_called_once()
        self.assertEqual(len(app_config), 3)
        self.assertEqual(True, 'DEVICE_NAME' in app_config.keys())
        self.assertEqual(True, 'AUTH_MODE' in app_config.keys())

    def test_get_config_json_invalid_json(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_config_json_invalid_json
        """
        # Arrange
        from helpers.app_runtime import get_config_json
        from json.decoder import JSONDecodeError
        app_config = None

        # Act
        with patch("helpers.app_runtime.path.exists", return_value=True) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data="")) as mock_func_open \
        , self.assertRaises(JSONDecodeError):
            app_config = get_config_json()
            #assert open("path/to/open").read() == "data"
            #mock_file.assert_called_with("path/to/open")
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_called_once()
        self.assertEqual(app_config, None)

    """
    Tests for get_secrets_json
    Test conditions:
    1.  file does not exists        test_get_secrets_json_not_exists
    2.  file exists
        1.  file is valid json      test_get_secrets_json_valid_json
        2.  file is invalid json    test_get_secrets_json_invalid_json
    """

    def test_get_secrets_json_not_exists(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_secrets_json_not_exists
        """
        # Arrange
        from helpers.app_runtime import get_secrets_json

        # Act
        with patch("helpers.app_runtime.path.exists", return_value=False) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data="{}")) as mock_func_open:
            app_secrets = get_secrets_json()
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_not_called()
        self.assertEqual(len(app_secrets), 0)

    def test_get_secrets_json_valid_json(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_secrets_json_valid_json
        """
        # Arrange
        from helpers.app_runtime import get_secrets_json

        # Act
        dummy_data = {
            "AUTH_MODE" : "DB"
        }
        with patch("helpers.app_runtime.path.exists", return_value=True) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data=json.dumps(dummy_data))) as mock_func_open:
            app_secrets = get_secrets_json()
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_called_once()
        self.assertEqual(len(app_secrets), 1)
        self.assertEqual(True, 'AUTH_MODE' in app_secrets.keys())

    def test_get_secrets_json_invalid_json(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_get_secrets_json_invalid_json
        """
        # Arrange
        from helpers.app_runtime import get_secrets_json
        from json.decoder import JSONDecodeError
        app_secrets = None

        # Act
        with patch("helpers.app_runtime.path.exists", return_value=True) as mock_func_path_exists \
        , patch("builtins.open", mock_open(read_data="")) as mock_func_open \
        , self.assertRaises(JSONDecodeError):
            app_secrets = get_secrets_json()
            
        # Assert
        mock_func_path_exists.assert_called_once()
        mock_func_open.assert_called_once()
        self.assertEqual(app_secrets, None)



    def mock_api_call2(self):
        g = lambda x : x
        g.userxxx = 'alad'
        # g.pp = 'asd'
        #setattr(g, 'user', 'aaa')
        #setattr(self, 'userAAA', 'www')
        return g

    def test_before_each_request(self):
        """
        python -m unittest -v tests.test_app_runtime.app_runtime_tests.test_before_each_request
        """
        # Arrange
        from helpers.app_runtime import before_each_request
        from flask import Flask
        from uuid import UUID

        # Act
        app = Flask(__name__)
        with app.test_request_context('/?name=ya') as mock_context \
        , patch("helpers.app_runtime.uuid4", return_value=UUID('139f1fb2-e510-4ad9-ad27-1e8bddbdcbbe')) as mock_uuid4 \
        , patch("helpers.app_runtime.g") as mock_g:
            #app.preprocess_request()
            before_each_request()
            print("User is [{0}], correlation id is [{1}]".format(mock_g.user, mock_g.correlation_id))

        # with patch("helpers.app_runtime.g", return_value=True):
        #     before_each_request()

        # Assert
        mock_uuid4.assert_called_once()
        self.assertEqual(mock_g.correlation_id, UUID('139f1fb2-e510-4ad9-ad27-1e8bddbdcbbe'))