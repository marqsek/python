import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("200x300") #windows size
app.title('CREATE-CONNECT MS DATABASE')

entry_database=customtkinter.CTkEntry(app,placeholder_text="Database Name")
entry_database.place(relx=0.1,rely=0.1)

def create_db():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'Server=MARQSEK\WODAWEK;' +
                                    f'Database=master;' +
                                    'Trusted_Connection=True')  # system authentication
        connection.autocommit = True  # commit function is used after each sql statement
        connection.execute(f'create database {entry_database.get()}')
        info_label.configure(text="Database Created")
    except pyodbc.Error as ex:
        print('Connection failed!', ex)
        info_label.configure(text="Database Creating Failed!")

create_button = customtkinter.CTkButton(app,text="Create",
                                        command=create_db,
                                        fg_color="green")
create_button.place(relx=0.1,rely=0.2)

def connect_db():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'Server=MARQSEK\WODAWEK;' +
                                    f'Database={entry_database.get()};' +
                                    'Trusted_Connection=True')  # system authentication
        info_label.configure(text="Connection Successfull")
    except pyodbc.Error as ex:
        print('Connection failed!', ex)
        info_label.configure(text="Connection Failed!")

connect_button = customtkinter.CTkButton(app,text="Connect",
                                        command=connect_db,
                                        fg_color="blue")
connect_button.place(relx=0.1,rely=0.3)

info_label=customtkinter.CTkLabel(app,text="something")
info_label.place(relx=0.1,rely=0.4)

app.mainloop() #preventing from disconnecting suddenly
