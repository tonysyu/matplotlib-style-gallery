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


Adding your own styles
======================

Comparing the default styles is great, but what if you want to test something
different.

If you have a plot script that you believe would help others decide which is
the best stylesheet, **pull requests are welcome!**


Installation
============

::

   $ pip install git+https://github.com/tonysyu/matplotlib-style-gallery

::

   $ git clone https://github.com/tonysyu/matplotlib-style-gallery.git
   $ cd matplotlib-style-gallery
   $ python -m mpl_style_gallery


Dependencies
============

* `Matplotlib <http://matplotlib.org/>`__ >= 1.4
* `Flask <http://flask.pocoo.org/>`__


License
=======

New BSD (a.k.a. Modified BSD). See `LICENSE`_ file for details.

.. _LICENSE:
   https://github.com/tonysyu/matplotlib-style-gallery/blob/master/LICENSE
