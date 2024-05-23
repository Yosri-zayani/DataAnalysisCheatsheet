# Number of dup rows 
num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")

#remove dupliacted rows : 
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates

      
# find missing data
missing_values = df.isnull().sum() or isna()
print(missing_values)

# drop missing values 
df.dropna()

# replacing na values in college with No college 
nba["College"].fillna("No College", inplace = True) 


# Find least frequent value in a Series (replace 'col1' with your column name)
least_frequent_value = df['col1'].value_counts().idxmin()

# Get number of unique values in a Series (replace 'col1' with your column name)
num_unique_values = df['col1'].nunique()

