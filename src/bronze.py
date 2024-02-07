from common.filesystem import get_raw_data_path, get_clean_data_path, load_json, dump_json

IN_VIVO = "In vivo"


def _is_relevant(entry):
    return entry["environment"]["name"] == IN_VIVO


def _extract_relevant_fields(entry):
    if "cell_response" not in entry:
        print(f"Missing cell_response for entry: {entry}")
        entry["cell_response"] = 0
    return {
        "cell_type": entry["cell_type"]["name"],
        "cell_response": entry.get("cell_response", 0)
    }


def process_raw_data(experiment_id):
    input_file_path = get_raw_data_path(experiment_id)
    raw_data = load_json(input_file_path)

    necessary_data = [_extract_relevant_fields(entry) for entry in raw_data if _is_relevant(entry)]

    output_file_path = get_clean_data_path(experiment_id)
    dump_json(output_file_path, necessary_data)


__all__ = [process_raw_data]
