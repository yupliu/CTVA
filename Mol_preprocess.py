import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np

#stFile = "~/source_code/REINVENT4/sampling.csv"
#mol = pd.read_csv(stFile)
#mol["mol"] = mol["SMILES"].apply(Chem.MolFromSmiles)

#from chembl_structure_pipeline import standardizer
#mol["std_mol"] = mol["mol"].apply(standardizer.standardize_mol)

def getFigerpringArray(smiles):
    mol = Chem.MolFromSmiles(smiles)
    from rdkit.Chem import rdFingerprintGenerator
    import numpy as np
    rd_fgen = rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048)
    mol_fp = rd_fgen.GetFingerprint(mol)
    mol_fp_array = ','.join(mol_fp.ToBitString())
    return mol_fp_array

sm = "CCCO"



print(getFigerpringArray(sm))


mol = Chem.MolFromSmiles('c1cccnc1C')
fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
array = np.zeros((0, ), dtype=np.int8)
DataStructs.ConvertToNumpyArray(fp, array)

