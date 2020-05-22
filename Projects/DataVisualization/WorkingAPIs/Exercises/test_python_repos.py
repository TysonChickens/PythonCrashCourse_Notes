import unittest
import python_repos_visual as prv

class TestPythonRepos(unittest.TestCase):
    """Tests for GitHub Python repo visuals."""

    def setUp(self):
        """Initialize all functions and variables."""
        self.r = prv.get_response()
        self.repo_dicts = prv.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = prv.get_project_data(self.repo_dicts)
    
    def test_response(self):
        """Test for status_code 200 is successful."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo(self):
        """Test for data and required keys."""
        repo_keys = ['name', 'owner', 'html_url']
        for key in repo_keys:
            self.assertTrue(key in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()