from sqlalchemy import create_engine, text
from decouple import config


# Connection details
server = config('server')
database = config('database')
username = config('username')
password = config('password@')
driver = config('driver')

# Create engine
engine_url = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)
engine = create_engine(engine_url)

# Connect and query
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT @@VERSION"))
        for row in result:
            print(f"Connected successfully! SQL Server version: {row[0]}")
except Exception as e:
    print(f"Error: {e}")