import psycopg2
# define variables for database connection
hostname = 'localhost'
portID = 5432
database = 'HHLT'
username = 'postgres'
pwd = 'postgres'
connection = None
cur = None

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

    # as the script could be re run, it's important to drop the table, as the script 
    # wont execute second time as we already have some data in it and we cant overwrite the ID
    cur.execute('DROP TABLE IF EXISTS satellite_database')

    # creating table
    create_script = '''
        CREATE TABLE IF NOT EXISTS satellite_database (
            id SERIAL PRIMARY KEY,
            Agency varchar(50) NOT NULL ,
            Link varchar(150),
            Description varchar(500),
            Incorporates varchar(100),
            Features varchar(400),
            Best_resolution varchar(30),
            Cost varchar(250)                             )'''
    # now executing the above script
    cur.execute(create_script)
    print("Table Executed")
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
        