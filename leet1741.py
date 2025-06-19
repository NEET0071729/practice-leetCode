import pandas as pd

data = [['1', '2020-11-28', '4', '32'], ['1', '2020-11-28', '55', '200'], ['1', '2020-12-3', '1', '42'], ['2', '2020-11-28', '3', '33'], ['2', '2020-12-9', '47', '74']]
employees = pd.DataFrame(data, columns=['emp_id', 'event_day', 'in_time', 'out_time']).astype({'emp_id':'Int64', 'event_day':'datetime64[ns]', 'in_time':'Int64', 'out_time':'Int64'})

# def total_time(employees: pd.DataFrame) -> pd.DataFrame:
#     employees['total_time'] = 0
#     print(employees)
#     for x in employees.index:
#         employees.iat[x, 4] = employees.iat[x, 3] - employees.iat[x, 2]
#     employees = employees.groupby(by=['emp_id', 'event_day']).sum()
#     employees.reset_index(inplace=True)
#     employees.rename(columns={'event_day': 'day'}, inplace=True)
#     return employees[['day', 'emp_id', 'total_time']]

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(by=['emp_id', 'event_day']).sum()
    employees.reset_index(inplace=True)
    employees.rename(columns={'event_day': 'day'}, inplace=True)
    return employees[['day', 'emp_id', 'total_time']]


print(total_time(employees))