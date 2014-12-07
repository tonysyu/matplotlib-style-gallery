#!/usr/bin/env python
import os

import flask
from flask import request

from .build import build_gallery_table, save_plots
from .path_utils import in_directory
from .web_utils import open_app
from .path_utils import disk


local_dir = os.path.dirname(os.path.abspath(__file__))


class GalleryApp(object):

    def __init__(self):
        self._app = flask.Flask(__name__)
        self._template = 'index.html'
        self._plot_names = disk.get_plot_names()
        self._gallery_table = build_gallery_table()
        self._input_status = ''
        self._input_stylesheets = []

        self._add_url_rules(self._app)

    def _add_url_rules(self, app):

        @app.route('/static/css/<path:filename>')
        def route_css_files(filename):
            return flask.send_from_directory('static/css', filename)

        @app.route('/build/<path:filename>')
        def route_build_files(filename):
            return flask.send_from_directory('build', filename)

        @app.route('/')
        def render():
            return self.render()

        @app.route('/', methods=['POST'])
        def update_styles():
            stylesheet = request.form['input-stylesheet']
            try:
                msg = "Building plots for '{}'"
                self._input_status = msg.format(stylesheet)
                save_plots(stylesheet, base_dir=disk.scratch_dir)
                self._input_status = ''
            except ValueError:
                msg = "Input '{}' does not appear to be a valid stylesheet."
                self._input_status = msg.format(stylesheet)
            return self.render()

    def render(self):
        user_rows = build_gallery_table(src_dir=disk.scratch_dir)
        gallery_table = user_rows + self._gallery_table
        return flask.render_template(self._template,
                                     input_status=self._input_status,
                                     column_headers=self._plot_names,
                                     gallery_table=gallery_table)

    def run(self):
        # App opens in the package root since image paths in the table are
        # relative to the package root.
        with in_directory(local_dir):
            open_app(self._app)


def main():
    app = GalleryApp()
    app.run()
