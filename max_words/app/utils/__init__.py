import os
from windows_import_workaround import init
init()
from max_words.app.utils.logger import logger

def files_finder(path):
    files_in_path = list()
    if os.path.isfile(path):
        files_in_path.append(path)
    for dp, dn, files in os.walk(path):
        if len(files) == 0:
            continue
        #logger.debug(f"Files in directory: {files}")
        for file in files:
            files_in_path.append(os.path.join(dp, file))
    return files_in_path


def assemble_files_list(paths, max_files=None):
    files = list()
    for path in paths:
        new_files = files_finder(path)
        files.extend(new_files)
    if max_files is not None:
        logger.debug(f"For debugging using only {max_files} files")
        files = files[:max_files]
    logger.info(f"Found {len(files)} files in {path}")
    return files

def sum_dic(first_dic, second_dic):
    for first_word, first_freq in first_dic.items():
        if first_word in second_dic:
            first_dic[first_word] += second_dic.pop(first_word)
    first_dic.update(second_dic)
    return first_dic
