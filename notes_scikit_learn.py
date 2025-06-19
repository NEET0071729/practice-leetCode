from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt

print(load_diabetes()['DESCR'])
X , y = load_diabetes(return_X_y=True)
X_new = StandardScaler().fit_transform(X)
plt.scatter(X[:, 0], X[:, 1], c=y)
mod = KNeighborsRegressor()
pipe = Pipeline([
    ("model", mod.set_params(n_neighbors = 5))
])

mod = GridSearchCV(estimator=pipe,
                   param_grid={'model__n_neighbors': [1, 2, 3, 4, 5]},
                   cv=3)

mod.fit(X_new, y)
pred = mod.predict(X_new)
# plt.scatter(pred, y)
plt.show()

# pipe.fit(X, y)
# pred = pipe.predict(X)
# plt.scatter(pred, y)
# plt.show()

# print(pipe.get_params())
