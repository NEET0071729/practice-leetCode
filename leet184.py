import pandas as pd

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

# def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
#     l = [0] * len(department.index)
#     for x in employee.index:
#         list_inddex = department[department["id"] == employee.loc[x, "departmentId"]].index
#         list_inddex = list_inddex[0]
#         if employee.loc[x, "salary"] >= l[list_inddex]:
#             l[list_inddex] = employee.loc[x, 'salary']
#         else:
#             continue
#     for x in employee.index:
#         list_inddex = department[department["id"] == employee.loc[x, "departmentId"]].index
#         list_inddex = list_inddex[0]
#         if employee.loc[x, "salary"] >= l[list_inddex]:
#             l[list_inddex] = employee.loc[x, 'salary']
#         else:
#             employee.drop(index=x, inplace=True)
#     employee.drop(columns="id", inplace=True)
#     employee.rename(columns={"departmentId": "id"}, inplace=True)
#     e2 = employee.merge(department,how='left', on="id")
#     e2.rename(columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"}, inplace=True)
#     return e2[["Department", "Employee", "Salary"]]

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e2 = employee.merge(department, how='left', left_on="departmentId", right_on="id")
    e2.columns = ["id", "Employee", "Salary", "dId", "id_y", "Name"]
    e3 = e2.groupby("dId")["Salary"].transform('max')
    e4 = e2.loc[e2.Salary == e3, ["Name", "Employee", "Salary"]]
    return e4

print(department_highest_salary(employee, department))