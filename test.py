import pandas as pd

X_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
tt_train = pd.read_csv(r"C:\Users\gaura\OneDrive\Desktop\Code\PracticePython\dataforkgl\test.csv")
X_0_test = tt_train[X_columns]

X_0_test['Embarked'] = X_0_test['Embarked'].fillna(X_0_test['Embarked'].mode()[0])


print(tt_train['Embarked'].isnull().sort_values())