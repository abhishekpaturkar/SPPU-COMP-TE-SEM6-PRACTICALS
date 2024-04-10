import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Load Data
df = pd.read_csv('boston.csv')


print("----------------Dataframe Info-----------------------")
print(df.info())
print("\n")

print("----------------Dataframe Describe--------------------")
print(df.describe())
print("\n")

print("--------------First 10 Rows of Dataframe--------------")
print(df.head(10))
print("\n")


print("---------------Plot (RM vs MEDV)------------------")
df.plot.scatter('RM', 'MEDV', figsize = (6, 6))
plt.show()
print("\n")


print("----------------Heatmap-----------------------")
sns.heatmap(df.corr(), cmap = 'coolwarm', annot = True, fmt = '.1f')
plt.show()
print("\n")


# Lets focus at the last line, where y = MEDV:
# When shades of Blue: the more Blue color is on X axis, smaller the MEDV. Negative correlation
# When light colors: those variables at axis x and y, they dont have any relation. Zero correlation
# When shades of Red : the more Red color is on X axis, higher the MEDV. Positive correlation

print("======Trainning Linear Regression Model===========\n")
# X: Varibles named as predictors, independent variables, features.
# Y: Variable named as response or dependent variable

X = df[df.columns[:-1]]
Y = df['MEDV']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Split Dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

print("-------------Trained Dataset-------------------")
print(f'Train Dataset Size - X: {X_train.shape}, Y: {Y_train.shape}')
print(f'Test  Dataset Size - X: {X_test.shape}, Y: {Y_test.shape}')


print("-------------Test VS Prediction Model-------------------")
# Model Building
lm = LinearRegression()
lm.fit(X_train, Y_train)
predictions = lm.predict(X_test)

# Model Visualization
plt.figure(figsize=(6, 6))
plt.scatter(Y_test, predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.title('Test vs Prediction')
plt.show()
print("\n")


print("--------------Regression Line Tracing---------------------")
plt.figure(figsize=(6, 6))
sns.regplot(x=X_test[ :, 5], y=Y_test, scatter_kws={'s': 5})
plt.scatter(X_test[:, 5], predictions, marker='+')
plt.xlabel('Average number of rooms per dwelling')
plt.ylabel('Median value of owner-occupied homes')
plt.title('Regression Line Tracing')
plt.show()
print("\n")


