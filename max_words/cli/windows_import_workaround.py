import os
import sys


def init():
    """
    here I use a workaround for running under windows
    and avoiding to fix the import path, as __init__ does not work
    """
    my_path = 'C:\\Users\\nivw2\\PycharmProjects\\niv\\max_words'
    if os.path.isdir(my_path):
        sys.path.append(my_path)
    # executing this via the pycharm venv I get different path then the windows command line.
    try:
        from max_words import max_words
    except ImportError:
        import max_words
    return max_words


def init_logger():
    init()
    from max_words.app.utils.logger import logger
    return logger

