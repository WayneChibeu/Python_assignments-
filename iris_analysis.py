# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set plot style
sns.set_theme(style="whitegrid")

# ============================
# Task 1: Load and Explore the Dataset
# ============================
print("\n Loading Dataset...")

try:
    # Load Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame

    print("\n Dataset loaded successfully!\n")
    print(" First five rows:")
    print(df.head())

    print("\n Data Types:")
    print(df.dtypes)

    print("\n Missing Values Check:")
    print(df.isnull().sum())

    # No missing values to clean in this dataset
except Exception as e:
    print(f" Error loading dataset: {e}")

# ============================
# Task 2: Basic Data Analysis
# ============================

print("\n Basic Statistical Analysis:")

# Basic statistics
print(df.describe())

# Mapping target numbers to species names
species_map = dict(zip(range(3), iris.target_names))
df['species'] = df['target'].map(species_map)

# Grouping by species
grouped_species = df.groupby('species').mean()

print("\n Average measurements by species:")
print(grouped_species)

# Observations
print("\n Observations:")
print("- Setosa flowers have significantly smaller petals compared to Versicolor and Virginica.")
print("- Virginica generally has the largest measurements across most features.")

# ============================
# Task 3: Data Visualization
# ============================

# Line Chart: Sepal and Petal Length over sample index
plt.figure(figsize=(10,6))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', color='royalblue')
plt.plot(df.index, df['petal length (cm)'], label='Petal Length', color='orangered')
plt.title('Sepal and Petal Length Over Samples', fontsize=16)
plt.xlabel('Sample Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8,6))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='muted')
plt.title('Average Petal Length per Species', fontsize=16)
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

# Histogram: Distribution of Sepal Width
plt.figure(figsize=(8,6))
sns.histplot(df['sepal width (cm)'], kde=True, color='mediumseagreen', bins=20)
plt.title('Distribution of Sepal Width', fontsize=16)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='bright')
plt.title('Sepal Length vs Petal Length by Species', fontsize=16)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.show()

# ============================
# Final Conclusion
# ============================

print("\n Conclusion:")
print("- The Iris dataset is clean, with no missing data.")
print("- Clear distinctions exist among species based on petal and sepal measurements.")
print("- Virginica species tend to have the largest flower parts, while Setosa has the smallest.")
print("- Scatter plots show a strong positive correlation between sepal length and petal length.")
