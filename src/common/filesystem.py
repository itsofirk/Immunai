import json
import os
from common import settings
from errors import ExperimentNotFoundError


def get_raw_data_path(experiment_id):
    return os.path.join(settings.raw_data_dir, f'{experiment_id}.json')


def get_processed_data_path(experiment_id):
    return os.path.join(settings.processed_data_dir, f'{experiment_id}.json')


def get_validated_data_path(experiment_id):
    return os.path.join(settings.validated_data_dir, f'{experiment_id}.json')


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
