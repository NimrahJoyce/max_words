from multiprocessing import Pool
from windows_import_workaround import init
init()
from max_words.app.utils.logger import logger
from max_words.app.utils import assemble_files_list
from max_words.app.words_in_file import words_in_file
from collections import OrderedDict
from operator import itemgetter


def sort_dict(dict):
    return OrderedDict(sorted(dict.items(), key=itemgetter(1), reverse=True))


def get_max_items(dict, max):
    response = list()
    for index, pair in enumerate(dict.items()):
        if index == max:
            break
        response.append(pair)
    return response


def single_proc(max, paths):
    files = assemble_files_list(paths)
    found_words = dict()
    for current_file in files:
        try: #some windows log files have permission issues
            current_words = words_in_file(current_file)
            for word, freq in found_words.items():
                if word in current_words:
                    found_words[word] += current_words.pop(word)
            found_words.update(current_words)
            sorted_words = sort_dict(found_words)
        except PermissionError:
            logger.warn(f"Failed to open {current_file} due to PermissionError")
            continue
            #logger.debug(found_words.items())
        #logger.debug(sorted_words.items())
        result = get_max_items(sorted_words, max)
    print(f"Maximum {max} words:")
    for item in result:
        print(f"{item[0]} occurred {item[1]} times")


def parallel_proc(max,paths):
    files = assemble_files_list(paths)
    p = Pool(len(files))
    for current_file in files:
        result = p.map(words_in_file, current_file)


def main(max, paths):
    single_proc(max, paths)
