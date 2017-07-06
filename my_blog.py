#! /usr/bin/env python3
# -*- coding: utf8 -*-

from Blog import Blog
from ArticleList import article_list


blog=Blog("rss.xml")

for art in article_list :
    blog.add_article(art)
