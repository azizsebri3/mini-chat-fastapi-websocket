from database import engine

try:
    conn = engine.connect()
    conn.close()
    print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")