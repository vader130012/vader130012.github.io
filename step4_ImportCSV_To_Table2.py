from optparse import Values
import pandas as pd
import psycopg2
from sqlalchemy import values
# define variables for database connection
hostname = 'localhost'
portID = 5432
database = 'HHLT'
username = 'postgres'
pwd = 'postgres'
connection = None
cur = None
filepath = 'sensor_list.csv'
df = pd.read_csv(filepath)

# defining connection variable to pass the required parameters to make the connection
try:

    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = portID            )
    print("Connection Established")
    cur = connection.cursor()

    with open('sensor_list.csv','r') as f:
        next(f)
        cur.copy_from(f,'sensor_database', sep=',')

    
    # now commiting the transcation
    connection.commit()
    print("Table Committed")    
except Exception as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
    if cur is not None:
        cur.close()

