#!/usr/bin/env python
import flask
from flask import request

from .build import build_gallery_table, save_scratch_plots
from .path_utils import in_directory, make_directory
from .web_utils import open_app
from .path_utils import disk, remove_directory


class GalleryApp(object):

    def __init__(self):
        self._app = flask.Flask(__name__)
        self._input_status = ''
        self._input_stylesheet = ''

        self._clear_scratch_directory()

        self._plot_names = disk.get_plot_names()
        self._gallery_table = build_gallery_table()

        self._add_url_rules(self._app)

    @staticmethod
    def _clear_scratch_directory():
        remove_directory(disk.scratch_dir)
        make_directory(disk.scratch_dir)

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
            self._input_status = save_scratch_plots(stylesheet)
            self._input_stylesheet = stylesheet
            return self.render()

    def render(self):
        user_rows = build_gallery_table(src_dir=disk.scratch_dir,
                                        prevent_cache=True)
        gallery_table = user_rows + self._gallery_table
        return flask.render_template('index.html',
                                     input_status=self._input_status,
                                     input_stylesheet=self._input_stylesheet,
                                     column_headers=self._plot_names,
                                     gallery_table=gallery_table)

    def run(self):
        # App opens in the package root since image paths in the table are
        # relative to the package root.
        with in_directory(disk.root_dir):
            open_app(self._app)


def main():
    app = GalleryApp()
    app.run()
