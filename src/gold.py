import logging
from common.filesystem import load_json

logger = logging.getLogger(__name__)


def summarize_hypothesis_accuracy(hypothesis_data_files):
    logger.info("Summarizing hypothesis accuracy...")

    total_experiments = 0
    below_min = 0
    below_avg = 0
    for filename in hypothesis_data_files:
        total_experiments += 1
        data = load_json(filename)
        if data["below_min"]:
            below_min += 1
        if data["below_avg"]:
            below_avg += 1

    below_min_accuracy = (below_min / total_experiments) * 100
    below_avg_accuracy = (below_avg / total_experiments) * 100
    print(f"Hypothesis is true for: {below_min_accuracy}% for {total_experiments} experiments.")
    print(f"Hypothesis is true for: {below_avg_accuracy}% looking on the average response for {total_experiments} experiments.")
    logger.info("Done!")


__all__ = [summarize_hypothesis_accuracy]
