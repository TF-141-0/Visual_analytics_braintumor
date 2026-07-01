 #Dataset upload check 

import pandas as pd
file_path = "Brain_GSE50161.csv"
df = pd.read_csv(file_path)
print(f"Dataset Structure: {df.shape[0]} rows (patients) and {df.shape[1]} columns (features).") 

