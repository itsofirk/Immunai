import json
import os
from common import settings
from errors import ExperimentNotFoundError


def _get_local_json_file_path(directory, experiment_id):
    return os.path.join(directory, f'{experiment_id}.json')


def get_raw_data_path(experiment_id):
    return _get_local_json_file_path(settings.raw_data_dir, experiment_id)


def get_clean_data_path(experiment_id):
    return _get_local_json_file_path(settings.clean_data_dir, experiment_id)


def get_hypothesis_data_path(experiment_id):
    return _get_local_json_file_path(settings.hypothesis_dir, experiment_id)


def get_conclusion_data_path(experiment_id):
    return _get_local_json_file_path(settings.conclusion_dir, experiment_id)


def load_json(json_file_path):
    try:
        with open(json_file_path, 'r') as input_file:
            return json.load(input_file)
    except FileNotFoundError:
        raise ExperimentNotFoundError("File not found. Please check the experiment ID and try again.")


def dump_json(json_file_path, data):
    os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
    with open(json_file_path, 'w') as output_file:
        json.dump(data, output_file)
