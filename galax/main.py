"""
Copyright 2021 Michael Anckaert

This file is part of Galax.

Galax is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Galax is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Galax.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import shutil
from pathlib import Path

from galax.exporters import html, gmi
from galax import utils


def get_object_list():
    p = Path('contents')
    pages = [x for x in p.iterdir() if x.is_file()]
    p = Path('contents/articles')
    articles = [x for x in p.iterdir() if x.is_file()]
    pages.extend(articles)
    return pages


def url_for_path(path):
    return utils.remove_suffix(utils.remove_prefix(str(path), "contents/"), ".md")


def html_url_for_path(path):
    return url_for_path(path) + ".html"


def gmi_url_for_path(path):
    return url_for_path(path) + ".gmi"


def build_link_map(articles):
    link_map = []
    for article_path in articles:
        with open(article_path, 'r') as f:
            contents = f.readlines()
            title = contents[0][1:].strip()

            link_map.append({
                "title": title, 
                "path": article_path, 
                "gmi_url": gmi_url_for_path(article_path),
                "html_url": html_url_for_path(article_path),
                "contents": ''.join(contents),
                "is_article": str(article_path).startswith('contents/articles')
            })

    return link_map


def generate():
    clean()

    Path("output/html/articles").mkdir(parents=True, exist_ok=True)
    Path("output/gmi/articles").mkdir(parents=True, exist_ok=True)

    objects = get_object_list()
    link_map = build_link_map(objects)

    html.save_contents(link_map)
    gmi.save_contents(link_map)

    article_map = [l for l in link_map if l['is_article']]
    html.save_article_index(article_map)
    gmi.save_article_index(article_map)


def clean():
    try:
        shutil.rmtree('output')
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build your static site in HTML and Gemini output')
    parser.add_argument('action', choices=['build', 'clean'])
    args = parser.parse_args()
    if args.action == "build":
        generate()
    elif args.action == "clean":
        clean()
    else:
        args.print_usage()
