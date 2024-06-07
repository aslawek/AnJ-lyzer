import pandas as pd

path = 'D:/Python/AnJ-lyzer/data_examples/SRDP_200ms.mpt'
data = pd.read_csv(f'{path}', encoding="ISO-8859-1", skiprows=80, sep='\t')
print(data)

