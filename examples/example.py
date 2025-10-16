# example.py
from expview import experiment_runner, cli

@experiment_runner
def dummy_experiment(args, df):
    """
    A simple experiment function to test the experiment_runner decorator.
    It just prints its received arguments.
    """
    print("Running dummy_experiment with args:")
    for k, v in args.items():
        print(f"  {k}: {v}")

if __name__ == "__main__":
    cli()

