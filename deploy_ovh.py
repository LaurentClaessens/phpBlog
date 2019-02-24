#! /usr/bin/env python3

"""
Deploy the blog to OVH.
"""

import os

REMOTE = "claessenvs@ftp.cluster003.ovh.net"

commande = f"sftp -b batchfile {REMOTE}"

CWD = os.getcwd()

def list_dir(dirname):
    """
    Yield the absolute path of the files in `dirname`.
    """
    for filename in os.listdir(dirname):
        filepath = os.path.join(CWD, dirname, filename)
        yield filepath

def html_files():
    """
    Yield the files to be copied in the html directory.
    They are the `html` files in `html`
    """
    for filename in list_dir('html'):
        if filename.endswith('.html'):
            yield filename

def php_files():
    """
    Yield the files to be copied in the php directory
    They are the `php` files in `php`
    """
    for filename in list_dir('php'):
        if filename.endswith('.php'):
            yield filename

def create_batchfile():
    skel ="""
cd laurent/blog
put rss.xml
cd laurent/blog/html
__PUT_HTML__
cd laurent/blog/php
__PUT_PHP__
    """
    put_html_list = []
    put_php_list = []
    for filename in html_files():
        put_html_list.append(f"put {filename}")
    for filename in php_files():
        put_php_list.append(f"put {filename}")

    put_html = "\n".join(put_html_list)
    put_php = "\n".join(put_php_list)
    text = skel.replace("__PUT_HTML__", put_html)
    text = text.replace("__PUT_PHP__", put_php)

    with open("batchfile", 'w') as batchfile:
        batchfile.write(text)


create_batchfile()
