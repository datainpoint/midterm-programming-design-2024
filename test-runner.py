import unittest
import importlib

class TestMidterm(unittest.TestCase):
    def test_01_range_fizz_buzz(self):
        self.assertEqual(asgmt.range_fizz_buzz(1, 5), [1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(6, 10), ['Fizz', 7, 8, 'Fizz', 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(11, 15), [11, 'Fizz', 13, 14, 'Fizz Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(16, 20), [16, 17, 'Fizz', 19, 'Buzz'])
        self.assertEqual(asgmt.range_fizz_buzz(21, 25), ['Fizz', 22, 23, 'Fizz', 'Buzz'])
    def test_02_cumulative_sum(self):
        self.assertEqual(asgmt.cumulative_sum(1, 2, 3), [1, 3, 6])
        self.assertEqual(asgmt.cumulative_sum(2, 3, 5), [2, 5, 10])
        self.assertEqual(asgmt.cumulative_sum(2, 3, 5, 7, 11), [2, 5, 10, 17, 28])
        self.assertEqual(asgmt.cumulative_sum(1, 2, 3, 4, 5), [1, 3, 6, 10, 15])
        self.assertEqual(asgmt.cumulative_sum(2, 4, 6, 8, 10), [2, 6, 12, 20, 30])
    def test_03_return_days_abbreviation_from_int(self):
        self.assertEqual(asgmt.return_days_abbreviation_from_int(0), ('Sunday', 'Sun.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(1), ('Monday', 'Mon.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(2), ('Tuesday', 'Tue.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(3), ('Wednesday', 'Wed.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(4), ('Thursday', 'Thu.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(5), ('Friday', 'Fri.'))
        self.assertEqual(asgmt.return_days_abbreviation_from_int(6), ('Saturday', 'Sat.'))
    def test_04_median_args(self):
        self.assertEqual(asgmt.median_args("January", "February", "March"), "February")
        self.assertEqual(asgmt.median_args("January", "February", "March", "April"), ("February", "March"))
        self.assertEqual(asgmt.median_args(5, 2, 3), 3)
        self.assertEqual(asgmt.median_args(5, 7, 2, 3), 4.0)
        self.assertEqual(asgmt.median_args("January", "February", "March", "April", "May"), ("March"))
        self.assertEqual(asgmt.median_args("January", "February", "March", "April", "May", "June"), ("March", "April"))
        self.assertEqual(asgmt.median_args(7, 5, 2, 3, 11), 5)
        self.assertEqual(asgmt.median_args(7, 5, 2, 3, 11, 13), 6.0)
    def test_05_square_negatives(self):
        self.assertEqual(asgmt.square_negatives([-3, -2, -1, 0, 1, 2, 3]), [9, 4, 1])
        self.assertEqual(asgmt.square_negatives([-3, -2, -1, 0, 1, 2, 3, '4', '5']), [9, 4, 1])
        self.assertEqual(asgmt.square_negatives([-3, -2, -1, False, True, 2, 3, '4', '5']), [9, 4, 1])
        self.assertEqual(asgmt.square_negatives([-4, -3, -2, -1, False, True, 2, 3, '4', '5', '6']), [16, 9, 4, 1])
        self.assertEqual(asgmt.square_negatives([-5, -4, -3, -2, -1, False, True, 2, 3, '4', '5', 6, 7]), [25, 16, 9, 4, 1])
    def test_06_filter_non_negatives(self):
        self.assertEqual(asgmt.filter_non_negatives([-3, -2, -1, 0, 1, 2, 3]), [0, 1, 2, 3])
        self.assertEqual(asgmt.filter_non_negatives([-3, -2, -1, 0, 1, 2, 3, '4', '5']), [0, 1, 2, 3])
        self.assertEqual(asgmt.filter_non_negatives([-3, -2, -1, False, True, 2, 3, '4', '5']), [False, True, 2, 3])
        self.assertEqual(asgmt.filter_non_negatives([-4, -3, -2, -1, False, True, 2, 3, '4', '5', '6']), [False, True, 2, 3])
        self.assertEqual(asgmt.filter_non_negatives([-5, -4, -3, -2, -1, False, True, 2, 3, '4', '5', 6, 7]), [False, True, 2, 3, 6, 7])
    def test_07_find_min_max(self):
        self.assertEqual(asgmt.find_min_max([2, 3, 5, 7, 11]), {'min': 2, 'max': 11})
        self.assertEqual(asgmt.find_min_max([13, 17, 19, 23, 29, 31]), {'min': 13, 'max': 31})
        self.assertEqual(asgmt.find_min_max([10, 9, 8, 6, 4, 1]), {'min': 1, 'max': 10})
        self.assertEqual(asgmt.find_min_max([2, 3, 5]), {'min': 2, 'max': 5})
        self.assertEqual(asgmt.find_min_max([11, 12, 12, 13, 13, 14, 14]), {'min': 11, 'max': 14})
    def test_08_find_idxmin_idxmax(self):
        self.assertEqual(asgmt.find_idxmin_idxmax([2, 3, 5, 7, 11]), {'idxmin': [0], 'idxmax': [4]})
        self.assertEqual(asgmt.find_idxmin_idxmax([2, 3, 5, 7, 11, 11, 7, 5, 3, 2]), {'idxmin': [0, 9], 'idxmax': [4, 5]})
        self.assertEqual(asgmt.find_idxmin_idxmax([10, 9, 8, 6, 4, 1]), {'idxmin': [5], 'idxmax': [0]})
        self.assertEqual(asgmt.find_idxmin_idxmax([10, 9, 8, 6, 4, 1, 1, 4, 6, 8, 9, 10]), {'idxmin': [5, 6], 'idxmax': [0, 11]})
        self.assertEqual(asgmt.find_idxmin_idxmax([1, 2, 3, 3, 2, 1]), {'idxmin': [0, 5], 'idxmax': [2, 3]})
    def test_09_pig_latin(self):
        self.assertEqual(asgmt.pig_latin("pig"), 'igpay')
        self.assertEqual(asgmt.pig_latin("smile"), 'ilesmay')
        self.assertEqual(asgmt.pig_latin("eat"), 'eatyay')
        self.assertEqual(asgmt.pig_latin("latin"), 'atinlay')
        self.assertEqual(asgmt.pig_latin("apple"), 'appleyay')
    def test_10_fibonacci(self):
        self.assertEqual(asgmt.fibonacci(0, 1, 5), [0, 1, 1, 2, 3])
        self.assertEqual(asgmt.fibonacci(0, 1, 7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(asgmt.fibonacci(0, 1, 11), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(asgmt.fibonacci(0, 1, 3), [0, 1, 1])
        self.assertEqual(asgmt.fibonacci(1, 1, 5), [1, 1, 2, 3, 5])
        self.assertEqual(asgmt.fibonacci(1, 2, 5), [1, 2, 3, 5, 8])
        self.assertEqual(asgmt.fibonacci(2, 3, 5), [2, 3, 5, 8, 13])

asgmt = importlib.import_module("midterm")
suite = unittest.TestLoader().loadTestsFromTestCase(TestMidterm)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))