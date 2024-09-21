import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("300x500") #windows size
app.title('INSERT INTO TABLE')

entry_table_name = customtkinter.CTkEntry(app,placeholder_text="Table Name")
entry_table_name.place(relx=0.2,rely=0.1)

entry_id = customtkinter.CTkEntry(app,placeholder_text="ID")
entry_id.place(relx=0.2,rely=0.2)

entry_first_name = customtkinter.CTkEntry(app,placeholder_text="First Name")
entry_first_name.place(relx=0.2,rely=0.3)

entry_last_name = customtkinter.CTkEntry(app,placeholder_text="Last Name")
entry_last_name.place(relx=0.2,rely=0.4)

def insert():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'Server=MARQSEK\WODAWEK;' +
                                    f'Database=Norkacode;' +
                                    'Trusted_Connection=True')
        connection.autocommit = True
        connection.execute(f"INSERT INTO {entry_table_name.get()} VALUES "+
                           f"({entry_id.get()}, '{entry_first_name.get()}',"+
                           f"'{entry_last_name.get()}')")
        info_label.configure(text="INSERT COMPLETED!")

    except pyodbc.Error as ex:
        print('Insertion failed', ex)
        info_label.configure(text="INSERTION FAILED!")

insert_button = customtkinter.CTkButton(app,text="INSERT",
                                        command=insert,
                                        fg_color="green")
insert_button.place(relx=0.2,rely=0.5)

info_label=customtkinter.CTkLabel(app,text="something")
info_label.place(relx=0.2,rely=0.6)

app.mainloop()
