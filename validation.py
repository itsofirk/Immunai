from bronze import process_raw_data
from silver import validate_hypothesis
from gold import summarize_hypothesis_accuracy

VALIDATED_DATA_DIR = "resources/validated_data"

experiments_files = [
    "EXP_001",
    "EXP_002",
    "EXP_003",
    "EXP_004_BAD_FORMAT",
]

for experiment_file in experiments_files:
    process_raw_data(experiment_file)
    validate_hypothesis(experiment_file)

experiments_files = [f"{VALIDATED_DATA_DIR}/{filename}.json" for filename in experiments_files]
summarize_hypothesis_accuracy(experiments_files)
