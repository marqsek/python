import pyodbc
import customtkinter

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("300x300") #windows size
app.title('SELECT TABLE')

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

        cursor.execute(f"select * from {entry_table_name.get()} where id = {entry_id.get()}")

        for data in cursor:
            info_label.configure(text=f"{data[0]} {data[1]} {data[2]}")
    except pyodbc.Error as ex:
        print('Insertion failed', ex)
        info_label.configure(text="NO DATA OR TABLE")

select_button = customtkinter.CTkButton(app,text="SELECT",
                                        command=select,
                                        fg_color="green")
select_button.place(relx=0.2,rely=0.3)

info_label=customtkinter.CTkLabel(app,text="something")
info_label.place(relx=0.2,rely=0.4)

app.mainloop()