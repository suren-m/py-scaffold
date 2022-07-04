import unittest
from services import repos_service


class TestReposService(unittest.TestCase):

    def test_service_should_return_repos(self):
        result = repos_service.get_gh_repos("microsoft")
        total_repos = len(result)
        self.assertGreater(total_repos, 0)
