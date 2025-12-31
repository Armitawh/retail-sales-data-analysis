import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday'],
    'Temperature': [20, 25, 22, 30, 28, 32, 18],
    'Sunny': ['No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No'],
    'Sales': [30, 50, 35, 70, 60, 80, 20]
}

df = pd.DataFrame(data)

print(df.info())
print(df.head())
print(df.describe())

# Mean, median, and standard deviation for Temperature and Sales
mean_temp = df['Temperature'].mean()
median_temp = df['Temperature'].median()
std_temp = df['Temperature'].std()

mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
std_sales = df['Sales'].std()

print(f"Temperature - Mean: {mean_temp:.2f}, Median: {median_temp:.2f}, Std Dev: {std_temp:.2f}")
print(f"Sales - Mean: {mean_sales:.2f}, Median: {median_sales:.2f}, Std Dev: {std_sales:.2f}")

# Histogram of Sales
plt.figure(figsize=(8, 5))
sns.histplot(df['Sales'], bins=5, kde=True)
plt.title('Distribution of Lemonade Sales')
plt.xlabel('Sales (Cups)')
plt.ylabel('Frequency')
plt.show()

# Scatterplot: Sales vs. Temperature
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Temperature', y='Sales', hue='Sunny', data=df)
plt.title('Sales vs. Temperature')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Sales (Cups)')
plt.show()

# Barplot: Average Sales by Weather Condition
plt.figure(figsize=(8, 5))
sns.barplot(x='Sunny', y='Sales', data=df)
plt.title('Average Sales by Weather Condition')
plt.xlabel('Sunny (Yes/No)')
plt.ylabel('Average Sales (Cups)')
plt.show()

# Correlation
correlation = df['Temperature'].corr(df['Sales'])
print(f"Correlation between Temperature and Sales: {correlation:.2f}")
