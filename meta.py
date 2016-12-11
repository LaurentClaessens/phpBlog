#! /usr/bin/env python3
# -*- coding: utf8 -*-

import rssflux

blog=rssflux.Blog("Trss.xml")

meta=rssflux.ArticleSummary(title="Qu'est-ce que la méta-programmation ?",html_file="meta.html")
meta.set_title="Qu'est-ce que la méta programmation ?"
meta.set_html_file="meta.html"
meta.set_decription="Du code qui génère du code qui est interprété pour produire du code ..."

blog.add_article(meta)
