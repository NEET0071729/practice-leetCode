import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'salary']).astype({'Id':'Int64', 'salary':'Int64'})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    l = 'getNthHighestsalary(' + str(N) + ')'
    employee.drop_duplicates(subset=['salary'],keep='first', inplace=True)
    if N > len(employee.index):
        return pd.DataFrame({l : ''}, index=[0])
    employee.sort_values(by = 'salary', ascending= False, inplace=True)
    s = employee.iat[N-1, 1]
    return pd.DataFrame({ l : s}, index=[0])
print(nth_highest_salary(employee,2))