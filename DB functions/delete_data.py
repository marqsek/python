import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("300x300") #windows size
app.title('Delete DATA')

entry_table_name = customtkinter.CTkEntry(app,placeholder_text="Table name")
entry_table_name.place(relx=0.2,rely=0.1)

entry_id = customtkinter.CTkEntry(app,placeholder_text="ID")
entry_id.place(relx=0.2,rely=0.2)

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
select_button.place(relx=0.2,rely=0.3)


def delete():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                'Server=MARQSEK\WODAWEK;' +
                                f'Database=Norkacode;' +
                                'Trusted_Connection=True')
        connection.autocommit = True
        connection.execute(f"delete from {entry_table_name.get()} "+
                       f"where id = {entry_id.get()}")

        info_label.configure(text="Deletion Successfull")
    except pyodbc.Error as ex:
        print('failed', ex)
        info_label.configure(text="failed")

delete_button = customtkinter.CTkButton(app,text="DELETE",
                                        command=delete,
                                        fg_color="red")
delete_button.place(relx=0.2,rely=0.4)

info_label=customtkinter.CTkLabel(app,text="something")
info_label.place(relx=0.2,rely=0.5)

app.mainloop()