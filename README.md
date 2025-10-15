# ExpView

## About
A terminal-based analytics and visualization tool inspired by spreadsheet interfaces like Excel, optimized for developers and data scientists. Displays columns of a pandas DataFrame directly in the terminal using the Curses library, with fast navigation, shortcut keys, and instant refresh.  

ExpView integrates with experiment pipelines by passing variable configurations to external programs, collecting CSV outputs, and visualizing results with matplotlib to analyze parameter effects and performance trends. It is ideal for quickly exploring datasets, aggregating metrics, and generating plots without leaving the terminal.  

## Sample Dataset
A sample dataset `sample_experiments.csv` is included to demonstrate the tool’s capabilities. It contains synthetic experiment runs with multiple parameters, performance metrics, and dates. This dataset is suitable for:  

- Aggregation using pivot tables (e.g., average accuracy by model and optimizer)  
- Line and bar charts (e.g., accuracy trends over time, batch size vs. loss)  
- Quick filtering and sorting to analyze parameter effects  

Columns include:  
```
experiment_id, date, model, optimizer, learning_rate, batch_size, accuracy, loss, training_time, run_by
```
## Test

To test the tool with the sample dataset:

```bash
python show.py sample
```

This will load the dataset in the terminal interface, allowing you to:

- Navigate the DataFrame with arrow keys
- Sort and filter columns
- Generate basic matplotlib plots directly from the terminal
- Explore aggregations and trends interactively

