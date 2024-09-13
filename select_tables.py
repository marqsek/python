import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'Server=MARQSEK\WODAWEK;' +
                                f'Database=Norkacode;' +
                                'Trusted_Connection=True')
    cursor = connection.cursor()

    cursor.execute("select * from employees")

    for data in cursor:
        print(data[0],data[1],data[2])

except pyodbc.Error as ex:
    print("Failed!",ex)