import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("400x400") #windows size
app.title('Update table')

entry_table_name = customtkinter.CTkEntry(app,placeholder_text="Table name")
entry_table_name.place(relx=0.3,rely=0.1)

entry_id = customtkinter.CTkEntry(app,placeholder_text="ID")
entry_id.place(relx=0.3,rely=0.2)

entry_first_name = customtkinter.CTkEntry(app,placeholder_text="FIRST_NAME")
entry_first_name.place(relx=0.3,rely=0.3)

entry_last_name = customtkinter.CTkEntry(app,placeholder_text="SECOND_NAME")
entry_last_name.place(relx=0.3,rely=0.4)

def select():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'Server=MARQSEK\WODAWEK;' +
                                f'Database=Norkacode;' +
                                'Trusted_Connection=True')

        cursor = connection.cursor()

        a=0
        cursor.execute(f"select * from {entry_table_name.get()} "+
                       f"where id = {entry_id.get()}")

        for data in cursor:
            a=1
            info_label.configure(text=f"{data[0]} {data[1]} {data[2]}")
        if a == 0:
            info_label.configure(text="no data!")
    except pyodbc.Error as ex:
        print('Failed', ex)
        info_label.configure(text="NO TABLE")

select_button = customtkinter.CTkButton(app,text="SELECT",
                                        command=select,
                                        fg_color="green")
select_button.place(relx=0.5,rely=0.5)

def update():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'Server=MARQSEK\WODAWEK;' +
                                    f'Database=Norkacode;' +
                                    'Trusted_Connection=True')
        connection.autocommit = True
        connection.execute(f"UPDATE {entry_table_name.get()} "+
                           f"SET first_name = '{entry_first_name.get()}', "+
                           f"last_name =  '{entry_last_name.get()}' "+
                           f"where id = {entry_id.get()}")
        info_label.configure(text="Update COMPLETED!")

    except pyodbc.Error as ex:
        print('Insertion failed', ex)
        info_label.configure(text="Update FAILED!")

insert_button = customtkinter.CTkButton(app,text="Update",
                                        command=update,
                                        fg_color="red")
insert_button.place(relx=0.1,rely=0.5)

info_label = customtkinter.CTkLabel(app,text="INFO",font=('Arial',25))
info_label.place(relx=0.2,rely=0.65)



app.mainloop()