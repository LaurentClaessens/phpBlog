#! venv/bin/python3

from src.blog import Blog
from src.article_summary import ArticleSummary
from src.utilities import read_json_file


def create_blog(filename):
    """Read the json and create the blog."""
    blog = Blog()
    json_articles = read_json_file("articles.json")
    for data in json_articles:
        if not data.get("published", True):
            continue
        article = ArticleSummary(name=data["name"], blog=blog)
        article.set_title(data["title"])
        article.set_date(data["date"])
        article.description = data["description"]
        blog.add_article(article)
    return blog


def do_work(filename):
    """Do the work."""
    blog = create_blog(filename)
    blog.build()


do_work("articles.json")
