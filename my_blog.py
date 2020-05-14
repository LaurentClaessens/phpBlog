#! venv/bin python3

from src.blog import Blog
from article_list import article_list

blog = Blog()

for art in article_list:
    blog.add_article(art)
blog.build()
