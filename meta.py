#! /usr/bin/env python3
# -*- coding: utf8 -*-

import xml.etree.ElementTree
import rssflux

for art in rssflux.article_list("Trss.xml"):
    print(art.get_title())
    print(art.get_guide())
