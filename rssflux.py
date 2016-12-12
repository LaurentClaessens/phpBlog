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
from xml.etree.ElementTree import tostring
import os

# the subdirectory in which are the html files written by the author.
# This is relative from the path to which belongs 'rss.xml'
HTML_DIR="html"     
PHP_DIR="php"     
SRC_DIR="src"     

class ArticleSummary(object):
    """
    This is the summary of an article, that means basically what we found/write
    in the xml file of the rss flux.

    - `name` is the generic filename of the article. Not its title.
      The file names will de deduced from there. If the author writes the
      file "XXX.html", he has to pass "XXX" as name here.
      The php file will be named "XXX.php" and the html content searched in 
      "XXX.html". See also the subdirectory structure desribed in README.md
    """
    def __init__(self,name):
        self.title=None
        self.name=name
        self.description=None
        self.date=None
    def set_title(self,t):
        self.title=t
    def set_date(self,d):
        self.date=d
    def set_description(self,t):
        self.description=t
    def get_title(self):
        return self.title
    def get_html_file(self):
        return self.html_file
    def get_php_file(self):
        return os.path.join(PHP_DIR,self.name+".php")
    def get_html_file(self):
        return os.path.join(HTML_DIR,self.name+".html")
    def create_php(self,surrounding):
        """ Creates the php file; the one that the reader will see.  """
        text="""<? php
                require("SRC_DIR/Article.php");

                $art=new Article("TITLE");
                $art->set_date("DATE");
                $art->set_content_file("HTML_FILE");
                $art->set_surrounding_flux("SURROUNDING");
                $art->echo_page();
                ?>            
        """.replace("SRC_DIR",SRC_DIR)\
            .replace("DATE",self.date)\
            .replace("HTML_FILE",self.get_html_file())\
            .replace("SURROUNDING",surrounding)\
            .replace("TITLE",self.title)
        with open(self.get_php_file(),'w') as f:
            f.write(text)

    def DOM_item_element(self):
        # return a DOM element describing the "<item>...</item>"
        # to be added to the xml file.
        item_el = Element("item")

        title_el = Element("title")
        title_el.text=self.title

        link_el=Element("link")
        link_el.text=self.get_php_file()

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

        This function is end-user function and makes several things :
        - add the article in the xml file
        - creates the php file
        - rewrite the xml file
        """
        # We insert in position 3 because the channel includes
        # - title, link, description (of the blog) before the list
        # of articles.
        self._channel.insert(3,article.DOM_item_element())
        article.create_php(self._xml_source)
        self.write_xml()
    def article_list(self):
        """
        Yield the list of the articles published on the blog.

        The articles are given under the form of 'ArticleSummary' objects.
        """
        for item in self._channel.iter("item"):
            title=item.find("title").text
            link=item.find("link").text
            yield ArticleSummary(title,link)
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
