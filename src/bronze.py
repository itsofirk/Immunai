import logging
from common.filesystem import get_raw_data_path, get_clean_data_path, load_json, dump_json

IN_VIVO = "In vivo"

logger = logging.getLogger(__name__)


def _is_relevant(entry):
    return entry["environment"]["name"] == IN_VIVO


def _extract_relevant_fields(entry):
    if "cell_response" not in entry:
        logger.warning(f"Missing cell_response for entry: {entry}")
        entry["cell_response"] = 0
    return {
        "cell_type": entry["cell_type"]["name"],
        "cell_response": entry.get("cell_response", 0)
    }


def process_raw_data(experiment_id):
    logger.info(f"Processing experiment {experiment_id}...")
    input_file_path = get_raw_data_path(experiment_id)

    logger.debug(f"Loading data from {input_file_path}...")
    raw_data = load_json(input_file_path)

    logger.debug(f"Filtering entries and extracting relevant fields...")
    necessary_data = [_extract_relevant_fields(entry) for entry in raw_data if _is_relevant(entry)]

    logger.debug(f"Dumping data to {get_clean_data_path(experiment_id)}...")
    output_file_path = get_clean_data_path(experiment_id)
    dump_json(output_file_path, necessary_data)
    logger.info(f"Done!")


__all__ = [process_raw_data]
