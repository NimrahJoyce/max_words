import argparse
import os
# This works in windows command line
from windows_import_workaround import init
init()

from max_words.app.utils.logger import logger
from max_words.app.main import main


def init():
    parser = argparse.ArgumentParser(prog='Max_words')
    parser.add_argument('max', metavar='N', type=int, nargs='?',
                        help='An integer representing how many maximum occurred words to print.')
    parser.add_argument('paths', nargs='+', help='A list of paths that represent the directories or files to'
                                                 ' traverse')
    return parser.parse_args()


def validate_args():
    args = init()
    if args.max is None:
        logger.error('Missing max integer argument')
        logger.error('usage: Max_words [-h] [N] paths')
        raise Exception
    if len(args.paths) == 0:
        logger.error('Missing paths argument')
        logger.error('usage: Max_words [-h] [N] paths')
        raise Exception
    for path in args.paths:
        if not os.path.isfile(path) and not os.path.isdir(path):
            logger.error(f"Path {path} does not exist. stopping execution")
            raise Exception
    return args


if __name__ == '__main__':
    args = validate_args()
    logger.info(f"Got these args: {args}")
    main(args.max, args.paths)
