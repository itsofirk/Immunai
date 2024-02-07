from common.filesystem import get_clean_data_path, load_json, dump_json, get_hypothesis_data_path

NEURON = "Neuron"


def _collect_stats(data):
    """
    Returns the average neuron response and the number of neurons, the highest cell response, and the lowest neuron response
    """
    neuron_response_sum = 0
    neuron_number = 0
    lowest_neuron_response = float("inf")
    highest_cell_response = float("-inf")
    for entry in data:
        if entry["cell_type"] == NEURON:
            neuron_response_sum += entry["cell_response"]
            neuron_number += 1
            if entry["cell_response"] < lowest_neuron_response:
                lowest_neuron_response = entry["cell_response"]
        else:
            if entry["cell_response"] > highest_cell_response:
                highest_cell_response = entry["cell_response"]

    return (neuron_response_sum,
            neuron_number,
            highest_cell_response,
            lowest_neuron_response)


def _check_hypothesis(data):
    """
    Check whether non-neuron cells are above average or below the lowest neuron response
    """
    # Collect stats
    avg_neuron_response, highest_cell_response, lowest_neuron_response, neuron_number = _collect_stats(data)

    # Hypothesis check
    if neuron_number == 0:
        # TODO: add setting for this
        return False, False
    average = avg_neuron_response / neuron_number

    is_above_average = average > highest_cell_response
    is_below_min = lowest_neuron_response > highest_cell_response

    return is_below_min, is_above_average


def validate_hypothesis(experiment_id):
    input_file_path = get_clean_data_path(experiment_id)
    output_file_path = get_hypothesis_data_path(experiment_id)

    data = load_json(input_file_path)

    result = _check_hypothesis(data)

    results = {
        "below_min": result[0],
        "below_avg": result[1]
    }

    dump_json(output_file_path, results)


__all__ = [validate_hypothesis]