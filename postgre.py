import psycopg2

# Define connection parameters
db_host = '192.168.x.x'  # Replace with host IP
db_name = 'postgres'
db_user = 'sans'
db_password = 'training'

# Connect to PostgreSQL database
try:
    conn = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password
    )
    print("Connection to PostgreSQL database established successfully.")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")

# Create cursor to interact with the database
cursor = conn.cursor()

# Retrieve table names
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
tables = cursor.fetchall()
print("Tables in the PostgreSQL database:", tables)

# Retrieve columns from a specific table (replace 'your_table' with table name)
table_name = 'your_table'  # Replace with table
cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}';")
columns = cursor.fetchall()
print(f"Columns in {table_name}:", columns)

# Execute SQL query (adjust to match table/column)
cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
records = cursor.fetchall()
print("Sample records from table:", records)

# Close the cursor and connection
cursor.close()
conn.close()