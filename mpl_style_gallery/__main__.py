#!/usr/bin/env python
"""
Create Matplotlib style gallery for all Matplotlib stylesheets and display in
the browser. By default, all plots are rebuilt, but this can be avoided using
the `--skip-build` (`-s`) flag.
"""
import argparse

from . import app
from . import build
from .path_utils import disk, remove_directory


def main():
    formatter = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=formatter)
    parser.add_argument('-s', '--skip-build', action='store_true',
                        help="If set, skip plot-generation step.")

    args = parser.parse_args()

    if not args.skip_build:
        remove_directory(disk.build_dir)
        build.save_all_plots()

    app.main()


if __name__ == '__main__':
    main()
