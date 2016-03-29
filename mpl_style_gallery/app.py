import os.path as pth

import flask
import matplotlib
from flask import request
from jinja2 import Environment, FileSystemLoader

from .build import build_gallery_table, save_scratch_plots
from .path_utils import make_directory
from .web_utils import open_app
from .path_utils import disk, remove_directory


LOCAL_DIR = pth.dirname(pth.abspath(__file__))


class GalleryApp(object):

    def __init__(self, no_input_stylesheets=False):
        self._app = flask.Flask(__name__)
        self._allow_inputs = not no_input_stylesheets
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
            directory = pth.join(disk.root_dir, 'static/css')
            return flask.send_from_directory(directory, filename)

        @app.route('/build/<path:filename>')
        def route_build_files(filename):
            directory = pth.join(disk.root_dir, 'build')
            return flask.send_from_directory(directory, filename)

        @app.route('/')
        def render():
            return self.render()

        @app.route('/', methods=['POST'])
        def update_styles():
            stylesheet = request.form['input-stylesheet']
            self._input_status = save_scratch_plots(stylesheet)
            self._input_stylesheet = stylesheet
            return self.render()

    def _rendering_kwargs(self):
        return dict(
            allow_inputs=self._allow_inputs,
            column_headers=self._plot_names,
            input_status=self._input_status,
            input_stylesheet=self._input_stylesheet,
            matplotlib_version=matplotlib.__version__,
        )

    def render(self):
        user_rows = build_gallery_table(src_dir=disk.scratch_dir,
                                        prevent_cache=True)
        gallery_table = user_rows + self._gallery_table

        kwargs = self._rendering_kwargs()
        kwargs['gallery_table'] = gallery_table
        return flask.render_template('index.html', **kwargs)

    def render_static(self):
        loader = FileSystemLoader(pth.join(LOCAL_DIR, 'templates'))
        env = Environment(loader=loader)
        template = env.get_template('index.html')

        kwargs = self._rendering_kwargs()
        kwargs['gallery_table'] = self._gallery_table
        return template.render(**kwargs)

    def serve(self, host, port):
        self._app.run(host=host, port=int(port))

    def open(self):
        """Serve app and open browser to the app.

        This is intended for running locally.
        """
        open_app(self._app)
