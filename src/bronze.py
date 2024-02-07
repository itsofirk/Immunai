from common.filesystem import get_raw_data_path, get_clean_data_path, load_json, dump_json


def process_experiment(experiment_id):
    input_file_path = get_raw_data_path(experiment_id)
    raw_data = load_json(input_file_path)

    necessary_data = []

    for entry in raw_data:
        if entry["environment"]["name"] == "In vivo":
            relevant_data = {
                "cell_type": entry["cell_type"]["name"],
                "cell_response": entry["cell_response"]
            }

            necessary_data.append(relevant_data)

    output_file_path = get_clean_data_path(experiment_id)
    dump_json(output_file_path, necessary_data)


if __name__ == "__main__":
    _experiment_id = 'EXP_001'
    process_experiment(_experiment_id)
