import os
import sys
import pandas as pd

from sklearn.preprocessing import RobustScaler
import joblib


datafile = os.path.abspath(sys.argv[1])  # a file containing WHALES descriptors (eos3ae6) of 100K molecules randomly sampled from ChEMBL

data = pd.read_csv(datafile)
X = data.drop(columns=['key', "input"])
X = X.values
print(X.shape)

scaler = RobustScaler()
scaler.fit(X)

joblib.dump(scaler, '../../checkpoints/scaler.pkl')