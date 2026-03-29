import pandas as pd
import matplotlib.pyplot as plt

ETH_Analysis = pd.read_csv("ETH.csv")

print(ETH_Analysis.head())
ETH_Analysis['date'] = pd.to_datetime(ETH_Analysis['date'])
ETH_Analysis.head()
ETH_Analysis.info()
ETH_Analysis.describe()

plt.plot(ETH_Analysis['close'])
plt.title("Ethereum Price Trend")
plt.show()

ETH_Analysis.loc[ETH_Analysis['volume'].idxmax()]
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ETH_Analysis = pd.read_csv("C:/Users/HP/Downloads/ADA.csv")

correlation = ETH_Analysis[['open','high','low','close','volume']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Price Correlation Heatmap")
plt.show()

ETH_Analysis['date'] = pd.to_datetime(ETH_Analysis['date'])

ETH_Analysis['year'] = ETH_Analysis['date'].dt.year
ETH_Analysis['month'] = ETH_Analysis['date'].dt.month

pivot = ETH_Analysis.pivot_table(values='close', index='year', columns='month')

plt.figure(figsize=(12,6))
sns.heatmap(pivot, cmap='YlGnBu')
plt.title("Monthly Ethereum Price Heatmap")
plt.show()
ETH_Analysis['volatility'] = ETH_Analysis['high'] - ETH_Analysis['low']

pivot = ETH_Analysis.pivot_table(values='volatility', index='year', columns='month')

sns.heatmap(pivot, cmap='Reds')
plt.title("Ethereum Volatility Heatmap")
plt.show()
