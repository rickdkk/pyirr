from dataclasses import dataclass, asdict

import numpy as np


@dataclass
class maxwell_result:
    subjects: int
    raters: int
    value: float

    def to_dict(self):
        return asdict(self)

    def __repr__(self):
        model_string = "=" * 50 + "\n" + f"Maxwell's RE".center(50, " ")
        model_string += "\n" + "=" * 50 + "\n"
        model_string += f"Subjects = {self.subjects}\nRaters = {self.raters}\nRE = {self.value:.2f}\n"
        model_string += "=" * 50
        return model_string


def maxwell(ratings):
    """Calculate Maxwell's RE

    Parameters
    ----------
    ratings: array_like
        subjects * raters array or dataframe

    """
    ratings = np.array(ratings)  # make sure ratings is not a list or DataFrame

    ratings = ratings[~np.isnan(ratings).any(axis=1)]  # drop nans

    ns = ratings.shape[0]
    nr = ratings.shape[1]

    if nr > 2:
        raise Exception("Number of raters exceeds 2.")

    levels = set(ratings.ravel())  # number of unique levels

    if len(levels) > 2:
        raise Exception("Ratings are not binary.")

    r1, r2 = ratings[:, 0], ratings[:, 1]

    coeff = 2 * np.sum((r1 - r2) == 0) / ns - 1

    return maxwell_result(ns, nr, value=coeff)