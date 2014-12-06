from argparse import ArgumentParser

from . import app
from . import build


parser = ArgumentParser()
parser.add_argument('action', nargs='?', default='build',
                    choices=['build', 'display'])
args = parser.parse_args()

if args.action == 'build':
    build.save_all_plots()

if args.action in ('build', 'display'):
    app.main()
