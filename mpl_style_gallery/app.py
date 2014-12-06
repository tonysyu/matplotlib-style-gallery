#!/usr/bin/env python
import os

import flask

from .build import build_gallery_table
from .path_utils import in_directory
from .web_utils import open_app


local_dir = os.path.dirname(os.path.abspath(__file__))


class GalleryApp(object):

    def __init__(self):
        self._app = flask.Flask(__name__)
        self._route_css_files()
        self._route_build_files()

    def _route_css_files(self):
        url = '/static/css/<path:filename>'

        def route_css_files(filename):
            return flask.send_from_directory('static/css', filename)
        self._app.add_url_rule(url, view_func=route_css_files)

    def _route_build_files(self):
        url = '/images/<path:filename>'

        def route_build_files(filename):
            return flask.send_from_directory('build/images', filename)
        self._app.add_url_rule(url, view_func=route_build_files)

    def render(self, plot_names, table, url='/', template='index.html'):
        """Render the gallery.
        """
        def _render():
            return flask.render_template(template, column_headers=plot_names,
                                         gallery_table=table)
        self._app.add_url_rule(url, view_func=_render)

    def run(self):
        plot_names, table = build_gallery_table()
        self.render(plot_names, table)

        # App opens in the package root since image paths in the table are relative
        # to the package root.
        with in_directory(local_dir):
            open_app(self._app)


def main():
    app = GalleryApp()
    app.run()
