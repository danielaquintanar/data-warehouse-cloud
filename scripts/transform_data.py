import pandas as pd

# Leer los datos cargados desde la base de datos
data = pd.read_csv('data/source_data.csv')

# Realizar transformaciones, por ejemplo, calcular el total por producto
data['total'] = data['quantity'] * data['price']

# Guardar los datos transformados
data.to_csv('data/transformed_data.csv', index=False)
