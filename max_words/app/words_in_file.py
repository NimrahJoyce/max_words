import os
import string
from pprint import pprint


from windows_import_workaround import init
init()
from max_words.app.utils.logger import logger


def remove_unprintable(word):
    """
    In windows log files I found some characters that caused problems
    So here I fix it.
    """
    return ''.join([ch for ch in word if ch in string.printable])


def words_in_file(file_w_path):
    found_words = dict()
    logger.info(f"Processing {file_w_path}")
    # windows had unicode decode issues in the logs directory
    # so I used the ignore errors flag here.
    with open(file_w_path,errors='ignore') as fd:
        for line in fd.readlines():
            for word in line.split():
                word = remove_unprintable(word)
                #logger.debug(f"Found {word}")
                if word in found_words:
                    found_words[word] += 1
                else:
                    found_words[word] = 1
    return found_words
