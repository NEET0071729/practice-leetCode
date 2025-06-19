import pandas as pd
import numpy as np
data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id':'Int64', 'income':'Int64'})

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category']= accounts['income'].apply(lambda x: 'Low Salary' if x<20000 else 'Average Salary' if x >=20000 and x<=50000 else 'High Salary' if x> 50000 else '')
    accounts= accounts.groupby(by='category').size().reset_index().rename(columns={0:'accounts_count'})
    accounts2 = pd.DataFrame(['Low Salary', 'Average Salary', 'High Salary'], columns=['category']).astype({'category': 'str'})
    accounts3= accounts2.merge(accounts, how='left', on='category')
    return accounts3.fillna(0)

print(count_salary_categories(accounts))