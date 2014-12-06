import itertools
import random
import socket
import webbrowser


def open_app(app, ip='127.0.0.1', port=8888, n_retries=50, debug=False):
    """Start a server serving the given HTML, and open a browser
    Parameters
    ----------
    app : Flask application
        Application to run in a browser.
    ip : string (default = '127.0.0.1')
        IP address at which the HTML will be served.
    port : int
        The port at which to serve the HTML
    n_retries : int
        The number of nearby ports to search if the specified port is in use.
    debug : bool
        Run app in debug mode. Note that debug mode causes two tabs to open up.
    """
    port = find_open_port(ip, port, n_retries)

    open_browser(ip, port)
    app.run(host=ip, port=port, debug=debug)


def open_browser(ip, port):
    webbrowser.open('http://{0}:{1}'.format(ip, port))


def find_open_port(ip, port, n=50):
    """Find an open port near the specified port. """
    ports = itertools.chain((port + i for i in range(n)),
                            (port + random.randint(-2 * n, 2 * n)))

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        s.close()
        if result != 0:
            return port
    raise ValueError("no open ports found")
