import pandas as pd
df = pd.read_csv(r'C:\Users\samsung\OneDrive\Documents\Mani - Python\Pandas\student_data.csv')
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())