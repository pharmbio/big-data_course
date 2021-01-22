from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.datasets import dump_svmlight_file
from rdkit.Chem import DataStructs
import numpy as np

with open('acd_logd_100.smiles', 'r') as file_in:
    dataset = np.zeros((0, ), dtype=np.int8)
    count = 0
    ys = []
    fps = []
    for line in file_in:
        count+=1
        if count == 1: continue

        (x, y) = line.split('\t')
        ys.append(y)
        mol = Chem.MolFromSmiles(x)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        fps.append(fp)
        
    xs = np.array(fps)

dump_svmlight_file(xs, list(map(float,ys)), f='test.dat')
