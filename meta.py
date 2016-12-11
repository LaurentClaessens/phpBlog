#! /usr/bin/env python3
# -*- coding: utf8 -*-

from xml.etree.ElementTree import tostring
import rssflux

blog=rssflux.Blog("Trss.xml")

for art in blog.article_list():
    print(art.get_title())
    print(art.get_guide())

meta=rssflux.ArticleSummary(title="Qu'est-ce que la méta-programmation ?",html_file="meta.html")
meta_item=meta.DOM_item_element()


blog.add_article(meta)

print("Après ajout, nous avons --- ")

for art in blog.article_list():
    print(art.get_title())


