import os
from windows_import_workaround import init_logger
logger =init_logger()


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


def assemble_files_list(paths):
    files = list()
    for path in paths:
        new_files = files_finder(path)
        #logger.info(f"Found {len(new_files)} files in {path}")
        files.extend(new_files)
    return files
