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

from pathlib import Path
import shutil
from src.article_summary import ArticleSummary

dprint = print

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
        self.main_dir = Path('.').resolve()
        self.build_dir = self.main_dir / "blog"
        self.build_html_dir = self.build_dir / "html"
        self.src_dir = self.main_dir / "articles_src"

        self.build_dir.mkdir(parents=True, exist_ok=True)
        self.build_html_dir.mkdir(parents=True, exist_ok=True)

    def add_article(self, article):
        """
        Add an article to the flux.

        @param {ArticleSummary} `article`
        """
        self.article_list.append(article)
        article.build()

    def build(self):
        """Create the html files and rss.xml."""
        for article in self.article_list:
            article.build()
        self.write_xml()
        src_css = self.main_dir / "articles.css"
        shutil.copy(src_css, self.build_dir )

    def older_links(self):
        """Return the html code for the list of older articles."""
        text = "<br> <ul>"
        list_copy = self.article_list[:]
        list_copy.reverse()
        for article in list_copy:
            text = text + article.older_link()

        text = text + "</ul>\n"
        return text

    def write_xml(self):
        """Rewrite the xml file."""

        skel = open("skel_rss.xml", 'r').read()
        code_list = []
        for article in self.article_list:
            code_list.append(article.xml_code())
        articles_code = "\n".join(code_list)

        xml = skel.replace("__ARTICLES__", articles_code)

        with open(self.build_dir / 'rss.xml', 'w') as rss_xml:
            rss_xml.write(xml)
