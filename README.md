# Function Plotter

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A GUI python project that allows you to draw graphs also has validation for user input.

## Installation

Clone the repo and install dependencies with python package manger pip

```bash
git clone https://github.com/omarfareed/function-plotter
cd function-plotter/
sudo pip3 install -r requirements.txt
```

For Windows

```bash
pip install -r requirements.txt
```

## Usage

### run the application

```bash
python application.py
```

### test the application

```bash
pytest -v
```

#### Test Result

![Result of testing](./images/testing.PNG)

## Features

1. drawing the graph
2. determine the range you want

## Snapshots

### Validation

#### Empty fields

![Empty validation](./images/emptyInputs.PNG)

#### Wrong Input Values

##### Wrong Range

![Wrong Range](./images/wrongRange.PNG)

##### Invalid Range Values

![Wrong Range Value](./images/invalidRangeValues.PNG)

##### Wrong Expression

![Wrong Expression](./images/wrongExpression.PNG)

### Plotting

![graph](./images/plot.PNG)
