from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(str(b), 'Blog :: Test by Test Author (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        self.assertEqual(str(b), 'Blog :: Test by Test Author (1 post)')
        b.create_post('Test Post 2', 'Test Content 2')
        self.assertEqual(str(b), 'Blog :: Test by Test Author (2 posts)')

    def test_json(self):
        b = Blog('Test', 'Test Author')
        expected = {'title': 'Test', 'author': 'Test Author', 'posts': []}

        self.assertDictEqual(expected, b.json())
