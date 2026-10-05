import sys
import numpy as np

print("Python:", sys.version)

import pandas
import matplotlib
import seaborn
import joblib
import streamlit
import sklearn

print(
    "pandas", pandas.__version__,
    "| numpy", np.__version__,
    "| matplotlib", matplotlib.__version__,
    "| seaborn", seaborn.__version__
)

print(
    "scikit-learn", sklearn.__version__,
    "| streamlit", streamlit.__version__
)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

rng = np.random.default_rng(42)

X = rng.random((300, 4))

y = (
    X @ np.array([3.0, 2.0, 1.0, 0.5])
    + rng.normal(0, 0.1, 300)
)

for model in (
    LinearRegression(),
    RandomForestRegressor(
        n_estimators=30,
        random_state=42
    ),
    GradientBoostingRegressor(
        random_state=42
    )
):

    model.fit(X, y)

    print(
        type(model).__name__,
        "OK, train R2 =",
        round(model.score(X, y), 3)
    )

print("ALL CHECKS PASSED")