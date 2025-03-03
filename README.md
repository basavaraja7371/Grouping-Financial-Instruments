# Grouping Financial instruments.
## Objective
Here in this project we choose a financial data from yahoo finance. We create a data set by using
this data and some feature engineering.  The main objective of this project is to capture behaviour
of different financial instruments in the market. Mainly to cluster the instruments into three
clusters which may be

- High risk and high return
- Low risk and low return
- Neutral

We create out data capturing the return, volatility of the prices and volume and group them into
clusters and see if there is any groups.  This is usefull in portfolio creation and analysis. You
can analyse how the funds are allocated to different sectors to eliminate risk.

## Data
The data contain `Price` , `Open` , `High` , `Low` , `Close` and `Volume` for different stocks in
SP&500 and additional instruments such as bonds, crypto and indexes (tickers) from 2018-01-01 to
2023-01-01.

Using this dataset, we create our own dataset. We take the tickers. We create new features such as from the dataset for all the
1. Returns : annual average of the close price.
2. Volatility : annual standard deviation of the stocks.
3. Sharpe_ratio : the ratio of the above two.
4. Momentum_30 : thirty day average of the returns.
These four should capture the price movements fairly.
