import pandas as pd

data = [[1, 2, 3], [1, 2, 4], [1, 3, 3], [2, 1, 1], [2, 2, 1], [2, 3, 1], [2, 4, 1]]
teacher = pd.DataFrame(data, columns=['teacher_id', 'subject_id', 'dept_id']).astype({'teacher_id':'Int64', 'subject_id':'Int64', 'dept_id':'Int64'})

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher.drop_duplicates(subset=['teacher_id', 'subject_id'],keep='first', inplace=True)
    teacher = teacher.groupby(by='teacher_id').count()
    teacher.reset_index(inplace=True)
    teacher.rename(columns={'subject_id':'cnt'}, inplace=True)
    return teacher[['teacher_id', 'cnt']]

print(count_unique_subjects(teacher))