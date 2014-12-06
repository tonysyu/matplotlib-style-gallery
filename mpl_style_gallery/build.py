"""
Save test plots for all styles defined in `mpltools.style`.

Note that `test_artists_plot` calls `matplotlib.pyplot.tight_layout` so subplot
spacing is not tested for this plot.
"""
from __future__ import print_function

import os
import os.path as pth

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
from matplotlib import style

from .constants import IMAGE_EXT
from .path_utils import disk, base_filename


def save_plots(style_name, image_ext=IMAGE_EXT):
    style_dir = pth.join(disk.images_dir, style_name)
    if not pth.exists(style_dir):
        os.makedirs(style_dir)

    with style.context(style_name):
        for script in disk.iter_plot_scripts():
            script_name = base_filename(script)
            execfile(script)
            plt.savefig(pth.join(style_dir, script_name + image_ext))
            plt.close('all')


def save_all_plots():
    # Only show styles defined by package, not by user.
    for style_name in style.available:
        print("Creating plots for style: {}".format(style_name))
        save_plots(style_name)
    print("\nDone.")
