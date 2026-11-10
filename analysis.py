import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv')
print("Total Sales:", df['Sales'].sum())
print(df.groupby('Region')['Sales'].sum())

plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Sales', data=df, estimator=sum)
plt.title('Sales by Region - West is Highest')
plt.savefig('sales_by_region.png')
print("Dashboard Ready!")