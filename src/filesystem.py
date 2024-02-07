import os
from config import Settings

settings = Settings()


def get_raw_data_path(experiment_id):
    return os.path.join(settings.raw_data_dir, f'{experiment_id}.json')


def get_processed_data_path(experiment_id):
    return os.path.join(settings.processed_data_dir, f'{experiment_id}.json')


def get_validated_data_path(experiment_id):
    return os.path.join(settings.validated_data_dir, f'{experiment_id}.json')

