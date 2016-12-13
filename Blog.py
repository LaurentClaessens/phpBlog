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

from xml.etree.ElementTree import Element,parse,ElementTree
from ArticleSummary import ArticleSummary

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

        This function is end-user function and makes several things :
        - add the article in the xml file
        - creates the php file
        - rewrite the xml file
        """
        # We insert in position 3 because the channel includes
        # - title, link, description (of the blog) before the list
        # of articles.
        if article not in self:
            self._channel.insert(3,article.DOM_item_element())
            self.write_xml()
        else :
            print("You already have an article with title "+article.title)
        article.create_php(self._xml_source)
    def article_list(self):
        """
        Yield the list of the articles published on the blog.

        The articles are given under the form of 'ArticleSummary' objects.
        """
        for item in self._channel.iter("item"):
            title=item.find("title").text
            link=item.find("link").text
            art=ArticleSummary(name=None)
            art.set_title(title)
            yield art
    def write_xml(self,filename=None):
        """
        Rewrite the xml file. 

        By default, it overwrites the original file, but you can pass the
        `filename` parameter.
        """
        if filename is None :
            filename=self._xml_source
        new=parse(self._xml_source)
        new.getroot()[0]=self._channel
        new.write(filename,encoding="utf-8")
    def __contains__(self,article):
        """
        Return 'True' if this flux already contains an article with
        the same title.
        """
        for art in self.article_list():
            if art.title==article.title :
                return True
        return False
