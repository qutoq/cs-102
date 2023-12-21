import unittest
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab4.task1 import Cinema, films_path, views_path, user_views, parse_data


class TestCinema(unittest.TestCase):
    def test_parse(self):
        true_films = {
            1: 'Мстители: Финал',
            2: 'Хатико',
            3: 'Дюна',
            4: 'Унесенные призраками'
        }

        true_views = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        films, views = parse_data(films_path, views_path)
        self.assertEqual(films, true_films)
        self.assertEqual(views, true_views)

    def test_like_users(self):
        true_result = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        result = Cinema(films_path, views_path, user_views).like_users()
        self.assertEqual(result, true_result)

    def test_delete_watched_films(self):
        like_users = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]
        true_result = [3, 4, 3, 3]
        result = Cinema(films_path, views_path, user_views).delete_watched_films(like_users)
        self.assertEqual(result, true_result)


if __name__ == '__main__':
    unittest.main()
