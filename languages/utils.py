import requests
from datetime import datetime, timedelta


class TrandingGithubAPI:
    def __init__(self, languages_count):
        self.from_date = (datetime.today() -
                          timedelta(days=30)).strftime("%Y-%m-%d")
        self.languages_count = languages_count
        self.api_url = f"""https://api.github.com/search/repositories?q=created:>
        {self.from_date}&sort=stars&order=desc&per_page={self.languages_count}"""

    def _get_trending_repositories(self):
        repositories = requests.get(url=self.api_url).json()["items"][:100]
        return repositories

    def get_trending_languages_data(self):
        repositories = self._get_trending_repositories()
        languages_data = {}

        for repository in repositories:
            language = Language()
            languages_data = language._check_repetition_and_process_data(
                languages_data, repository["language"], repository
            )
        return languages_data


class Language:
    def _check_repetition_and_process_data(self, languages_data, language, repository):
        if languages_data.get(language):
            languages_data[language]["count"] += 1
            languages_data[language]["repositories"].append(repository)
        else:
            languages_data[language] = {
                "count": 1,
                "repositories": [
                    repository,
                ],
            }
        return languages_data
