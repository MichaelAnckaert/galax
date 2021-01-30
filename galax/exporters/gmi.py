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

import re
from jinja2 import Environment, FileSystemLoader

def generate_article_list(link_map):
    loader = FileSystemLoader('templates/gmi')
    env = Environment(loader=loader)
    template = env.get_template('blog.gmi')
    return template.render(posts=link_map)


def save_article_index(link_map):
    gmi = generate_article_list(link_map)
    with open('output/gmi/blog.gmi', 'w') as f:
        f.write(gmi)


def prepare_content(contents):
    """Transform the Markdown links to GMI links"""
    def gmi_link(m):
        target = m.group(2)
        label = m.group(1)
        return f"\n=> {target} {label}"

    contents = re.sub(r"\[(.*?)\]\((.*?)\)", gmi_link, contents)
    return contents.replace('.md', '.gmi')


def save_contents(link_map):
    for link in link_map:
        content = prepare_content(link['contents'])
        filename = f"output/gmi/{link['gmi_url']}"
        with open(filename, 'w') as f:
            f.write(content)


