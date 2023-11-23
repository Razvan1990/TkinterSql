import sqlite3
import tkinter
from tkinter import ttk
import ttkthemes
import os

from checker import CheckThings
from tkinter import *
from tkinter import messagebox
import constants


class GuiInterface:

    def __init__(self):
        self.checker = CheckThings()
        self.table = "footballers"

    def cancel_x_button_level_2(self):
        pass

    def return_treeview_x(self, root_value, table_name):
        title ="EXIT"
        message = "Are you sure you want to exit"
        close = messagebox.askokcancel(title, message)
        if close:
            root_value.destroy()
            self.see_records(table_name)
        else:
            return



    def return_main_window_with_x(self, root_value, option):
        global title, message
        if option == 1:
            title = list(constants.CANCEL_DICTIONARY.keys())[0]
            message = constants.CANCEL_DICTIONARY[title]
        elif option == 2:
            title = list(constants.CANCEL_DICTIONARY.keys())[1]
            message = constants.CANCEL_DICTIONARY[title]
        elif option == 3:
            title = list(constants.CANCEL_DICTIONARY.keys())[2]
            message = constants.CANCEL_DICTIONARY[title]
        close = messagebox.askokcancel(title, message)
        if close:
            root_value.destroy()
            self.create_main_gui()

    '''ADD PART'''

    def cancel_add(self):
        root_add.destroy()
        self.create_main_gui()

    def sql_add(self, table_name):
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        # check if table exists and if not create it
        if not self.checker.check_if_table_exists(table_name):
            self.checker.create_table(table_name)
        my_cursor.execute("""INSERT INTO """ + table_name + """ VALUES (
                                         :first_name,
                                         :second_name,
                                         :club,
                                        :nationality,
                                        :age)""",
                          # dummy dictionary
                          {
                              "first_name": first_name_entry.get(),
                              "second_name": last_name_entry.get(),
                              "club": club_entry.get(),
                              "nationality": nationality_entry.get(),
                              "age": str(age_entry.get())
                          }
                          )
        connection.commit()
        connection.close()
        message_add = " Player {} {} has been added in {}".format(first_name_entry.get(), last_name_entry.get(),
                                                                  table_name)
        messagebox.showinfo("ADDING", message_add)
        root_add.destroy()
        self.create_main_gui()

    def open_add(self):
        root.destroy()
        global root_add
        global first_name_entry
        global last_name_entry
        global nationality_entry
        global club_entry
        global age_entry
        root_add = Tk()
        root_add.title("ADD")
        root_add.iconbitmap(r"2020-world11-men-1100-names.ico")
        root_add.geometry("400x400")
        root_add["bg"] = "#5BBD2A"
        root_add.protocol("WM_DELETE_WINDOW", lambda: self.return_main_window_with_x(root_add, 1, ))
        # create entry boxes
        first_name_entry = Entry(root_add, width=35, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                                 bg="#D4E2D0")
        first_name_entry.grid(row=0, column=1, pady=(5, 5))
        last_name_entry = Entry(root_add, width=35, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                                bg="#D4E2D0")
        last_name_entry.grid(row=1, column=1, pady=(5, 5))
        club_entry = Entry(root_add, width=35, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                           bg="#D4E2D0")
        club_entry.grid(row=2, column=1, pady=(5, 5))
        nationality_entry = Entry(root_add, width=35, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                                  bg="#D4E2D0")
        nationality_entry.grid(row=3, column=1, pady=(5, 5))
        age_entry = Entry(root_add, width=35, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                          bg="#D4E2D0")
        age_entry.grid(row=4, column=1)
        # make labels
        first_name_label = Label(root_add, text="First name", justify="center", font=("Comic Sans", 11, "bold"),
                                 cursor="star", fg="#3D91C4", bg="#5BBD2A")
        first_name_label.grid(row=0, column=0, padx=5, pady=(5, 5))
        last_name_label = Label(root_add, text="Last name", justify="center", font=("Comic Sans", 11, "bold"),
                                cursor="star", fg="#3D91C4", bg="#5BBD2A")
        last_name_label.grid(row=1, column=0, padx=5, pady=(5, 5))
        club_label = Label(root_add, text="Club", justify="center", font=("Comic Sans", 11, "bold"),
                           cursor="star", fg="#3D91C4", bg="#5BBD2A")
        club_label.grid(row=2, column=0, padx=5, pady=(5, 5))
        nationality_label = Label(root_add, text="Nationality", justify="center", font=("Comic Sans", 11, "bold"),
                                  cursor="star", fg="#3D91C4", bg="#5BBD2A")
        nationality_label.grid(row=3, column=0, padx=5, pady=(5, 5))
        age_label = Label(root_add, text="Age", justify="center", font=("Comic Sans", 11, "bold"),
                          cursor="star", fg="#3D91C4", bg="#5BBD2A")
        age_label.grid(row=4, column=0, padx=5, pady=(5, 5))

        # create buttons
        ok_button = Button(root_add, text="OK", width=15, height=2, fg="#E1254D", bg="#248B48",
                           command=lambda: self.sql_add(self.table))
        ok_button.grid(row=5, column=0, padx=20, pady=30)
        ok_button.place(relx=0.3, rely=0.6, anchor='center')
        cancel_button = Button(root_add, text="CANCEL", width=15, height=2, fg="#E1254D", bg="#E8E7D8",
                               command=self.cancel_add)
        cancel_button.grid(row=5, column=1, padx=70, pady=30)
        cancel_button.place(relx=0.7, rely=0.6, anchor='center')
        root_add.mainloop()

    '''DELETE PART'''

    def cancel_delete(self):

        root_delete.destroy()
        self.create_main_gui()

    def sql_delete(self, table_name, table_id):
        if not self.checker.check_for_id(table_name, table_id):
            messagebox.showerror("NO ID", "There is no record in the database with the selected id")
            return
        else:
            database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
            connection = sqlite3.connect(database)
            my_cursor = connection.cursor()
            my_cursor.execute(("SELECT * FROM " + table_name + " WHERE oid =:id"),
                              {
                                  "id": table_id
                              })
            list_delete = my_cursor.fetchall()
            my_cursor.execute(("DELETE  FROM " + table_name + " WHERE oid=:id"),
                              {
                                  "id": table_id
                              })
            connection.commit()
            connection.close()
            delete_message = "Player {} {} has been deleted from {}".format(list_delete[0][0], list_delete[0][1],
                                                                            table_name)
            messagebox.showinfo("DELETED", delete_message)
            root_delete.destroy()
            self.create_main_gui()

    def open_delete(self):
        root.destroy()
        global root_delete
        global id_delete
        root_delete = Tk()
        root_delete.title("DELETE RECORD")
        root_delete.iconbitmap(r"2020-world11-men-1100-names.ico")
        root_delete.geometry("250x250")
        root_delete["bg"] = "#C9334F"
        root_delete.protocol("WM_DELETE_WINDOW", lambda: self.return_main_window_with_x(root_delete, 3, ))
        # create entry and label
        id_delete = Entry(root_delete, width=10, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                          bg="#D4E2D0")
        id_delete.grid(row=0, column=1, pady=(5, 5), sticky=tkinter.E, padx=10)
        id_delete.place(relx=0.5, rely=0.2)
        id_delete_label = Label(root_delete, text="ID", justify="center", font=("Comic Sans", 11, "bold"),
                                cursor="star", fg="#F8F7EB", bg="#C9334F")
        id_delete_label.grid(row=0, column=0, padx=5, pady=(5, 5))
        id_delete_label.place(relx=0.2, rely=0.2)
        # create buttons
        ok_button = Button(root_delete, text="OK", width=10, height=2, fg="#E1254D", bg="#248B48",
                           command=lambda: self.sql_delete(self.table, id_delete.get()))
        ok_button.grid(row=5, column=0, padx=20, pady=30)
        ok_button.place(relx=0.3, rely=0.6, anchor='center')
        cancel_button = Button(root_delete, text="CANCEL", width=10, height=2, fg="#E1254D", bg="#E8E7D8",
                               command=self.cancel_delete)
        cancel_button.grid(row=5, column=1, padx=70, pady=30)
        cancel_button.place(relx=0.7, rely=0.6, anchor='center')

        root_delete.mainloop()

    '''EDIT/UPDATE PART'''

    def cancel_edit_update(self):
        root_edit_update.destroy()
        # self.create_main_gui()

    def cancel_edit(self):
        root_edit.destroy()
        self.create_main_gui()

    def check_update_modification(self, table_name, id_table):
        # check if there is something modified
        list_original = self.checker.get_original_list(table_name, id_table)
        if list_original[0][0] != first_name_entry_edit.get():
            return True
        if list_original[0][1] != last_name_entry_edit.get():
            return True
        if list_original[0][2] != club_entry_edit.get():
            return True
        if list_original[0][3] != nationality_entry_edit.get():
            return True
        if list_original[0][4] != int(age_entry_edit.get()):
            return True
        return False

    def sql_update(self, table_name, table_id):
        if not self.check_update_modification(table_name, table_id):
            messagebox.showerror("NO MODIFICATIONS", "There are no modifications for the record")
            return
        else:
            # create connection
            database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
            connection = sqlite3.connect(database)
            my_cursor = connection.cursor()
            my_cursor.execute("""UPDATE """ + table_name + """ SET
                            first_name =:first_name,
                            second_name=:second_name,
                            club =:club,
                            nationality=:nationality,
                            age=:age WHERE oid=:id""",
                              # dummy dictionary
                              {
                                  "first_name": first_name_entry_edit.get(),
                                  "second_name": last_name_entry_edit.get(),
                                  "club": club_entry_edit.get(),
                                  "nationality": nationality_entry_edit.get(),
                                  "age": int(age_entry_edit.get()),
                                  "id": table_id

                              }
                              )
            connection.commit()
            connection.close()
            message_update = " Player {} {} has been edit in {}".format(first_name_entry_edit.get(),
                                                                        last_name_entry_edit.get(),
                                                                        table_name)
            messagebox.showinfo("UPDATE", message_update)
            root_edit_update.destroy()
            # self.create_main_gui()

    def sql_edit(self, table_name, table_id):
        if not self.checker.check_for_id(table_name, table_id):
            messagebox.showerror("NO ID", "There is no record in the database with the selected id")
            return
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        my_cursor.execute(("""SELECT * FROM """ + table_name + " WHERE oid= " + table_id))
        list_select = my_cursor.fetchall()
        # create the entries and the label and output them
        global root_edit_update
        global first_name_entry_edit
        global last_name_entry_edit
        global nationality_entry_edit
        global club_entry_edit
        global age_entry_edit
        root_edit_update = Tk()
        root_edit_update.title("Update/Edit record")
        root_edit_update.iconbitmap(r"2020-world11-men-1100-names.ico")
        root_edit_update.geometry("400x400")
        root_edit_update["bg"] = "#2092B0"
        root_edit_update.protocol("WM_DELETE_WINDOW",
                                  lambda: self.cancel_x_button_level_2())
        # create entry boxes
        first_name_entry_edit = Entry(root_edit_update, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                      cursor="star",
                                      bg="#D4E2D0")
        first_name_entry_edit.grid(row=0, column=1, pady=(5, 5))
        last_name_entry_edit = Entry(root_edit_update, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                     cursor="star",
                                     bg="#D4E2D0")
        last_name_entry_edit.grid(row=1, column=1, pady=(5, 5))
        club_entry_edit = Entry(root_edit_update, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                cursor="star",
                                bg="#D4E2D0")
        club_entry_edit.grid(row=2, column=1, pady=(5, 5))
        nationality_entry_edit = Entry(root_edit_update, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                       cursor="star",
                                       bg="#D4E2D0")
        nationality_entry_edit.grid(row=3, column=1, pady=(5, 5))
        age_entry_edit = Entry(root_edit_update, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                               cursor="star",
                               bg="#D4E2D0")
        age_entry_edit.grid(row=4, column=1)
        # make labels
        first_name_label_edit = Label(root_edit_update, text="First name", justify="center",
                                      font=("Comic Sans", 11, "bold"),
                                      cursor="star", fg="#C7A8B1", bg="#2092B0")
        first_name_label_edit.grid(row=0, column=0, padx=5, pady=(5, 5))
        last_name_label_edit = Label(root_edit_update, text="Last name", justify="center",
                                     font=("Comic Sans", 11, "bold"),
                                     cursor="star", fg="#C7A8B1", bg="#2092B0")
        last_name_label_edit.grid(row=1, column=0, padx=5, pady=(5, 5))
        club_label_edit = Label(root_edit_update, text="Club", justify="center", font=("Comic Sans", 11, "bold"),
                                cursor="star", fg="#C7A8B1", bg="#2092B0")
        club_label_edit.grid(row=2, column=0, padx=5, pady=(5, 5))
        nationality_label_edit = Label(root_edit_update, text="Nationality", justify="center",
                                       font=("Comic Sans", 11, "bold"),
                                       cursor="star", fg="#C7A8B1", bg="#2092B0")
        nationality_label_edit.grid(row=3, column=0, padx=5, pady=(5, 5))
        age_label_edit = Label(root_edit_update, text="Age", justify="center", font=("Comic Sans", 11, "bold"),
                               cursor="star", fg="#C7A8B1", bg="#2092B0")
        age_label_edit.grid(row=4, column=0, padx=5, pady=(5, 5))
        # button creation
        ok_button = Button(root_edit_update, text="OK", width=15, height=2, fg="#E1254D", bg="#248B48",
                           command=lambda: self.cancel_edit_update()
                           )
        ok_button.grid(row=5, column=0, padx=20, pady=30)
        ok_button.place(relx=0.3, rely=0.6, anchor='center')
        update_button = Button(root_edit_update, text="UPDATE", width=15, height=2, fg="#E1254D", bg="#E8E7D8",
                               command=lambda: self.sql_update(self.table, id_edit.get()))
        update_button.grid(row=5, column=1, padx=70, pady=30)
        update_button.place(relx=0.7, rely=0.6, anchor='center')

        # insert the names form the list
        first_name_entry_edit.insert(0, list_select[0][0])
        last_name_entry_edit.insert(0, list_select[0][1])
        club_entry_edit.insert(0, list_select[0][2])
        nationality_entry_edit.insert(0, list_select[0][3])
        age_entry_edit.insert(0, str(list_select[0][4]))
        root_edit_update.mainloop()

    def open_edit(self):
        root.destroy()
        global root_edit
        global id_edit
        root_edit = Tk()
        root_edit.title("VIEW/UPDATE RECORD")
        root_edit.iconbitmap(r"2020-world11-men-1100-names.ico")
        root_edit.geometry("250x250")
        root_edit["bg"] = "#2092B0"
        root_edit.protocol("WM_DELETE_WINDOW", lambda: self.return_main_window_with_x(root_edit, 2, ))
        # create entry and label
        id_edit = Entry(root_edit, width=10, justify="center", font=("Comic Sans", 9, "bold"), cursor="star",
                        bg="#D4E2D0")
        id_edit.grid(row=0, column=1, pady=(5, 5), sticky=tkinter.E, padx=10)
        id_edit.place(relx=0.5, rely=0.2)
        id_edit_label = Label(root_edit, text="ID", justify="center", font=("Comic Sans", 11, "bold"),
                              cursor="star", fg="#F8F7EB", bg="#2092B0")
        id_edit_label.grid(row=0, column=0, padx=5, pady=(5, 5))
        id_edit_label.place(relx=0.2, rely=0.2)
        # create buttons
        ok_button = Button(root_edit, text="OK", width=10, height=2, fg="#E1254D", bg="#248B48",
                           command=lambda: self.sql_edit(self.table, id_edit.get()))
        ok_button.grid(row=5, column=0, padx=20, pady=30)
        ok_button.place(relx=0.3, rely=0.6, anchor='center')
        cancel_button = Button(root_edit, text="CANCEL", width=10, height=2, fg="#E1254D", bg="#E8E7D8",
                               command=self.cancel_edit)
        cancel_button.grid(row=5, column=1, padx=70, pady=30)
        cancel_button.place(relx=0.7, rely=0.6, anchor='center')
        root_edit.mainloop()

    def open_entry(self, event):
        #first we create the root things like in edit
        #view_root.destroy()
        global root_treeview_edit
        root_treeview_edit = Tk()
        root_treeview_edit.title("VIEW RECORD")
        root_treeview_edit.iconbitmap(r"2020-world11-men-1100-names.ico")
        root_treeview_edit.geometry("400x400")
        root_treeview_edit["bg"] = "#A29476"
        #root_treeview_edit.protocol("WM_DELETE_WINDOW", lambda: self.return_treeview_x(root_treeview_edit, self.table))
        #create labels and
        first_name_entry_tree = Entry(root_treeview_edit, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                      cursor="star",
                                      bg="#D4E2D0")
        first_name_entry_tree.grid(row=0, column=1, pady=(5, 5))
        last_name_entry_tree = Entry(root_treeview_edit, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                     cursor="star",
                                     bg="#D4E2D0")
        last_name_entry_tree.grid(row=1, column=1, pady=(5, 5))
        club_entry_tree = Entry(root_treeview_edit, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                cursor="star",
                                bg="#D4E2D0")
        club_entry_tree.grid(row=2, column=1, pady=(5, 5))
        nationality_entry_tree = Entry(root_treeview_edit, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                                       cursor="star",
                                       bg="#D4E2D0")
        nationality_entry_tree.grid(row=3, column=1, pady=(5, 5))
        age_entry_tree = Entry(root_treeview_edit, width=35, justify="center", font=("Comic Sans", 9, "bold"),
                               cursor="star",
                               bg="#D4E2D0")
        age_entry_tree.grid(row=4, column=1)
        # make labels
        first_name_label_tree = Label(root_treeview_edit, text="First name", justify="center",
                                      font=("Comic Sans", 11, "bold"),
                                      cursor="star", fg="#C7A8B1", bg="#A29476")
        first_name_label_tree.grid(row=0, column=0, padx=5, pady=(5, 5))
        last_name_label_tree = Label(root_treeview_edit, text="Last name", justify="center",
                                     font=("Comic Sans", 11, "bold"),
                                     cursor="star", fg="#C7A8B1", bg="#A29476")
        last_name_label_tree.grid(row=1, column=0, padx=5, pady=(5, 5))
        club_label_tree = Label(root_treeview_edit, text="Club", justify="center", font=("Comic Sans", 11, "bold"),
                                cursor="star", fg="#C7A8B1", bg="#A29476")
        club_label_tree.grid(row=2, column=0, padx=5, pady=(5, 5))
        nationality_label_tree = Label(root_treeview_edit, text="Nationality", justify="center",
                                       font=("Comic Sans", 11, "bold"),
                                       cursor="star", fg="#C7A8B1", bg="#A29476")
        nationality_label_tree.grid(row=3, column=0, padx=5, pady=(5, 5))
        age_label_tree = Label(root_treeview_edit, text="Age", justify="center", font=("Comic Sans", 11, "bold"),
                               cursor="star", fg="#C7A8B1", bg="#A29476")
        age_label_tree.grid(row=4, column=0, padx=5, pady=(5, 5))
        #now define the binding
        for footballer in tree_footballers.selection():
            player = tree_footballers.item(footballer)
            record = player["values"]
            #insert into entries
            first_name_entry_tree.insert(0, record[1])
            last_name_entry_tree.insert(0, record[2])
            club_entry_tree.insert(0, record[3])
            nationality_entry_tree.insert(0, record[4])
            age_entry_tree.insert(0, str(record[5]))
        root_treeview_edit.mainloop()


    def see_records(self, table_name):
        global view_root
        global tree_footballers
        # create the connection and get all records
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        my_cursor.execute("""SELECT oid, * FROM """ + table_name)
        list_entries = my_cursor.fetchall()
        connection.close()
        # create a treeview to see these items with a root a frame
        view_root = Tk()
        view_root.title("ALL RECORDS")
        view_root.geometry("520x400")
        view_root["bg"] = "#A29476"
        players_frame = LabelFrame(view_root, text="PLAYER DATABASE", bg="#ABCABD", fg="#EEEEFC",
                                   font=("Comic Sans", 14, "bold"), labelanchor="n", width="500", cursor="target",
                                   height=400)
        players_frame.grid(padx=(10, 10), pady=(10, 0),row=0, column=0, )  # put it in the middle
        players_frame.grid_rowconfigure(0, weight=1)
        players_frame.grid_columnconfigure(0, weight=1)
        # create tree to show footballers
        columns = ( "ID","FIRST NAME", "SECOND NAME", "CLUB", "NATIONALITY", "AGE")
        tree_footballers = ttk.Treeview(players_frame, show='headings', columns=columns, height=15)
        # define the headings
        tree_footballers.heading(0, text="ID",anchor=tkinter.W)
        tree_footballers.heading(1, text="FIRST NAME", anchor=tkinter.W)
        tree_footballers.heading(2, text="LAST NAME", anchor=tkinter.W)
        tree_footballers.heading(3, text="CLUB", anchor=tkinter.W)
        tree_footballers.heading(4, text="NATIONALITY", anchor=tkinter.W)
        tree_footballers.heading(5, text="AGE", anchor=tkinter.W)
        #tree_footballers.heading("ID", text="ID", anchor=tkinter.W)
        #redefine column dimensions
        tree_footballers.column("ID", width=25,)
        tree_footballers.column("FIRST NAME", width=100, stretch=NO)
        tree_footballers.column("SECOND NAME", width=100, stretch=NO)
        tree_footballers.column("CLUB", width=100, stretch=NO)
        tree_footballers.column("NATIONALITY", width=100, stretch=NO)
        tree_footballers.column("AGE", width=40, stretch=NO)
        tree_footballers.tag_configure("orow")
        # create a style for the headings
        style = ttk.Style(view_root)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="#99DA7C", foreground="#A74356")
        # populate the list
        for record in list_entries:
            record_update = list()
            record_update.append(str(record[0]))
            record_update.append(record[1])
            record_update.append(record[2])
            record_update.append(record[3])
            record_update.append(record[4])
            record_update.append(str(record[5]))
            record_update_tuple = tuple(record_update)
            tree_footballers.insert('', tkinter.END, values=record_update_tuple)
        # put the tree on the frame
        tree_footballers.pack(fill= tkinter.BOTH, expand = True)
        # create a scrollbar for the tree
        my_scrollbar = Scrollbar(view_root, orient=tkinter.VERTICAL, command=tree_footballers.yview)
        tree_footballers.configure(yscrollcommand=my_scrollbar.set)
        my_scrollbar.grid(row=0, column=1, sticky='ns')
        '''
        here we will bind the view in order to select the item and open a new root
        '''
        tree_footballers.bind("<Double-Button-1>", self.open_entry)
        view_root.mainloop()

    '''MENU PART'''

    def cancel_gui(self):
        root.destroy()

    def create_main_gui(self):
        global root
        root = Tk()
        root.title("SQL TRAINING")
        root.iconbitmap(r"2020-world11-men-1100-names.ico")
        root.geometry("850x300")
        root["bg"] = "#B5EFEE"
        # create three buttons and a frame
        app_menu = LabelFrame(root, text="Football Database", bg="#CEDE2F", fg="#EEEEFC",
                              font=("Comic Sans", 20, "bold"), labelanchor="n", width="600", cursor="target",
                              height=200)
        app_menu.grid(padx=50, pady=30, row=0, column=0, )  # put it in the middle
        app_menu.grid_rowconfigure(0, weight=1)
        app_menu.grid_columnconfigure(0, weight=1)
        # buttons
        add_button = Button(app_menu, fg="#151714", bg="#5BBD2A", font=("Comic Sans", 11, "bold"), bd=5,
                            cursor="target", width=18, height=2, justify="center", text="ADD", command=self.open_add)
        select_button = Button(app_menu, fg="#151714", bg="#2092B0", font=("Comic Sans", 11, "bold"), bd=5,
                               cursor="target", width=18, height=2, justify="center", text="VIEW/EDIT",
                               command=self.open_edit)
        delete_button = Button(app_menu, fg="#151714", bg="#C9334F", font=("Comic Sans", 11, "bold"), bd=5,
                               cursor="target", width=18, height=2, justify="center", text="DELETE",
                               command=self.open_delete)
        view_all_button = Button(app_menu, fg="#151714", bg="#A29476", font=("Comic Sans", 11, "bold"), bd=5,
                                 cursor="target", width=18, height=2, justify="center", text="VIEW ALL",
                                 command=lambda: self.see_records(self.table)
                                 )
        add_button.grid(row=0, column=0, padx=10, pady=15, ipady=20)
        select_button.grid(row=0, column=1, padx=10, pady=15, ipady=20)
        delete_button.grid(row=0, column=2, padx=10, pady=15, ipady=20)
        view_all_button.grid(row=0, column=3, padx=10, pady=15, ipady=20)
        cancel_button = Button(app_menu, fg="#151714", bg="#BDBCAF", font=("Comic Sans", 11, "bold"), bd=5,
                               cursor="target", height=2, justify="center", text="CANCEL", command=self.cancel_gui)
        cancel_button.grid(row=1, column=0, columnspan=4, padx=10, sticky="nsew")

        root.mainloop()
