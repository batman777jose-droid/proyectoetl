import pandas as pd

clientes = pd.read_csv('../data/clientes_limpios.csv')
ventas = pd.read_csv('../data/ventas_limpios.csv')

merge = pd.merge(ventas, clientes, on='id_cliente')
merge['total'] = merge['cantidad'] * merge['precio']

merge.to_csv('../data/ventas_transformadas.csv', index=False)

print(merge.head())
