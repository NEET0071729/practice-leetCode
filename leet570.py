import pandas as pd

data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 100], [103, 'James', 'A', 100], [104, 'Amy', 'A', 100], [105, 'Anne', 'A', 100], [106, 'Ron', 'B', 100]]
employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype({'id':'Int64', 'name':'object', 'department':'object', 'managerId':'Int64'})

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    man = employee.groupby(by='managerId').size().reset_index().rename(columns={0 : 'cnt'})
    man = man[man['cnt']>=5]
    man = man[['managerId']].reset_index(drop=True)
    if man['managerId'].isin(employee['id']).any():
        employee = employee.merge(man, how='right', left_on='id', right_on='managerId')
    else:
        employee = employee.merge(man, how='right', left_on='id', right_on='managerId')
        employee = employee[['name']].dropna()
    return employee[['name']]

print(find_managers(employee))