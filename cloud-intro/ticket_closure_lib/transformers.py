from typing import Dict

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class OrdinalConverter(BaseEstimator, TransformerMixin):
    """
    For categoricals where we know the appropriate
    ordering, convert to integer manually instetad of
    allowing OrdinalEncoder to make itt up based
    on the order of occurrence in the data.
    """

    def __init__(self, feature_map: Dict[str, Dict[str, int]]):
        # Map of {feature_name: levels}, where
        #    * feature_name: a column name in the training data
        #    * levels: a dictionary whose keys are current values in
        #              the column and values are the numeric value
        #              to replace them with
        self.feature_map = feature_map

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X = X.copy()
        for feat_col, levels in self.feature_map.items():
            X[feat_col] = X[feat_col].map(levels).astype("int")
        return X


class DateColTransformer(BaseEstimator, TransformerMixin):
    """
    Custom feature-creation class
    """

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame, y=None):
        X = X.copy()
        creation_col = "opened_at"
        X["time_til_update"] = (X["sys_updated_at"] - X[creation_col]) / np.timedelta64(
            1, "s"
        )
        X["open_hour_of_day"] = X[creation_col].dt.hour
        return X


class FeatureRemover(BaseEstimator, TransformerMixin):
    """
    Drop columns from the data. This is useful for
    discarding intermediate features or
    raw columns that you don't want to train on.
    """

    def __init__(self, cols_to_drop):
        self.cols_to_drop = cols_to_drop

    def fit(self, X, y=None):
        return self

    def transform(self, X: pd.DataFrame, y=None):
        X = X.copy()
        for col in self.cols_to_drop:
            if col in X.columns:
                del X[col]
        return X
