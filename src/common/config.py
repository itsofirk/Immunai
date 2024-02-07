from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    raw_data_dir: str = '../../resources/raw_experiment_data/'
    processed_data_dir: str = '../../resources/processed_data/'
    validated_data_dir: str = '../resources/validated_data/'
