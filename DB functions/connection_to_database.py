import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'MARQSEK\WODAWEK'
DATABASE_NAME = 'Norkacode'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid=sa;
    pwd=Zaq12wsx@;
"""

conn = pyodbc.connect(connection_string)
print(conn)
