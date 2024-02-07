from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    raw_data_dir: str = '../resources/raw_experiment_data/'
    clean_data_dir: str = '../resources/data/'
    hypothesis_dir: str = '../resources/validated_data/'
    conclusion_dir: str = '../resources/conclusion/'

    logging_level: str = "INFO"
