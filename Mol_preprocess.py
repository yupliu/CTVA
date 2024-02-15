import pandas as pd
import rdkit
from rdkit import Chem

stFile = "~/source_code/REINVENT4/sampling.csv"
mol = pd.read_csv(stFile)
mol["mol"] = mol["SMILES"].apply(Chem.MolFromSmiles)

from chembl_structure_pipeline import standardizer
mol["std_mol"] = mol["mol"].apply(standardizer.standardize_mol)
