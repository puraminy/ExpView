# Exper

# Exper
> ⚠️ Note: This project is currently under active maintenance and refinement. 


## About
A terminal-based analytics and visualization tool inspired by spreadsheet interfaces like Excel, optimized for developers and data scientists. Easily expandable by user codes or plug-ins, open source. Displays columns of a pandas DataFrame directly in the terminal using the Curses library, with fast navigation, shortcut keys, and instant refresh.  

Exper integrates with experiment pipelines by passing variable configurations to external programs, collecting CSV outputs, Managing configs, and visualizing results with matplotlib to analyze parameter effects and performance trends. It is ideal for quickly exploring datasets, aggregating metrics, and generating plots without leaving the terminal.  

## Installation
to install the program clone it then go to Exper folder and run 
`pip install -e .`, 

This will install the expview and requirements

## Get Started
In the example folder, you can find an initial example on how to use it for a new experiment.
The code is repeated below:

```


```



## Exploring Experiment Results

Then running expview inside `logs` directory or any subdirectory including results wil search for the csv, tsv, or json files, merge them and shows the rusults in a tabular ui for navigation and applying analysis tools

```bash
expview 
```
### Screen shot of output

 link to a screen shot

## Ploting

expview offers manyfeatures and many features can plug-in to it or written by the user, as an example of a basic visulasation you can draw a plot for the example experiment above. 

navigate on the column `learning_rate` then hit X (shift + x) this set and highlight column as x index, then for ... hit Y (shift + y) it sets the column as y axis, if you have changed another variable like `batch_size` you can select it as legend using T (shift + t) now by hitting : the command prompt opens and you can enter `line` to draw line which is show below.
