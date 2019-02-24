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
        self._xml_source = xml_source
        self.article_list = []
    def add_article(self, article):
        """
        Add an article to the flux.

        @param {ArticleSummary} `article`

        This function is end-user function and makes several things :
        - add the article in the xml file
        - creates the php file
        - rewrite the xml file
        """
        self.article_list.append(article)
        article.create_php(self._xml_source)
    def write_xml(self,filename=None):
        """
        Rewrite the xml file. 

        By default, it overwrites the original file, but you can pass the
        `filename` parameter.
        """

        skel = """
        <rss version="2.0"> 
            <channel> 
                <title>Blog de Laurent Claessens</title> 
                <link>http://laurent.claessens-donadello.eu/blog</link> 
                <description>
                    Mon blog personnel, tout fait à la main en Vim.
                </description>
                __ARTICLES__
            </channel>
        </rss>
        """
        code_list = []
        for art in self.article_list:
            code_list.append(art.xml_code())
        articles_code = "\n".join(code_list)

        xml = skel.replace("__ARTICLES__", articles_code)

        if filename is None :
            filename=self._xml_source
        with open(filename, 'w') as rss_xml:
            rss_xml.write(xml)
    def __contains__(self,article):
        """
        Return 'True' if this flux already contains an article with
        the same title.
        """
        raise DeprecationWarning
        for art in self.article_list:
            if art.title==article.title :
                return True
        return False
