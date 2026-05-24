import pandas as pd

clientes = pd.read_csv('../data/clientes.csv')
ventas = pd.read_csv('../data/ventas.csv')

clientes = clientes.dropna().drop_duplicates()
ventas = ventas.dropna().drop_duplicates()

clientes.to_csv('../data/clientes_limpios.csv', index=False)
ventas.to_csv('../data/ventas_limpios.csv', index=False)

print('Datos limpios correctamente')
