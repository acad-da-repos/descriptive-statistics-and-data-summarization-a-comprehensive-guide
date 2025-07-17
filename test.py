
import unittest
import pandas as pd
from assignment import summarize_data

class TestDataSummarization(unittest.TestCase):
    def test_summarize_data(self):
        # Create a sample dataframe
        data = {'Value': [10, 20, 30, 40, 50]}
        df = pd.DataFrame(data)

        stats = summarize_data(df)

        # Check the type of the output
        self.assertIsInstance(stats, dict)

        # Check the keys in the output
        self.assertIn('mean', stats)
        self.assertIn('median', stats)
        self.assertIn('std_dev', stats)

        # Check the values of the statistics
        self.assertAlmostEqual(stats['mean'], 30.0)
        self.assertAlmostEqual(stats['median'], 30.0)
        self.assertAlmostEqual(stats['std_dev'], 15.811388300841896)

if __name__ == '__main__':
    unittest.main()
