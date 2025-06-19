import pandas as pd

data = [['2020-05-30', 'Headphone'], ['2020-06-01', 'Pencil'], ['2020-06-02', 'Mask'], ['2020-05-30', 'Basketball'], ['2020-06-01', 'Bible'], ['2020-06-02', 'Mask'], ['2020-05-30', 'T-Shirt']]
activities = pd.DataFrame(data, columns=['sell_date', 'product']).astype({'sell_date':'datetime64[ns]', 'product':'object'})

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.sort_values(by=['sell_date', 'product'], inplace=True)
    activities.drop_duplicates(subset=['sell_date', 'product'], inplace=True)
    activities = activities.groupby(by= 'sell_date')['product'].agg([('num_sold', 'nunique'), ('products', lambda x : ','.join(x))])
    activities.reset_index(inplace=True)
    # activities2 = activities.groupby(by='sell_date')['product'].count().reset_index()
    # activities2.rename(columns={'product':'num_sold'}, inplace=True)
    # activities1 = activities.groupby(by='sell_date')['product'].apply(lambda x : ','.join(x)).reset_index()
    # activities1 = activities1.rename(columns={'product':'products'})
    # activities1['num_sold'] = activities2['num_sold']
    # return activities1[['sell_date', 'num_sold', 'products']]
    return activities[['sell_date', 'num_sold', 'products']]

print(categorize_products(activities))