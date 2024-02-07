from common.filesystem import get_raw_data_path, get_clean_data_path, load_json, dump_json

IN_VIVO = "In vivo"


def is_relevant(entry):
    return entry["environment"]["name"] == IN_VIVO


def extract_relevant_fields(entry):
    return {
        "cell_type": entry["cell_type"]["name"],
        "cell_response": entry["cell_response"]
    }


def process_experiment(experiment_id):
    input_file_path = get_raw_data_path(experiment_id)
    raw_data = load_json(input_file_path)

    necessary_data = [extract_relevant_fields(entry) for entry in raw_data if is_relevant(entry)]

    output_file_path = get_clean_data_path(experiment_id)
    dump_json(output_file_path, necessary_data)


if __name__ == "__main__":
    _experiment_id = 'EXP_001'
    process_experiment(_experiment_id)
