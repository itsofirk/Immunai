from common.filesystem import load_json


def summarize_hypothesis_accuracy(hypothesis_data_files):
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
    print(f"Hypothesis is true for: {below_avg_accuracy}% of experiments looking on the average response for {total_experiments} experiments.")


if __name__ == "__main__":
    import os

    results_path = '../resources/validated_data'
    hypothesis_data_files = [os.path.join(results_path, filename) for filename in os.listdir(results_path)]
    summarize_hypothesis_accuracy(hypothesis_data_files)
