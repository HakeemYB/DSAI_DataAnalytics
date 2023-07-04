import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = pd.read_csv('provincial-number-of-government-employees-by-grade-and-sex.csv')

# Step 2: Data Exploration and Preparation
data['Male'] = pd.to_numeric(data['Male'], errors='coerce')
data['Female'] = pd.to_numeric(data['Female'], errors='coerce')
data['Year'] = pd.to_datetime(data['Year'], format='%Y', errors='coerce')

# Step 3: Data Analysis and Visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Plot 1: Total Number of Government Employees by Province
total_employees_by_province = data.groupby('Province')[['Male', 'Female']].sum().sum(axis=1)
axes[0, 0].bar(total_employees_by_province.index, total_employees_by_province.values, color='blue')
axes[0, 0].set_xlabel('Province')
axes[0, 0].set_ylabel('Total Number of Employees')
axes[0, 0].set_title('Total Number of Government Employees by Province')

# Plot 2: Distribution of Government Employees by Grade
grade_counts = data['Grade'].value_counts()
axes[0, 1].pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', radius=2, startangle=90, pctdistance=0.8)
axes[0, 1].axis('equal')
axes[0, 1].set_title('Distribution of Government Employees by Grade')

# Plot 3: Trend of Government Employees Over Time
total_employees_over_time = data.groupby('Year')[['Male', 'Female']].sum().sum(axis=1)
axes[1, 0].plot(total_employees_over_time, marker='o')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Total Number of Employees')
axes[1, 0].set_title('Trend of Government Employees Over Time')
axes[1, 0].grid(True)

# Remove empty subplot
fig.delaxes(axes[1, 1])

# Adjust spacing between subplots
plt.tight_layout()

# Step 4: Data Insights and Communication
plt.show()
