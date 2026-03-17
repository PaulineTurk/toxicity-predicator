from rdkit.Chem import Descriptors
import numpy as np

def compute_features(molecule, morgan_generator):

    fingerprint = morgan_generator.GetFingerprint(molecule)

    physchem = np.array([
        Descriptors.MolLogP(molecule),
        Descriptors.TPSA(molecule),
        Descriptors.NumHDonors(molecule),
        Descriptors.NumHAcceptors(molecule),
        Descriptors.MolWt(molecule),
    ])

    return np.concatenate([np.array(fingerprint), physchem])