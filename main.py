import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'Dataset\titanic.csv')

# Basic info and description
print(df.info())
print(df.describe())

# Handling Missing Values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Dropping Duplicates
df = df.drop_duplicates()

# Filter data: Passengers in first class
first_class = df[df['Pclass'] == 1]
print("First Class Passengers: \n", first_class.head())

# Visualization: Survival rate by passenger class
def plot_survival_by_class(dataframe):
    survival_by_class = dataframe.groupby('Pclass')['Survived'].mean()
    survival_by_class.plot(kind='bar', color='skyblue')
    plt.title('Survival Rate by Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Survival Rate')
    plt.show()

# Visualization: Age distribution histogram
def plot_age_distribution(dataframe):
    sns.histplot(dataframe['Age'], kde=True, bins=20, color='purple')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

# Additional Exploratory Visualizations

# Survival rate by gender
def plot_survival_by_gender(dataframe):
    survival_by_gender = dataframe.groupby('Sex')['Survived'].mean()
    survival_by_gender.plot(kind='bar', color=['pink', 'lightblue'])
    plt.title('Survival Rate by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Survival Rate')
    plt.show()

# Survivors count by embarkation point
def plot_survivors_by_embarkation(dataframe):
    sns.countplot(x='Embarked', hue='Survived', data=dataframe, palette='Set1')
    plt.title('Survivors Count by Embarkation Point')
    plt.xlabel('Embarkation Point')
    plt.ylabel('Count')
    plt.show()

# Fare distribution by passenger class (boxplot)
def plot_fare_distribution_by_class(dataframe):
    sns.boxplot(x='Pclass', y='Fare', data=dataframe, palette='coolwarm')
    plt.title('Fare Distribution by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Fare')
    plt.show()

# Correlation heatmap among key features
def plot_correlation_heatmap(dataframe):
    numeric_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    corr = dataframe[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Call the plotting functions to visualize data
plot_survival_by_class(df)
plot_age_distribution(df)
plot_survival_by_gender(df)
plot_survivors_by_embarkation(df)
plot_fare_distribution_by_class(df)
plot_correlation_heatmap(df)
