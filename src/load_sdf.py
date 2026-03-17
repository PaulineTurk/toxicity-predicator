from rdkit.Chem import PandasTools

def load_sdf(path):
    return PandasTools.LoadSDF(path)