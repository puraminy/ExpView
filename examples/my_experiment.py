# example.py
import random
from expview import experiment, cli


@experiment
def my_experiment(run_args, exp_vars, results):
    """
    run_args → meta / infra configs (expid, save_path, seed, logging)
    exp_vars → actual experimental parameters
    results  → dict for metrics and artifacts
    """
    print(f"------------------- Experiment {run_args['expid']} ------------------------")
    for k, v in exp_vars.items():
        print(f"{k}: {v}")

    accuracy = round(random.uniform(0.4, 0.99), 2)
    results["accuracy"] = accuracy

    print("accuracy:", accuracy)


if __name__ == "__main__":
    cli()

