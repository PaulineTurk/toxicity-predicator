from rdkit.Chem.rdFingerprintGenerator import GetMorganGenerator
import pandas as pd
from compute_feature import compute_features
import numpy as np
from load_sdf import load_sdf


def sdf_to_dataset(path, target):
    df = load_sdf(path)
    renamed_target = target.replace("-", "_")
    dataframe = df.rename(columns={target: renamed_target})
    return build_dataset(dataframe, renamed_target)

def build_dataset(dataframe, target_column):

    morgan_generator = GetMorganGenerator(radius=2, fpSize=2048)

    features = []
    targets = []

    for row in dataframe.itertuples():

        mol = row.ROMol
        target = getattr(row, target_column)

        if mol is None or pd.isna(target):
            continue

        feat = compute_features(mol, morgan_generator)

        features.append(feat)
        targets.append(float(target))

    X = np.vstack(features)
    y = np.array(targets)

    return X, y