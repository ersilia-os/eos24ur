import os
import sys
import pandas as pd

from sklearn.preprocessing import RobustScaler
import joblib

ROOT = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(ROOT, "..", "..", "checkpoints", "chembl34_whales.csv")

data = pd.read_csv(datafile)
X = data.drop(columns=['smiles'])
X = X.values
print(X.shape)

scaler = RobustScaler()
scaler.fit(X)

print("scaling done")
print(os.path.join(ROOT, "..", "..", "checkpoints",'scaler_chembl34.pkl'))
joblib.dump(scaler, os.path.join(ROOT, "..", "..", "checkpoints",'scaler_chembl34.pkl'))