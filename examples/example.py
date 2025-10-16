# example.py
import random
from expview import experiment_runner, cli

@experiment_runner
def dummy_experiment(args, results):
    """
    A simple experiment function to test the experiment_runner decorator.
    """
    print("Running dummy_experiment with args:")
    for k, v in args.items():
        print(f"  {k}: {v}")

    accuracy = round(random.uniform(0.4, 0.99), 2)
    results["accuracy"] = accuracy

    print("Accuracy:", accuracy)

if __name__ == "__main__":
    cli()

