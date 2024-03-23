from unittest import TestCase
from unittest.mock import patch
from src.app import print_blogs
from src import app
from src.blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.print') as mocked_print:
            print_blogs()
            mocked_print.assert_called_with('- Blog :: Test by Test Author (0 posts)')
