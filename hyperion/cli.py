# !/usr/bin/python3
# -*- coding: utf-8 -*-

""" Creates/updates EOS db from files """

import argparse

from logs.logger import get_custom_logger
from models.create import Creator
from models.meta import MetaRunner
from models.update import Updater

LOGGER = get_custom_logger('CLI')
AVAILABLE_MODES = {
    'update': Updater(),
    'create': Creator()
}


def create_args():
    """
    :return: ArgumentParser
        Parser that handles cmd arguments.
    """

    parser = argparse.ArgumentParser(usage='-m <run mode> '
                                           '-h for full usage')

    available_modes = ','.join(AVAILABLE_MODES.keys())
    help_message = 'running mode, must be in ' + available_modes
    parser.add_argument('-m', dest='run_mode',
                        help=help_message, required=True)

    return parser


def parse_args(parser):
    """
    :param parser: ArgumentParser
        Object that holds cmd arguments.
    :return: tuple
        Values of arguments.
    """

    args = parser.parse_args()

    run_mode = str(args.run_mode)
    assert run_mode in AVAILABLE_MODES

    return run_mode


def get_runner(run_mode) -> MetaRunner:
    return AVAILABLE_MODES[run_mode]


def main():
    run_mode = parse_args(create_args())  # parse mode
    runner = get_runner(run_mode)  # create runner
    runner.run()  # run


if __name__ == '__main__':
    main()
