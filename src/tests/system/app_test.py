from unittest import TestCase
from unittest.mock import patch
from src.app import print_blogs
from src import app
from src.blog import Blog
from src.post import Post

class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'TestCreateBlog', 'TestAuthor', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['TestCreateBlog'])

    def test_menu_calls_print_blogs(self):
        with patch('src.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_read_blog(self):
        blog = Blog('Blog Title', 'Test Author')
        app.blogs = {blog.title: blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'Blog Title', 'q')
            self.assertEqual(app.blogs['Blog Title'], blog)

    def test_menu_calls_create_post(self):
        blogTitle = 'Blog Title'
        blog = Blog(blogTitle, 'Test Author')
        app.blogs = {blog.title: blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', blogTitle, 'PostTitle', 'Content', 'q')
            app.menu()
            self.assertEqual(blog.posts[0].json(), {'title': 'PostTitle', 'content': 'Content'})

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.print') as mocked_print:
            print_blogs()
            mocked_print.assert_called_with('- Blog :: Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input', return_value='Test'):
            with patch('src.app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test Post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('src.app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
--- Post Title ---

Post Content
'''

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Post Content')
            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEqual(blog.posts[0].content, 'Post Content')
