import pandas as pd

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby(by='customer_number', as_index=False)['order_number'].count().sort_values(by='order_number', ascending=False).head(1)
    return orders[['customer_number']]

print(largest_orders(orders))