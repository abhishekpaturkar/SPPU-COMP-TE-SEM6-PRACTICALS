import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("iris.data")

print("--------------Describe the Dataframe----------------------")
print(df.describe())
print("\n")

print("--------------Shape of the Dataframe----------------------")
print(df.shape)
print("\n")

print("--------------First 5 rows of the Dataframe----------------------")
print(df.head())
print("\n")

print("--------------Last 5 rows of the Dataframe----------------------")
print(df.tail())
print("\n")

print("--------------Mean of the First Column----------------------")
print(df["5.1"].mean())
print("\n")


print("--------------Histogram of the Dataframe (using 5 bins)----------------------")
df.hist(bins=5)
plt.show()
print("\n")

print("--------------Histogram of the Dataframe----------------------")
df.hist()
plt.show()
print("\n")

print("--------------Columns of the Dataframe----------------------")
print(df.columns)
print("\n")

print("--------------Minimum value from Each Column----------------------")
print(df.min())
print("\n")

print("--------------Maximum value from Each Column----------------------")
print(df.max())
print("\n")

print("--------------Quantile of the Dataframe----------------------")
print(df.quantile([0, 0.25, 0.5, 0.75, 1.0], numeric_only=True))
print("\n")

print("--------------Correlation of the Dataframe----------------------")
iris_long = pd.melt(df, id_vars='5.1')
ax = sns.boxplot(x="5.1", y="value", hue="variable", data=iris_long)
plt.show()

print("--------------Frequecy of each value in the first column----------------------")
print(df['5.1'].value_counts())
print("\n")

print("--------------Density plot for 5.1 column----------------------")
df['5.1'].plot.density(color='green')
plt.title('Density plot for 5.1 column')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
print("\n")

print("--------------Heatmap for the Correlation----------------------")
subset_df = df.iloc[:, :4]
plt.figure(figsize=(8, 6))
sns.heatmap(subset_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
