import pandas as pd

file_customers = "customers.csv"
file_orders = "orders.csv"
file_products = "products.csv"

dfc = pd.read_csv(file_customers, sep=',', header=0)
dfc = dfc.drop_duplicates().dropna()

dfo = pd.read_csv(file_orders, sep=',', header=0)
dfo = dfo.drop_duplicates().dropna()

dfp = pd.read_csv(file_products, sep=',', header=0)
dfp = dfp.drop_duplicates().dropna()

dfc[['First', 'Last']] = dfc['CustomerName'].str.split(pat=' ', expand=True).loc[:, [0, 1]]
dfc = dfc.dropna()

customer_id_john = dfc.loc[dfc['First'] == 'John']['CustomerID'].to_list()
dfo = dfo.loc[dfo['CustomerID'].isin(customer_id_john)].drop(columns=['CustomerID', 'OrderID', 'OrderStatus', 'OrderDate', 'TotalAmount'])


