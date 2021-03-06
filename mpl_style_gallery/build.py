"""
Save test plots for all styles defined in `mpltools.style`.

Note that `test_artists_plot` calls `matplotlib.pyplot.tight_layout` so subplot
spacing is not tested for this plot.
"""
from __future__ import print_function

import os
import os.path as pth
from time import time
from warnings import catch_warnings

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import style

from .constants import IMAGE_EXT
from .path_utils import base_filename, disk


plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['image.interpolation'] = 'none'

USER_STYLE_NAME = 'user-style'


def save_plots(stylesheet, image_ext=IMAGE_EXT, base_dir=None):
    """Save plots for a given stylessheet.

    Each script in the plot-scripts directory is run with the given
    stylesheet and saved to a subdirectory in `base_dir`.
    """
    base_dir = base_dir or disk.images_dir
    style_dir = pth.join(base_dir, base_filename(stylesheet))

    with style.context(stylesheet):
        # Create directory after trying to load style so we don't create an
        # empty directory if the stylesheet isn't valid.
        if not pth.exists(style_dir):
            os.makedirs(style_dir)

        for script in disk.iter_plot_scripts():
            image_name = base_filename(script) + image_ext
            with open(script) as f:
                exec(compile(f.read(), script, 'exec'), {})
            plt.savefig(pth.join(style_dir, image_name))
            plt.close('all')


def save_all_plots():
    """Save plots for all stylesheets known by matplotlib."""
    # Only show styles defined by package, not by user.
    for stylesheet in style.available:
        print("Creating plots for style: {}".format(stylesheet))
        save_plots(stylesheet)
    print("\nDone.")


def save_scratch_plots(stylesheet):
    """Save temporary plots for stylesheet based on user input.

    Parameters
    ----------
    stylesheet : str
        URL pointing to a stylesheet or matplotlibrc key-value pairs.

    Returns
    -------
    status : str
        Status message: Empty-string for success; error message for failures.
    """
    status = ''

    if not mpl.is_url(stylesheet):
        filename = USER_STYLE_NAME + '.' + style.core.STYLE_EXTENSION
        filename = pth.join(disk.scratch_dir, filename)
        with open(filename, 'w') as f:
            f.write(stylesheet)
        stylesheet = filename

    try:
        with catch_warnings(record=True) as warnings:
            save_plots(stylesheet, base_dir=disk.scratch_dir)
    except ValueError:
        msg = ("Input '{}' does not appear to be a valid stylesheet.\n"
               "Verify your network connection and the target stylesheet.")
        status = msg.format(stylesheet)
    else:
        status = '' if len(warnings) == 0 else warnings[-1].message

    return status


def build_gallery_table(src_dir=None, prevent_cache=False):
    """Return plot-names and table of images.

    Each row of the table starts with the style name, and followed by
    dictionaries with 'url', 'thumbnail', 'alt', 'style', and 'type' keys.

    Parameters
    ----------
    prevent_cache : bool
        If True, append a timestamp to URLs to prevent caching.
    """
    query_string = '?{}'.format(time())
    table = []
    for stylesheet, image_list in disk.iter_image_sets(root_dir=src_dir):
        # XXX: `thumbnail` is actually not a thumbnail.
        #      Rescaling would improve loading times.
        if prevent_cache:
            image_list = [path + query_string for path in image_list]
        image_cells = [dict(url=path, thumbnail=path, alt='image',
                            style=stylesheet, type=base_filename(path))
                       for path in image_list]
        table.append([stylesheet, image_cells])
    return table
