#! /usr/bin/env python3
# -*- coding: utf8 -*-

import rssflux

blog=rssflux.Blog("rss.xml")

meta=rssflux.ArticleSummary(name="meta")
meta.set_title("Qu'est-ce que la méta programmation ?")
meta.set_date("Décembre 2016")
meta.set_decription="Du code qui génère du code qui est interprété pour produire du code ..."


meta.create_php("rss.xml")
#blog.add_article(meta)
