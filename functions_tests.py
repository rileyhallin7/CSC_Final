from functions import summarize
import unittest

class TestCases(unittest.TestCase):
    pass

    def test_summarize1(self):
        input1 = 1937
        input2 = 1942
        expected = 'Largest Population Year: 1940'
        result = summarize(input1, input2)['highest']['year']
        self.assertEqual(result, expected)
    def test_summarize2(self):
        input1 = 1937
        input2 = 1942
        expected = 'Largest Population: 101985'
        result = summarize(input1, input2)['highest']['population']
        self.assertEqual(result, expected)
    def test_summarize3(self):
        input1 = 1937
        input2 = 1942
        expected = {'highest': {'year': 'Largest Population Year: 1940', 'population': 'Largest Population: 101985'}, 'lowest': {'year': 'Smallest Population Year: 1937', 'population': 'Smallest Population: 35217'}, 'total_change': 'Total Change: 20941', 'percent_change': 'Percent Change: 59.462759462759465'}
        result = summarize(input1, input2)
        self.assertEqual(result, expected)


