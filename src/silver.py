from common.filesystem import get_clean_data_path, load_json, dump_json, get_hypothesis_data_path

NEURON = "Neuron"


def get_neuron_stats(data):
    """
    Get average, min, max and number of neuron cells response from the data
    """
    neuron_response_list = []
    for entry in data:
        if entry["cell_type"] == NEURON:
            neuron_response_list.append(entry["cell_response"])
    return sum(neuron_response_list) / len(neuron_response_list), \
        min(neuron_response_list), \
        max(neuron_response_list), \
        len(neuron_response_list)


def validate_hypothesis(experiment_id):
    input_file_path = get_clean_data_path(experiment_id)
    output_file_path = get_hypothesis_data_path(experiment_id)
    data = load_json(input_file_path)

    # Get average, min, max and number of neuron cells
    neuron_avg, neuron_min, neuron_max, neuron_count = get_neuron_stats(data)

    # Check if the hypothesis is true
    above_avg_count, above_max_count, below_min_count = check_hypothesis(data, neuron_avg, neuron_max, neuron_min)

    results = prepare_results(above_avg_count, above_max_count, below_min_count, data, neuron_avg, neuron_count,
                              neuron_max, neuron_min)

    dump_json(output_file_path, results)


def prepare_results(above_avg_count, above_max_count, below_min_count, data, neuron_avg, neuron_count, neuron_max,
                    neuron_min):
    return {
        "below_min_count": below_min_count,
        "above_avg_count": above_avg_count,
        "above_max_count": above_max_count,
        "stats": {
            "neuron_min": neuron_min,
            "neuron_avg": neuron_avg,
            "neuron_max": neuron_max,
            "neuron_count": neuron_count,
            "total_count": len(data)
        }
    }


def check_hypothesis(data, neuron_avg, neuron_max, neuron_min):
    # Iterate over all non-neuron cells and check if they are above the average
    above_avg_count = 0
    below_min_count = 0
    above_max_count = 0
    for entry in data:
        if entry["cell_type"] != NEURON:
            if entry["cell_response"] < neuron_min:
                below_min_count += 1
            elif entry["cell_response"] > neuron_avg:
                above_avg_count += 1
            elif entry["cell_response"] > neuron_max:
                above_max_count += 1
    return above_avg_count, above_max_count, below_min_count


if __name__ == "__main__":
    _experiment_id = 'EXP_001'
    validate_hypothesis(_experiment_id)
