import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))


def get_test_data(file_name):
    data_file = os.path.join(current_dir, '..', 'data', file_name)
    with open(data_file, 'r') as json_file:
        data = json.load(json_file)
    return data
