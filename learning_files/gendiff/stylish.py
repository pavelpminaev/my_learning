"""Module for parsing data_of_file from .yml and .json files."""

import json
import os
import yaml


def get_ending(pathfile: str) -> str:
    """Function get ending of file."""

    return os.path.splitext(pathfile)[1]


def parsing_data(data_of_file, ending: str) -> dict or bool:
    """Checking opening file and return dictionary
    with data_of_file of .json or .yml file.
    """

    data_dict = {}
    try:
        if ending == '.yaml' or '.yml':
            data_dict = yaml.load(data_of_file, Loader=yaml.FullLoader)
        elif ending == '.json':
            data_dict = json.load(data_of_file)
        if data_dict is None:
            raise TypeError  # поднять TypeError
    except (TypeError, yaml.parser.ParserError):
        return False
    else:
        return data_dict


def get_data(pathfile: str) -> dict:
    """Open file and get parsing_data."""

    with open(pathfile, 'r') as data_of_file:
        return parsing_data(data_of_file, get_ending(pathfile))






"""Modul search difference between two collections"""



ERROR_MESSAGE = "Impossible to build difference. Check your files."


def make_diff(node1, node2):
    def get_difference(key):

        if key in deleted_keys:
            value = {'type': 'deleted', 'value': node1[key]}

        elif key in added_keys:
            value = {'type': 'added', 'value': node2[key]}

        elif key in changed_keys and node1[key] == node2[key]:
            value = {'type': 'unchanged', 'value': node1[key]}

        elif key in changed_keys and node1[key] != node2[key]:
            if isinstance(node1[key], dict) and isinstance(node2[key], dict):
                value = {'type': 'internal_change',
                         'value': make_diff(node1[key], node2[key])}
            else:
                value = {'type': 'changed_value',
                         'value': [node1[key], node2[key]]}

        return key, value

    all_keys = sorted(set.union(set(node1), set(node2)))
    deleted_keys = set(node1).difference(set(node2))
    added_keys = set(node2).difference(set(node1))
    changed_keys = set(node1).intersection(set(node2))

    return dict(map(get_difference, all_keys))


def generate_diff(path_first_file, path_second_file):
    data_of_first_file, data_of_second_file = \
        get_data(path_first_file), get_data(path_second_file)

    if (data_of_first_file is False) or (data_of_second_file is False):
        return ERROR_MESSAGE

    diff_dict = make_diff(data_of_first_file, data_of_second_file)

    return diff_dict


ft = '/Users/pavelminaev/my_learning/learning_files/gendiff/tree_files/tree1.json'
st = '/Users/pavelminaev/my_learning/learning_files/gendiff/tree_files/tree2.json'
gd = generate_diff(ft, st)




import itertools
import json


REPLACER = ' '
STEP = 2


def output(lines, space):
    return ''.join(itertools.chain(
                   '{\n', lines, space * REPLACER + '}'))

l = 'lines'
s = 1
print(output(l, s))

def lines_form(space, status_name, name, value):
    signs_dict = {'deleted': '-', 'added': '+', 'unchanged': ' '}
    sign = signs_dict[status_name]
    return (space + STEP) * REPLACER + f'{sign} {name}: {value}\n'


from colorama import init, Fore
init(autoreset=True)




def make_format(diff_dict):

    def get_value(val, space):

        if isinstance(val, dict):
            result_with_dict = []
            for k, v in val.items():
                line = '{}: {}\n'.format(k, get_value(v, space + 2 * STEP))
                result_with_dict.append((space + 2 * STEP) * REPLACER + line)
            return output(result_with_dict, space)

        if isinstance(val, bool) or val is None:
            return json.dumps(val)

        return str(val)

    def make_lines(item, space):
        name, attributes = item
        status = attributes['type']

        if status == 'internal_change':
            children = attributes['value']
            val = list(map(lambda item: make_lines(item, space + 2 * STEP),
                           children.items()))
            return lines_form(space, 'unchanged', name,
                              output(val, space + 2 * STEP))

        elif status == 'changed_value':
            val_del, val_add = attributes['value']

            first_line = lines_form(space, 'deleted', name,
                                    get_value(val_del, space + 2 * STEP))
            second_line = lines_form(space, 'added', name,
                                     get_value(val_add, space + 2 * STEP))
            print(Fore.GREEN + 'it s' + str(space) + '<-')
            return first_line + second_line

        val = attributes['value']
        return lines_form(space, status, name, get_value(val, space + 2 * STEP))

    result = list(map(lambda item: make_lines(item, 0),
                      diff_dict.items()))

    return output(result, 0)



print(make_format(gd))
