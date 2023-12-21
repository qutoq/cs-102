import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab4.task2 import Respondent, group_respondents, parse_data, get_groups


class TestRespondent(unittest.TestCase):

    def test_sort_respondents(self):
        list = [
            Respondent('2', age=30),
            Respondent('1', age=20),
            Respondent('3', age=40)
        ]

        true_result = [
            Respondent('1', 20),
            Respondent('2', 30),
            Respondent('3', 40)
        ]
        result = sorted(list, key=lambda respondent: respondent.age)
        self.assertEqual(result, true_result)

    def test_group_respondents(self):
        respondents = [
            Respondent("1", 25),
            Respondent("2", 15),
            Respondent("3", 10),
        ]
        true_result = ['0-20: 2 (15), 3 (10)', '21-40: 1 (25)']
        groups = [(0, 20), (21, 40), (41, 60)]
        result = group_respondents(respondents, groups)
        self.assertEqual(result, true_result)

    def test_generate_age_groups(self):
        groups = "20 30 40"
        true_result = [
            (0, 20),
            (21, 30),
            (31, 40),
            (41, 123)
        ]
        result = get_groups(groups)
        self.assertEqual(result, true_result)


if __name__ == '__main__':
    unittest.main()
