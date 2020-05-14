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

from pathlib import Path
import os
import subprocess

dprint = print

MAIN_DIR = Path('.').resolve()
SRC_DIR = MAIN_DIR / "articles_src"     
BUILD_DIR = MAIN_DIR / "build"
TMP_DIR = MAIN_DIR / "tmp"

class ArticleSummary(object):
    """
    This is the summary of an article, that means basically 
    what we found/write in the xml file of the rss flux.

    - `name` is the generic filename of the article. Not its title.
      The file names will de deduced from there. If the author writes the
      file "XXX.html", he has to pass "XXX" as name here.
    """
    def __init__(self, name, blog):
        if not name:
            raise ValueError("You must provide a name for your article")
        self.name = name
        self.blog = blog
        self.title = None
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

    def get_dst_file(self):
        return os.path.join(HTML_DIR, self.name+".html")

    def get_source_html_file(self):
        """
        Return the path of the source html.

        In the case the author has written in markdown, the
        returned path does not correspond to an existing file.
        """
        return SRC_DIR / f'{self.name}.html'

    def get_source_md_file(self):
        """
        Return the path of the source markdown.

        In the case the author has written in html, the
        returned path does not correspond to an existing file.
        """
        return SRC_DIR / f'{self.name}.md'

    def dst_file(self):
        """Return the destination build filename."""
        return BUILD_DIR / f"{self.name}.html"

    def get_source_html_code(self):
        """
        Return the html source code of self.

        This is a html with the author part (not the final one).
        This is either the html written by the other or a generated
        html from the markdown.
        """
        html_file = self.get_source_html_file()
        if html_file.is_file():
            return open(html_file, 'r').read()

        md_filename = self.get_source_md_file()

        command = f"pandoc --mathml -s {md_filename}"
        bytes_ans = subprocess.check_output(['pandoc', 
                                             '--mathml', '-s', 
                                             md_filename])
        html_base = bytes_ans.decode("utf8")
        start_tag = "<body>"
        end_tag = "</body>"
        start = html_base.find(start_tag) + len(start_tag)
        stop = html_base.find(end_tag)
        return html_base[start:stop]

    def get_link(self):
        """Return the web link to this article."""
        return f"{self.name}.html"

    def older_link(self):
        """Return the html of the link to self."""
        link = f"{self.name}.html"
        return f"<li> <a href={self.get_link()}> {self.title}</a></li>"

    def build(self):
        """Create the final html file."""
        html_source = self.get_source_html_code()
        skel_file = MAIN_DIR / "skel_article.html"
        text = open(skel_file, 'r').read()
        text = text.replace('__MAIN_TITLE__', self.title)
        text = text.replace('__DATE__', self.date)
        text = text.replace('__AUTHOR_HTML__', html_source)
        text = text.replace('__OLDER_LINKS__', self.blog.older_links())
        open(self.dst_file(), 'w').write(text)

    def xml_code(self):
        """Return the part of `rss.xml` for self."""
        text = "<item><title>__TITLE__</title><link>__LINK__</link></item>"
        text = text.replace("__TITLE__", self.title)
        text = text.replace("__LINK__", self.get_link())
        return text
