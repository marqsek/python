import pyodbc

#connection definition to database.
try:
    database_name = input('Enter a database to create:') #creating variable with input value
    connection = pyodbc.connect('DRIVER={SQL Server};'+
                            'Server=MARQSEK\WODAWEK;'+
                            'Database=master;'+
                            'Trusted_Connection=True') #system authentication
    connection.autocommit=True #commit function is used after each sql statement
    connection.execute(f'create database {database_name}')
    print('Database has been created.')
except pyodbc.Error as ex:
    print('Connection failed!',ex)