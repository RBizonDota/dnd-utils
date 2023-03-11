import argparse
from enum import Enum

from dnd_utils import __app_name__, __version__
from dnd_utils.cli_client.client import CLIClient
from dnd_utils.utils import LogLevel


parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument('-h', '--help', action='help')
parser.add_argument("-v", "--version", action="version", version=f"{__app_name__} version {__version__}")
# TODO: parser.add_argument('-c', '--command', help='Runs the command')
parser.add_argument("-ll", "--log-level", help="Sets log level", type=LogLevel)


def main(args: argparse.Namespace):
    CLIClient(args.log_level).cmdloop()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
