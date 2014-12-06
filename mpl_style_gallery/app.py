#!/usr/bin/env python
import os
from collections import namedtuple

import flask

from path_utils import disk, in_directory
from web_utils import open_app


local_dir = os.path.dirname(os.path.abspath(__file__))

Cell = namedtuple('Cell', ['url', 'thumbnail', 'alt'])


app = flask.Flask(__name__)


@app.route('/static/css/<path:filename>')
def send_css_files(filename):
    return flask.send_from_directory('static/css', filename)


@app.route('/images/<path:filename>')
def send_build_files(filename):
    return flask.send_from_directory('build/images', filename)


def create_page(plot_names, gallery_rows, url='/', template='index.html'):
    """Create web page displaying the given data and route the given URL there.
    """
    def server():
        return flask.render_template(template, plot_names=plot_names,
                                     gallery_rows=gallery_rows)
    app.add_url_rule(url, view_func=server)


def main():
    with in_directory(local_dir):
        table = []
        for style_name, image_list in disk.iter_image_sets():
            # XXX: `thumbnail` is actually not a thumbnail.
            #      Rescaling would improve loading times.
            image_cells = [Cell(url=path, thumbnail=path, alt='image')
                           for path in image_list]
            table.append([style_name, image_cells])

        plot_names = disk.get_plot_names()
        create_page(plot_names, table)

        open_app(app)
