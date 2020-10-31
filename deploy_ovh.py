#! venv/bin/python3

"""Deploy the blog to OVH."""

from pathlib import Path
import subprocess

REMOTE = "claessenvs@ftp.cluster003.hosting.ovh.net"
MAIN_DIR = Path('.').resolve()
BUILD_DIR = MAIN_DIR / "build"
HTML_DIR = BUILD_DIR / "html"


def create_batchfile():
    skel = open("batchfile.skel", 'r').read()
    put_html_list = []
    for filename in HTML_DIR.iterdir():
        put_html_list.append(f"put {filename}")

    put_html = "\n".join(put_html_list)
    text = skel.replace("__PUT_HTML__", put_html)

    batch_filename = "batchfile"
    with open(batch_filename, 'w') as batchfile:
        batchfile.write(text)
        print(f"save: {batch_filename}")


def copy_ovh():
    """Send the whole to ovh."""
    subprocess.call(['sftp', '-b', 'batchfile', REMOTE])


create_batchfile()
copy_ovh()
