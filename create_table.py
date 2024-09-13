import tkinter

import customtkinter
import pyodbc

customtkinter.set_appearance_mode("system") #set the view mode
customtkinter.set_default_color_theme("blue")#default color

app = customtkinter.CTk() #window variable
app.geometry("500x500") #windows size
app.title('CREATE TABLE')

entry_table_name=customtkinter.CTkEntry(app,placeholder_text="TABLE NAME",width=190)
entry_table_name.place(relx=0.1,rely=0.1)

entry_column1=customtkinter.CTkEntry(app,placeholder_text="COLUMN_1",width=190)
entry_column1.place(relx=0.1,rely=0.2)

entry_column2=customtkinter.CTkEntry(app,placeholder_text="COLUMN_2",width=190)
entry_column2.place(relx=0.1,rely=0.3)

entry_column3=customtkinter.CTkEntry(app,placeholder_text="COLUMN_3",width=190)
entry_column3.place(relx=0.1,rely=0.4)

def create():
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};' +
                                    'Server=MARQSEK\WODAWEK;' +
                                    f'Database=Norkacode;' +
                                    'Trusted_Connection=True')  # system authentication
        connection.autocommit = True
        sql_stmt = f"CREATE TABLE {entry_table_name.get()}\
                    ({entry_column1.get()} {radio_var_col1.get()},\
                    {entry_column2.get()} {radio_var_col2.get()},\
                    {entry_column3.get()} {radio_var_col3.get()})"
        connection.execute(sql_stmt)
        info_label.configure(text="Table Created")
    except pyodbc.Error as ex:
        print('Connection failed', ex)
        info_label.configure(text="Connection failed!")

create_button = customtkinter.CTkButton(app,text="Create",
                                        command=create,
                                        fg_color="green")
create_button.place(relx=0.1,rely=0.5)

#column1
radio_var_col1 = tkinter.StringVar(value="")
col1_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable=radio_var_col1,
                                                 value="varchar(50)")
col1_rd_varchar50.place(relx=0.5,rely=0.2)

col1_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable=radio_var_col1,
                                                 value="integer")
col1_rd_int.place(relx=0.7,rely=0.2)

#column2
radio_var_col2 = tkinter.StringVar(value="")
col2_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable=radio_var_col2,
                                                 value="varchar(50)")
col2_rd_varchar50.place(relx=0.5,rely=0.3)

col2_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable=radio_var_col2,
                                                 value="integer")
col2_rd_int.place(relx=0.7,rely=0.3)

#column3
radio_var_col3 = tkinter.StringVar(value="")
col3_rd_varchar50 = customtkinter.CTkRadioButton(app,
                                                 text="varchar(50)",
                                                 variable=radio_var_col3,
                                                 value="varchar(50)")
col3_rd_varchar50.place(relx=0.5,rely=0.4)

col3_rd_int = customtkinter.CTkRadioButton(app,
                                                 text="integer",
                                                 variable=radio_var_col3,
                                                 value="integer")
col3_rd_int.place(relx=0.7,rely=0.4)

info_label=customtkinter.CTkLabel(app,text="something")
info_label.place(relx=0.1,rely=0.6)

app.mainloop()