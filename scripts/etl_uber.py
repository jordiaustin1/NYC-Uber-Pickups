import pandas as pd
import mysql.connector

# 1. Load CSV
df = pd.read_csv("data_raw/Uber-Jan-Feb-FOIL.csv")

# 2. Clean the date column
df['date'] = pd.to_datetime(df['date'])

# 3. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="uber_db"
)

cursor = conn.cursor()

# 4. Insert data into MySQL
insert_query = """
INSERT INTO uber_pickups (dispatching_base_number, date, active_vehicles, trips)
VALUES (%s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row['dispatching_base_number'],
        row['date'],
        int(row['active_vehicles']),
        int(row['trips'])
    ))

conn.commit()
conn.close()

print("Data successfully loaded into MySQL!")
