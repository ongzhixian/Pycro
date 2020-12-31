import unittest

class api_stats_tests(unittest.TestCase):
    """
    python -m unittest -v tests.test_api_stats.api_stats_tests
    get_api_stats
    update_api_stats
    """
   
    def test_get_api_stats(self):
        """
        python -m unittest -v tests.test_api_stats.api_stats_tests.test_get_api_stats
        """
        # Arrange
        from modules.api_stats import get_api_stats

        # Act
        count = get_api_stats("TEST_STAT_NAME")
            
        # Assert
        self.assertEqual(count, 0)
    
    def test_update_api_stats(self):
        """
        python -m unittest -v tests.test_api_stats.api_stats_tests.test_update_api_stats
        """
        # Arrange
        from modules.api_stats import get_api_stats, update_api_stats

        # Act
        prev_count = get_api_stats("TEST_STAT_NAME")
        update_api_stats("TEST_STAT_NAME")
        count = get_api_stats("TEST_STAT_NAME")
            
        # Assert
        self.assertEqual(prev_count, 0)
        self.assertEqual(count, prev_count + 1)

    def test_have_api_stats(self):
        """
        python -m unittest -v tests.test_api_stats.api_stats_tests.test_have_api_stats
        """
        # Arrange
        from modules.api_stats import have_api_stats, get_api_stats, update_api_stats

        # Act
        stat_exists = have_api_stats("TEST_NEW_STAT_NAME")
        update_api_stats("TEST_NEW_STAT_NAME")
        count = get_api_stats("TEST_NEW_STAT_NAME")
            
        # Assert
        self.assertEqual(stat_exists, False)
        self.assertEqual(count, 1)