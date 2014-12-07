"""
Save test plots for all styles defined in `mpltools.style`.

Note that `test_artists_plot` calls `matplotlib.pyplot.tight_layout` so subplot
spacing is not tested for this plot.
"""
from __future__ import print_function

import os
import os.path as pth
from collections import namedtuple

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import style

from .constants import IMAGE_EXT
from .path_utils import disk, base_filename


Cell = namedtuple('Cell', ['url', 'thumbnail', 'alt'])


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
            execfile(script)
            plt.savefig(pth.join(style_dir, image_name))
            plt.close('all')


def save_all_plots():
    # Only show styles defined by package, not by user.
    for stylesheet in style.available:
        print("Creating plots for style: {}".format(stylesheet))
        save_plots(stylesheet)
    print("\nDone.")


def build_gallery_table(src_dir=None):
    """Return plot-names and table of images.

    Each row of the table starts with the style name, and followed by `Cell`
    instances, which have `url`, `thumbnail`, and `alt` attributes.
    """
    table = []
    for stylesheet, image_list in disk.iter_image_sets(root_dir=src_dir):
        # XXX: `thumbnail` is actually not a thumbnail.
        #      Rescaling would improve loading times.
        image_cells = [Cell(url=path, thumbnail=path, alt='image')
                       for path in image_list]
        table.append([stylesheet, image_cells])
    return table
