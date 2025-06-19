import pandas as pd

data = [[0, 95, 100, 105], [1, 70, None, 80]]
products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype({'product_id':'Int64', 'store1':'Int64', 'store2':'Int64', 'store3':'Int64'})

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars='product_id', value_vars=['store1', 'store2', 'store3'],var_name='store', value_name='price',ignore_index=True).dropna()
    return products

print(rearrange_products_table(products))