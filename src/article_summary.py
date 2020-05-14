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
    This is the summary of an article, that means basically 
    what we found/write in the xml file of the rss flux.

    - `name` is the generic filename of the article. Not its title.
      The file names will de deduced from there. If the author writes the
      file "XXX.html", he has to pass "XXX" as name here.
      The php file will be named "XXX.php" and the html content
      searched in "XXX.html". See also the subdirectory 
      structure described in README.md
    """
    def __init__(self,name):
        if not name:
            raise ValueError("You must provide a name for your article")
        self.title = None
        self.name = name
        self.description = None
        self.date = None
    def set_title(self,t):
        self.title=t
    def set_date(self,d):
        self.date=d
    def set_description(self,t):
        self.description=t
    def get_title(self):
        return self.title
    def get_php_file(self):
        s = os.path.join(PHP_DIR, self.name + ".php")
        return s
    def get_html_file(self):
        return os.path.join(HTML_DIR,self.name+".html")
    def xml_code(self):
        """
        Return a text which is the XML code to be included in
        rss.xml.
        """
        text = "<item><title>__TITLE__</title><link>__LINK__</link></item>"
        text = text.replace("__TITLE__", self.title)
        text = text.replace("__LINK__", self.get_php_file())
        return text
