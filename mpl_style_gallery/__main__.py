#!/usr/bin/env python
"""
Create Matplotlib style gallery for all stylesheets and display in the browser.

By default, all plots are rebuilt, but this can be avoided using
the `--skip-build` (`-s`) flag.

To build a static website, run suppress user input and set a static output
directory::

    python -m mpl_style_gallery --no-input --static-output TARGET_DIRECTORY

"""
import argparse
import os
import shutil

from . import app
from . import build
from .path_utils import disk, remove_directory


def save_static_output(output, output_directory):
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.mkdir(output_directory)
    with open(os.path.join(output_directory, 'index.html'), 'w') as f:
        f.write(output)
    shutil.copytree(os.path.join('mpl_style_gallery', 'static'),
                    os.path.join(output_directory, 'static'))
    shutil.copytree(os.path.join('mpl_style_gallery', 'build'),
                    os.path.join(output_directory, 'build'))


def main():
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=formatter)
    parser.add_argument('-s', '--skip-build', action='store_true',
                        help="If set, skip plot-generation step.")
    parser.add_argument('--serve', nargs=2,
                        help="Serve app on hostname and port")
    parser.add_argument('--no-input', action='store_true',
                        help="Do not allow input stylesheets.")
    parser.add_argument('--static-output',
                        help="Save static files to static output directory.")

    args = parser.parse_args()

    if not args.skip_build:
        remove_directory(disk.build_dir)
        build.save_all_plots()

    gallery = app.GalleryApp(args.no_input)

    if args.static_output:
        output = gallery.render_static()
        save_static_output(output, args.static_output)
    elif args.serve:
        hostname, port = args.serve
        gallery.serve(hostname, port)
    else:
        gallery.open()


if __name__ == '__main__':
    main()
