import pandas as pd
import numpy as np

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    l = 'SecondHighestSalary'
    N = 2
    employee.drop_duplicates(subset=['salary'],keep='first', inplace=True)
    if N > len(employee.index) or N < 1:
        return pd.DataFrame({l : np.NaN}, index=[0])
    employee.sort_values(by = 'salary', ascending= False, inplace=True)
    employee.rename(columns= {'salary': l}, inplace=True) 
    return employee.iloc[N-1:N][[l]]

print(second_highest_salary(employee))