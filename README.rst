========================
Matplotlib Style Gallery
========================


This is a simple Flask application to compare different Matplotlib styles.


Quickstart
==========

To start up the gallery, make sure that this module is in your python path
(either by installing it or just changing to this directory) and execute::

   $ python -m mpl_style_gallery

This will fire up a local server with the gallery app running and open your
web-browser to that page.


After you've run the application for first time, you don't need to re-build
the images for the gallery (unless you've added your own plot scripts), so
you can skip the plotting as follows::

   $ python -m mpl_style_gallery --skip-build


Adding your own styles
======================

Comparing the default styles is great, but what if you want to test something
different?

This app provides two ways to add your own stylesheets:

1. Find a stylesheet online and copy the URL into the app's input area.
2. Create a stylesheet on the fly by adding valid
   `matplotlibrc syntax <http://matplotlib.org/users/customizing.html>`__.
   into the input area of the application.


Adding your own plot-scripts
============================

If you have a plot script that you believe would help others decide which is
the best stylesheet, **pull requests are welcome!**

To test out your own plot script, just grab a copy of this project and drop
any plotting script into the scripts directory::

   path/to/matplotlib-style-gallery/mpl_style_gallery/plot_scripts/


Installation
============

To run the gallery, you don't actually need to install this package. You can
simply grab the source and run the package as a script::

   $ git clone https://github.com/tonysyu/matplotlib-style-gallery.git
   $ cd matplotlib-style-gallery
   $ python -m mpl_style_gallery


Dependencies
============

* `Matplotlib <http://matplotlib.org/>`__ >= 1.4
* `Flask <http://flask.pocoo.org/>`__


Roadmap
=======

This was actually created as a project for me to learn a little bit of
javascript, so look for future updates with more interactivity.


License
=======

New BSD (a.k.a. Modified BSD). See `LICENSE`_ file for details.

.. _LICENSE:
   https://github.com/tonysyu/matplotlib-style-gallery/blob/master/LICENSE
