# Function Plotter

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/60b8e0742c4044d6b35eb7e27ecb7a4b)](https://app.codacy.com/gh/aboueleyes/cms-downloader?utm_source=github.com&utm_medium=referral&utm_content=aboueleyes/cms-downloader&utm_campaign=Badge_Grade_Settings)
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
