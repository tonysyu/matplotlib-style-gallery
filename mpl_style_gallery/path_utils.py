import os
import os.path as pth
from contextlib import contextmanager
from fnmatch import fnmatch
from glob import glob
from shutil import rmtree

from .constants import IMAGE_PATTERN


@contextmanager
def in_directory(path):
    """ Change the current working directory temporarily.
    """
    original_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_path)


def filter_image_files(files):
    return [fname for fname in files if fnmatch(fname, IMAGE_PATTERN)]


def remove_directory(directory):
    """Remove directory, including all children, if it exists."""
    if pth.exists(directory):
        rmtree(directory)


class DiskLayout(object):
    """On-disk directory structure for this project.

    Attributes
    ----------
    scripts_dir : str
        Directory where plot scripts are stored.
    images_dir : str
        Directory where plot images are stored.
    scratch_dir : str
        Directory where user-added plot images are stored.
    """

    def __init__(self):
        self.root_dir = pth.dirname(os.path.abspath(__file__))
        self.scripts_dir = pth.join(self.root_dir, 'plot_scripts')
        self.build_dir = pth.join(self.root_dir, 'build')
        self.images_dir = pth.join(self.build_dir, 'images')
        self.scratch_dir = pth.join(self.build_dir, 'scratch')

    def get_plot_names(self):
        return [base_filename(script) for script in self.iter_plot_scripts()]

    def iter_image_sets(self, root_dir=None):
        """Yield style name and image sets for each style."""
        root_dir = root_dir or self.images_dir

        for directory, subdirs, files in os.walk(root_dir):
            image_files = filter_image_files(files)
            if len(image_files) > 0:
                image_files = self._format_filenames(directory, image_files)
                style_name = pth.basename(directory)
                yield style_name, image_files

    def iter_plot_scripts(self):
        """Yield paths to plot scripts."""
        for script in glob(pth.join(self.scripts_dir, '*.py')):
            yield script

    def _format_filenames(self, directory, files):
        directory = pth.relpath(directory, self.root_dir)
        return [pth.join(directory, fname) for fname in files]

disk = DiskLayout()


def base_filename(path):
    """Return filename with the parent path and extension stripped off."""
    filename = pth.basename(path)
    basename, ext = pth.splitext(filename)
    return basename


def make_directory(directory):
    """Make directory (including sub-directories), if it doesn't exist."""
    if not pth.exists(directory):
        os.makedirs(directory)
