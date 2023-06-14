import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details
host = 'localhost'
database = 'ag002'
user = 'root'
password = 'inatel123!'

# Create SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

# SQL query
query = "SELECT * FROM `breast-cancer`"

# Read SQL query into a DataFrame
frame = pd.read_sql(query, con=engine)
print(frame)
