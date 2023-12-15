import pandas as pd

df = pd.read_csv('dataset_v1.01.csv', header=0, sep='\t')
df = df.sample(n=200)
df.to_csv('pilot_task.csv', sep='\t', index=False)
df.to_excel('pilot_task.xlsx', index=False)