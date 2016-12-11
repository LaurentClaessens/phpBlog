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

"""
Read an xml file like the one given in 'example/rss.xml', and add a new article.
"""

from xml.etree.ElementTree import Element,parse
from xml.etree.ElementTree import tostring      
import os


HTML_DIR="html"     # the subdirectory in which are the html files.

class ArticleSummary(object):
    """
    This is the summary of an article, that means basically what we found/write
    in the xml file of the rss flux.

    - `html_file` is the filename of the html file containing the text. This is
      what is called "link" is the xml file.
    - `guide` is the relative path to the html file from where the 'rss.xml' file
       stays.
    """
    def __init__(self,title=None,html_file=None):
        self.title=title
        self.html_file=html_file
    def get_title(self):
        return self.title
    def get_html_file(self):
        return self.html_file
    def get_guide(self):
        return os.path.join(HTML_DIR,self.get_html_file())
    def DOM_item_element(self):
        # return a DOM element describing the "<item>...</item>"
        # to be added to the xml file.
        item_el = Element("item")
        title_el = Element("title")
        title_el.text=self.title
        link_el=Element("link")
        link_el.text=self.html_file
        item_el.append(title_el)
        item_el.append(link_el)
        return item_el

class Blog(object):
    """
    This class represent the whole blog.
    This is a wrapper around parsing the xml file.

    - `_channel` is the element "channel" of the xml file.
        The xml file is supposed to have one and only one "channel" element.
        It is computed only once, and then can be modified (by adding articles
        for examples).
    """
    def __init__(self,xml_source):
        self._xml_source=xml_source
        self._channel=parse(self._xml_source).getroot()[0]
    def add_article(self,article):
        """
        Add an article to the flux.
        - `article` is type `ArticleSummary`.
        """
        self._channel.append(article.DOM_item_element())
    def article_list(self):
        """
        Yield the list of the articles published on the blog.

        The articles are given under the form of 'ArticleSummary' objects.
        """
        for item in self._channel.iter("item"):
            title=item.find("title").text
            link=item.find("link").text
            yield ArticleSummary(title,link)
