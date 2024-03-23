from unittest import TestCase
from blog.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'content': 'Test Content', 'title': 'Test'}

        self.assertDictEqual(expected, p.json())
