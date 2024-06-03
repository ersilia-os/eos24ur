# File to process CHEMBL34 to train a scaler

import pandas as pd
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
datafile = os.path.join(ROOT, "..", "..", "checkpoints", "chembl34.csv")

# Load the downloaded text file into a DataFrame & save it into the checkpoints folder
df = pd.read_csv('chembl_34_chemreps.txt', delimiter='\t') 
# keep only smiles & save as csv
df = df[["canonical_smiles"]] 
df.rename(columns={"canonical_smiles":"smiles"}, inplace=True)
df.to_csv("chembl34.csv", index=False)

#create chunks for easy predict
chunk_size = 100000
total_rows = len(df)
num_chunks = (total_rows + chunk_size - 1) // chunk_size  # Calculate the number of chunks
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, total_rows)
    chunk_df = df.iloc[start_idx:end_idx]
    chunk_df.to_csv(f'chembl34_{i + 1}.csv', index=False)


#eliminate molecule that cannot be calculated
df = pd.read_csv("chembl34_24.csv")
print(df[df["smiles"]=="Cc1ccc2c(c1)-n1-c(=O)/c=c\c(=O)-n-2-c2cc(C)ccc2-1"])
df_ = df.drop([11326])
df_.to_csv("chembl34_24.csv", index=False)

#merge all chunks with Whales descriptors (not normalised)

dfs = []
for i in range(1, 26):
    df1 = pd.read_csv(f"chembl34_{i}.csv")
    df2 = pd.read_csv(f"whales_{i}.csv")
    df = pd.concat([df1,df2],axis=1)
    dfs += [df]

df = pd.concat(dfs, ignore_index=True)
print(df.shape)
df.to_csv(os.path.join(ROOT, "..", "..", "checkpoints", "chembl34_whales.csv"), index=False)