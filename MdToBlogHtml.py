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

import os

GENERATED_WARNING=""

def md_to_blog_html(md_filename):
    """
    Takes a 'md' file and creates an `html` file (using pandoc) which is suitable 
    for inclusion in my blogging system.
    
    Here, "suitable" means without the header : only the <body> part.
    """ 
    html_filename=md_filename.replace(".md",".html")
    os.system("pandoc -s  -o "+html_filename+" "+ md_filename)
    html_base=open(html_filename,"r").read()

    start_tag="<body>"
    end_tag="</body>"
    start=html_base.find(start_tag)+len(start_tag)
    stop=html_base.find(end_tag)

    with open(html_filename,'w') as f:
        f.write(html_base[start:stop])

