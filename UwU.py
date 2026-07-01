 #Dataset upload check 
import pandas as pd
file_path = "Brain_GSE50161.csv"
df = pd.read_csv(file_path)
print(f"{df.shape[0]} rows (patients) and {df.shape[1]} columns (features).") 

# Separate the clinical labels from the genetic numbers
# CuMiDa datasets usually have one text column for the cancer type (e.g., 'Ependymoma').
# We find it by looking for the column that isn't a number.
label_column = df.select_dtypes(exclude=['float64', 'int64']).columns[0]

# Isolate just the numerical gene expression data
gene_data = df.select_dtypes(include=['float64', 'int64'])

#statistical variance of all features

variances = gene_data.var()

# We sort from highest variance to lowest, and grab the names (index) of the top 1000
top_1000_gene_names = variances.sort_values(ascending=False).head(1000).index

# Rebuild the dataset with only the important data
df_optimized = df[[label_column] + list(top_1000_gene_names)]

# 5. Verify the new, compressed dimensions
print(f"Old Dataset Structure: {df.shape[0]} rows and {df.shape[1]} columns.")
print(f"Optimized Structure: {df_optimized.shape[0]} rows and {df_optimized.shape[1]} columns.")

# View the new optimized DataFrame
df_optimized.head()
