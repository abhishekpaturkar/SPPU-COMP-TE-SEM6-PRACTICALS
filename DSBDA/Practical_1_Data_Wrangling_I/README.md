`````markdown
# Data Wrangling in Python

This Python script performs various data wrangling techniques on a dataset stored in `autodata.csv`.

# Data Wrangling in Python

This Python script performs various data wrangling techniques on a dataset stored in `autodata.csv`.

## Instructions to Run

1. Ensure you have Python installed on your system. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

2. Install the required libraries by running the following command in your terminal or command prompt:

````bash
pip install pandas numpy matplotlib


## Code Overview

The script starts by importing required libraries like Pandas, NumPy, and Matplotlib.

```python
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot
````
`````

````

It then loads the dataset into a Pandas DataFrame and prints some basic information about the data like:

- DataFrame info()
- Descriptive statistics
- First 10 rows
- Last 5 rows

```python
# Data Loading
df = pd.read_csv('autodata.csv')

# Data Information
print(df.info())
print(df.describe())
print(df.head(10))
print(df.tail())
```

## Data Preprocessing

Several data preprocessing steps are applied:

- Counting null values in each column
- Replacing null values in `stroke` column with mean
- Replacing null values in `horsepower` column with mean
- Filling null values in `num-of-doors` column with mode
- Dropping rows with null values in `horsepower-binned` column

This handles all the missing values in the dataset.

```python
# Count null values
print(df.isnull().sum())

# Impute mean for stroke
mean_stroke = df["stroke"].mean()
df["stroke"].fillna(mean_stroke, inplace=True)

# Impute mean for horsepower
mean_hp = df["horsepower"].mean()
df["horsepower"].fillna(mean_hp, inplace=True)

# Impute mode for num-of-doors
mode = df["num-of-doors"].mode()[0]
df["num-of-doors"].fillna(mode, inplace=True)

# Drop rows with missing horsepower-binned
df.dropna(subset=["horsepower-binned"], inplace=True)
```

## Data Standardization

The `city-mpg` and `highway-mpg` columns are standardized by converting to liters per 100 km. This standardizes the fuel consumption measures.

```python
df["city-L/100km"] = 235/df["city-mpg"]
df["highway-L/100km"] = 235/df["highway-mpg"]
```

## Data Normalization

The `length`, `width`, and `height` columns are normalized to the range 0-1 using min-max scaling. This standardizes disparate measures to a common scale.

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[["length", "width", "height"]] = scaler.fit_transform(df[["length", "width", "height"]])
```

## Encoding Categorical Data

The categorical `aspiration` column is encoded into two numeric columns using one-hot encoding. This converts the textual labels to numbers that can be used in models.

```python
aspiration_dummies = pd.get_dummies(df['aspiration'])
df = pd.concat([df, aspiration_dummies], axis=1)
```

## Binning

The `horsepower` column is binned into buckets like "Low", "Medium", and "High" using Pandas `cut()`. This groups the continuous values into discrete bins.

```python
bins = [0, 100, 200, 500]
labels = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=labels)
```

The binned values are visualized in a bar chart.

```python
df['horsepower-binned'].value_counts().plot(kind='bar')
```

This covers the major data wrangling operations like handling missing data, encoding categories, normalization/standardization, and binning. The processed data is now ready for machine learning modeling.
````
