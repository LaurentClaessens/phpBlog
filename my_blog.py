#! venv/bin python3

from blog import Blog
from ArticleList import article_list

blog = Blog()

for art in article_list:
    blog.add_article(art)
blog.write_xml()
