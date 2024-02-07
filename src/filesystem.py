import json
import os
from config import Settings
from errors import ExperimentNotFoundError

settings = Settings()


def get_raw_data_path(experiment_id):
    return os.path.join(settings.raw_data_dir, f'{experiment_id}.json')


def get_processed_data_path(experiment_id):
    return os.path.join(settings.processed_data_dir, f'{experiment_id}.json')


def get_validated_data_path(experiment_id):
    return os.path.join(settings.validated_data_dir, f'{experiment_id}.json')


def get_raw_data(experiment_id):
    try:
        with open(get_raw_data_path(experiment_id), 'r') as input_file:
            return json.load(input_file)
    except FileNotFoundError:
        raise ExperimentNotFoundError("File not found. Please check the experiment ID and try again.")
