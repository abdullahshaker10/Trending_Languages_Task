from django.test import TestCase
from languages.utils import TrandingGithubAPI, Language


class TestTrandingGithubAPI(TestCase):
    def setUp(self) -> None:
        self.github_api = TrandingGithubAPI(100)

    def test_get_trending_repositories(self):
        repositories = self.github_api._get_trending_repositories()
        self.assertEqual(len(repositories), 100)


class TestLanguage(TestCase):
    def setUp(self) -> None:
        self.repository = {"id": "1", "language": "Go"}
        self.another_repository = {"id": "2", "language": "Go"}
        self.language_data = {}
        self.trend_language = "GO"
        self.language = Language()

    def test_check_only_one_repetition(self):
        self.assertFalse(self.language_data)
        self.language._check_repetition_and_process_data(
            self.language_data, self.trend_language, self.repository
        )
        self.assertTrue(self.language_data)
        self.assertEqual(
            self.language_data,
            {
                self.trend_language: {
                    "count": 1,
                    "repositories": [
                        self.repository,
                    ],
                }
            },
        )

    def test_check_more_repetitions(self):
        self.language_data = {
            self.trend_language: {
                "count": 1,
                "repositories": [
                    self.repository,
                ],
            }
        }
        self.assertTrue(self.language_data)
        self.language._check_repetition_and_process_data(
            self.language_data, self.trend_language, self.another_repository
        )
        self.assertEqual(
            self.language_data,
            {
                self.trend_language: {
                    "count": 2,
                    "repositories": [self.repository, self.another_repository],
                }
            },
        )
