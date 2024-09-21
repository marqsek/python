import pyodbc
import customtkinter

try:
    connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'Server=MARQSEK\WODAWEK;' +
                                f'Database=Norkacode;' +
                                'Trusted_Connection=True')
    connection.autocommit = True
    connection.execute("insert into EMPLOYEES (id, first_name, last_name) values (1, 'Ferd', 'Patmore');")
    connection.execute("insert into EMPLOYEES (id, first_name, last_name) values (2, 'Stace', 'Gabbatt');")
    connection.execute("insert into EMPLOYEES (id, first_name, last_name) values (3, 'Thomasina', 'Elecum');")
    connection.execute("insert into EMPLOYEES (id, first_name, last_name) values (4, 'Evelina', 'Shellum');")

except pyodbc.Error as ex:
    print('Connection failed!', ex)