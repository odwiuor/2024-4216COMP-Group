# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace the file path with the actual path to your CSV file
file_path = '/home/victa/Downloads/archive/vgchartz-2024.csv'
df = pd.read_csv(file_path)

# Step 3: Data Analysis
# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Step 4: Data Visualization
plt.figure(figsize=(8, 6))
sns.histplot(df['column_name'], bins=20, kde=True)
plt.title('Histogram of Column Name')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# Example: Scatter plot of two numerical features
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_sales', y='genre', data=df)
plt.title('Scatter Plot of total_sales vs genre')
plt.xlabel('total_sales')
plt.ylabel('genre')
plt.show()

# Step 6: Main Execution
if __name__ == "__main__":
    pass  
