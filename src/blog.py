"""
Copyright Laurent Claessens
contact : laurent@claessens-donadello.eu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


"""Describe my blog."""

from xml.etree.ElementTree import Element,parse,ElementTree
from ArticleSummary import ArticleSummary

class Blog(object):
    """
    This class represent the whole blog.

    - `_channel` is the element "channel" of the xml file.
        The xml file is supposed to have one and only
        one "channel" element.It is computed only once, and
        then can be modified (by adding articles for examples).
    """
    def __init__(self):
        self.article_list = []

    def add_article(self, article):
        """
        Add an article to the flux.

        @param {ArticleSummary} `article`
        """
        self.article_list.append(article)
        article.build(self._xml_source)

    def build():
        """Create the html files and rss.xml."""
        for article in self.article_list:
            article.build()
        self.write_xml()
    
    def older_links(self):
        """Return the html code for the list of older articles."""
        text = "<br> <ul>"
        for article in self.article_list[:].reverse():
            text = text + article.older_link()

        text = text + "</ul>\n"

    def write_xml(self):
        """Rewrite the xml file."""

        skel = open("skel_rss.xml", 'r').read()
        code_list = []
        for article in self.article_list:
            code_list.append(article.xml_code())
        articles_code = "\n".join(code_list)

        xml = skel.replace("__ARTICLES__", articles_code)

        with open('rss.xml', 'w') as rss_xml:
            rss_xml.write(xml)
