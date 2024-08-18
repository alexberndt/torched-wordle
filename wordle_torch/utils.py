from typing import List

def read_file(file_name) -> List:

    file_list = []

    with open(file_name) as file:
        while line := file.readline():
            file_list.append(line.rstrip())

    return file_list