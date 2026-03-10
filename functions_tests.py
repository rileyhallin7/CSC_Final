from functions import summarize
import unittest

class TestCases(unittest.TestCase):
    pass

    def test_summarize1(self):
        input1 = 1937
        input2 = 1942
        expected = 1940
        result = summarize(input1, input2)['highest_year']
        self.assertEqual(result, expected)
    def test_summarize2(self):
        input1 = 1937
        input2 = 1942
        expected = 101985
        result = summarize(input1, input2)['highest_population']
        self.assertEqual(result, expected)
    def test_summarize3(self):
        input1 = 1937
        input2 = 1942
        expected = {'highest_population': 101985,
                    'highest_year': 1940,
                    'lowest_population': 35217,
                    'lowest_year': 1937,
                    'percent_change': 59.462759462759465,
                    'total_change': 20941}
        result = summarize(input1, input2)
        self.assertEqual(result, expected)


