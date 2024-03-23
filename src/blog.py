from typing import List
from .post import Post

class Blog:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.posts: List[Post] = []

    def __repr__(self):
        return 'Blog :: {} by {} ({} post{})'.format(
            self.title,
            self.author,
            len(self.posts),
            "s" if len(self.posts) != 1 else "")

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }
