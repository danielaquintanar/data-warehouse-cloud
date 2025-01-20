import psycopg2
import pandas as pd

# Conexión a la base de datos PostgreSQL (o Redshift)
conn = psycopg2.connect(
    host="your-db-host",
    dbname="your-db-name",
    user="your-db-user",
    password="your-db-password"
)
cursor = conn.cursor()

# Leer el archivo CSV
data = pd.read_csv('data/source_data.csv')

# Insertar los datos en la tabla
for index, row in data.iterrows():
    cursor.execute("""
        INSERT INTO sales_data (product_id, quantity, price, date)
        VALUES (%s, %s, %s, %s)
    """, (row['product_id'], row['quantity'], row['price'], row['date']))

conn.commit()
cursor.close()
conn.close()
