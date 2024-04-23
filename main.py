from tkinter import ttk, messagebox, Scrollbar, Spinbox, Label, StringVar, Entry
from tkinter import font as tkFont
from tkcalendar import DateEntry
from datetime import datetime
import tkinter as tk
import sqlite3

class GUI:

  def __init__(self, root):
    self.root = root
    self.root.title("Hedi Airport")
    self.root.geometry("730x400")
    self.root.configure(bg='#E6E6FA')
    self.connection = sqlite3.connect("terminal.db")
    self.conn.execute('PRAGMA foreign_keys = ON')
    self.cursor = self.connection.cursor()
    self.selected = {}  # Use in delete_operation
    self.backup = {}  # Use in delete_operation
    self.welcome_page()
#Page 1 - Welcome Page——————————————————————————————————————————————————————————————————
  def welcome_page(self):
    self.clear_screen()
    welcome_label = tk.Label(self.root,
                             text="Welcome to Hedi Airport",
                             font=('Helvetica', 30),
                             bg='#E6E6FA')
    welcome_label.pack(pady=20)
    enter_button = tk.Button(self.root,
                             text="Start",
                             width=10,
                             height=2,
                             command=self.function_page,
                             font=('Helvetica', 20),
                             bg='white')
    enter_button.pack(pady=50)
    author_label = tk.Label(self.root,
                            text="Coded by Jiahong Han(jh3984)",
                            font=('Helvetica', 20),
                            bg='#E6E6FA')
    author_label.pack(pady=20)
#Page 2 - Choose Function Page——————————————————————————————————————————————————————————
  def function_page(self):
    self.clear_screen()
    self.root.title("Hedi Airport")
    function_label = tk.Label(self.root,
                              text="Please Choose Function:",
                              font=('Helvetica', 20),
                              bg='#E6E6FA')
    function_label.pack(pady=20)
    add_button = tk.Button(self.root,
                           text="Add",
                           width=15,
                           height=1,
                           command=lambda: self.table_page("Add"),
                           bg='white')
    add_button.pack(pady=10)
    delete_button = tk.Button(self.root,
                              text="Delete",
                              width=15,
                              height=1,
                              command=lambda: self.table_page("Delete"),
                              bg='white')
    delete_button.pack(pady=10)
    query_button = tk.Button(self.root,
                             text="Query",
                             width=15,
                             height=1,
                             command=lambda: self.table_page("Query"),
                             bg='white')
    query_button.pack(pady=10)
    alter_button = tk.Button(self.root,
                             text="Alter",
                             width=15,
                             height=1,
                             command=lambda: self.table_page("Alter"),
                             bg='white')
    alter_button.pack(pady=10)
    additional_button = tk.Button(self.root,
                                  text="Additional Function",
                                  width=15,
                                  height=1,
                                  command=self.addtional_page,
                                  bg='white')
    additional_button.pack(pady=10)
    return_button = tk.Button(self.root,
                              text="Return",
                              width=8,
                              height=1,
                              command=self.welcome_page,
                              bg='white')
    return_button.pack(pady=10)
#Page 2.5 Additional Function Page---------------------------------------------
  def addtional_page(self):
    self.clear_screen()
    self.root.title("Hedi Airport - Addtional Function")
    start_label = tk.Label(self.root,
                           text="Please Choose Addtional Function:",
                           font=('Helvetica', 20),
                           bg='#E6E6FA')
    start_label.pack(pady=20)
    summary_button = tk.Button(self.root,
                               text="Summary Statistics",
                               width=30,
                               height=1,
                               command=lambda: self.addtional_function_page("Statistics"),
                               bg='white')
    summary_button.pack(pady=20)
    summary_button = tk.Button(self.root,
                               text="Find Flight for Departure or Destination",
                               width=30,
                               height=1,
                               command=lambda: self.addtional_function_page("Navigate"),
                               bg='white')
    summary_button.pack(pady=20)
    return_button = tk.Button(self.root,
                              text="Return",
                              width=8,
                              height=1,
                              command=self.function_page,
                              bg='white')
    return_button.pack(pady=20)
  #Page 2.5.1 Statistics Page-------------------------------------------------------
  def addtional_function_page(self, selected_function):
    self.clear_screen()
    self.root.title("Hedi Airport - " f"{selected_function}")
    # Operation for Statistics Summary----------------------------------------------
    if selected_function == "Statistics":
      pilot_num = self.cursor.execute(
          "select count(*) from pilot").fetchone()[0]
      flight_num = self.cursor.execute(
          "select count(*) from flight").fetchone()[0]
      aircraft_num = self.cursor.execute(
          "select count(*) from aircraft").fetchone()[0]
      total_label = tk.Label(
          self.root,
          text="Summary: "
          f"We have: {pilot_num}  Pilots, {flight_num} Flights, {aircraft_num} Aircrafts",
          bg='#E6E6FA')
      total_label.grid(row=1, column=0, pady=5)
      query_label = tk.Label(
          self.root,
          text="Choose date and Query Flights between these Date:",
          bg='#E6E6FA')
      query_label.grid(row=2, column=0, pady=5)
      start_date_label = tk.Label(self.root, text="Start Date:", bg='#E6E6FA')
      start_date_label.grid(row=3, column=0, pady=10)
      start_date_entry = DateEntry(self.root,
                                   width=12,
                                   bg='white',
                                   borderwidth=3,
                                   date_pattern="yyyy-mm-dd")
      start_date_entry.grid(row=3, column=1, pady=10)
      end_date_label = tk.Label(self.root, text="End Date:", bg='#E6E6FA')
      end_date_label.grid(row=4, column=0, pady=10)
      end_date_entry = DateEntry(self.root,
                                 width=12,
                                 bg='white',
                                 borderwidth=3,
                                 date_pattern="yyyy-mm-dd")
      end_date_entry.grid(row=4, column=1, pady=10)
      comfirm_button = tk.Button(
          self.root,
          text="Comfirm",
          width=8,
          height=1,
          command=lambda: self.query_flights_date(start_date_entry.get_date(),
                                                  end_date_entry.get_date()),
          bg='white')
      comfirm_button.grid(row=3, column=2, pady=10)
      return_button = tk.Button(self.root,
                                text="Return",
                                width=8,
                                height=1,
                                command=self.addtional_page,
                                bg='white')
      return_button.grid(row=4, column=2, pady=10)
    #Additional Operation for Navigate-------------------------------------------
    if selected_function == "Navigate":
      start_label = tk.Label(self.root,
                                text="Choose your Departure and Destination:",
                                font=('Helvetica', 20),
                                bg='#E6E6FA')
      start_label.pack(pady=10)
      start_place_label = tk.Label(self.root, text="Departure:", bg='#E6E6FA')
      start_place_label.pack(pady=1)
      start_place_entry = tk.Entry(self.root, width=22)
      start_place_entry.pack(pady=1)
      end_date_label = tk.Label(self.root, text="Destination:", bg='#E6E6FA')
      end_date_label.pack(pady=1)
      end_place_entry = tk.Entry(self.root, width=22)
      end_place_entry.pack(pady=1)
      list = [
          desc[1] for desc in self.cursor.execute(
              f"pragma table_info (flight)").fetchall()
      ]
      self.tree = ttk.Treeview(self.root, columns=list, show="headings")
      comfirm_button = tk.Button(
        self.root,
        text="Comfirm",
        width=8,
        height=1,
        command=lambda: self.query_flight_location(self.tree,
                                                   start_place_entry.get(), 
                                                   end_place_entry.get()), 
        bg='white')
      comfirm_button.pack(pady=5)
      return_button = tk.Button(
        self.root,
        text="Return",
        width=8,
        height=1,
        command =self.addtional_page,
        bg='white')
      return_button.pack(pady=5)
      all_data = self.cursor.execute(f"select * from flight").fetchall()
      for row in all_data:
        self.tree.insert("", "end", values=row)
      for col in list:
        self.tree.heading(col, anchor="center", text=col)
        max_width = max(tkFont.Font().measure(str(row[list.index(col)]))
                        for row in all_data)
        min_width = tkFont.Font().measure(col) + 10
        self.tree.column(col, anchor="center", width=max(min_width, max_width))
      self.tree.pack(expand=True, fill='both',side= tk.BOTTOM)
      yscrollbar = Scrollbar(self.tree)
      yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      yscrollbar.config(command=self.tree.yview)
      xscrollbar = Scrollbar(self.tree, orient=tk.HORIZONTAL)
      xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
      self.tree.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
#Page 3 - Choose which table to operate—————————————————————————————————————————————————
  def table_page(self, selected_function):
    self.clear_screen()
    self.root.title("Hedi Airport - "
                    f"{selected_function}")
    start_label = tk.Label(self.root,
                           text=f"Please Choose Table ({selected_function}):",
                           font=('Helvetica', 20),
                           bg='#E6E6FA')
    start_label.pack(pady=20)
    pilot_button = tk.Button(
        self.root,
        text="Pilot",
        width=15,
        height=1,
        command=lambda: self.operation_page(selected_function, "pilot"),
        bg='white')
    pilot_button.pack(pady=10)
    aircraft_button = tk.Button(
        self.root,
        text="Aircraft",
        width=15,
        height=1,
        command=lambda: self.operation_page(selected_function, "aircraft"),
        bg='white')
    aircraft_button.pack(pady=10)
    flight_button = tk.Button(
        self.root,
        text="Flight",
        width=15,
        height=1,
        command=lambda: self.operation_page(selected_function, "flight"),
        bg='white')
    flight_button.pack(pady=10)
    who_drove_plane_button = tk.Button(
        self.root,
        text="Who_Drove_Plane",
        width=15,
        height=1,
        command=lambda: self.operation_page(selected_function,
                                            "who_drove_plane"),
        bg='white')
    who_drove_plane_button.pack(pady=10)
    return_button = tk.Button(self.root,
                              text="Return",
                              width=8,
                              height=1,
                              command=self.function_page,
                              bg='white')
    return_button.pack(pady=30)
#Page 4 - Operation Page————————————————————————————————————————————————————————————————
  def operation_page(self, selected_function, selected_table):
    self.clear_screen()
    self.root.title(f"Hedi Airport - {selected_function} {selected_table}")
    # Operation for Add----------------------------------------------------------------
    if selected_function == "Add":
      list = [
          desc[1] for desc in self.cursor.execute(
              f"pragma table_info({selected_table})").fetchall()
      ]
      all_data = self.cursor.execute(
          f"select * from {selected_table}").fetchall()
      tree = ttk.Treeview(self.root, columns=list, show="headings")
      for col in list:
        tree.heading(col, anchor="center", text=col)
        max_width = max(tkFont.Font().measure(str(row[list.index(col)]))
                        for row in all_data)
        min_width = tkFont.Font().measure(col) + 10
        tree.column(col, anchor="center", width=max(min_width, max_width))
      for row in all_data:
        tree.insert("", "end", values=row)
      tree.pack(expand=True, fill='both')
      entry_widgets = {}
      entry_frame = tk.Frame(self.root, bg='#E6E6FA')
      entry_frame.pack(pady=10)
      if selected_table == "flight":
        xscrollbar = Scrollbar(tree, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(xscrollcommand=xscrollbar.set)
        print(xscrollbar.config())
      yscrollbar = Scrollbar(tree)
      yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      yscrollbar.config(command=tree.yview)
      tree.configure(yscrollcommand=yscrollbar.set)
      count = 0
      for list_name in list:  # List from {selected_table}
        label = tk.Label(entry_frame,
                         text=f"{list_name}:",
                         font=('Helvetica', 10),
                         bg='#E6E6FA')
        label.grid(row=count // 2, column=(count % 2) * 2, pady=3)
        if list_name == "flight_date":
          entry_widgets[list_name] = DateEntry(entry_frame,
                                               width=18,
                                               bg='#E6E6FA',
                                               foreground='white',
                                               borderwidth=3,
                                               date_pattern="yyyy-mm-dd")
        else:
          entry_widgets[list_name] = tk.Entry(entry_frame)
        entry_widgets[list_name].grid(row=count // 2,
                                      column=(count % 2) * 2 + 1,
                                      pady=5)
        count += 1
      #Operation Buttons
      add_button = tk.Button(
          self.root,
          text="Add",
          width=8,
          height=1,
          command=lambda: self.add(selected_table, entry_widgets, tree),
          bg='white')
      add_button.pack(side=tk.LEFT, pady=5)
      return_button = tk.Button(
          self.root,
          text="Return",
          width=8,
          height=1,
          command=lambda: self.table_page(selected_function),
          bg='white')
      return_button.pack(side=tk.RIGHT, pady=5)
    # Operation for Delete-----------------------------------------------------------
    if selected_function == "Delete":
      list = [
          desc[1] for desc in self.cursor.execute(
              f"pragma table_info({selected_table})").fetchall()
      ]
      self.tree = ttk.Treeview(self.root, columns=list, show="headings")
      all_data = self.cursor.execute(
          f"select * from {selected_table}").fetchall()
      for col in list:
        self.tree.heading(col, anchor="center", text=col)
        max_width = max(tkFont.Font().measure(str(row[list.index(col)]))
                        for row in all_data)
        min_width = tkFont.Font().measure(col) + 10
        self.tree.column(col, anchor="center", width=max(min_width, max_width))
      for row in all_data:
        self.tree.insert("", "end", values=row)
      self.tree.pack(expand=True, fill="both")
      if selected_table == "flight":
        xscrollbar = Scrollbar(self.tree, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=xscrollbar.set)
      yscrollbar = Scrollbar(self.tree)
      yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      yscrollbar.config(command=self.tree.yview)
      self.tree.configure(yscrollcommand=yscrollbar.set)
      #Operation Buttons
      delete_button = tk.Button(
          self.root,
          text="Delete",
          width=8,
          height=1,
          command=lambda: self.delete(
              selected_table, self.get_selected_row(), self.tree),
          bg='white')
      delete_button.pack(side=tk.LEFT, pady=5)
      restore_button = tk.Button(self.root,
                                 text="Restore",
                                 width=8,
                                 height=1,
                                 command=lambda: self.restore_button_clicked(
                                     selected_table, self.tree),
                                 bg='white')
      restore_button.pack(side=tk.LEFT, pady=5)
      return_button = tk.Button(
          self.root,
          text="Return",
          width=8,
          height=1,
          command=self.function_page,
          bg='white')
      return_button.pack(side=tk.RIGHT, pady=5)
    #Operation for Alter--------------------------------------------------------------
    if selected_function == "Alter":
      list = [
          desc[1] for desc in self.cursor.execute(
              f"pragma table_info({selected_table})").fetchall()
      ]
      all_data = self.cursor.execute(
          f"select * from {selected_table}").fetchall()
      self.tree = ttk.Treeview(self.root, columns=list, show="headings")
      for col in list:
        self.tree.heading(col, anchor="center", text=col)
        max_width = max(tkFont.Font().measure(str(row[list.index(col)]))
                        for row in all_data)
        min_width = tkFont.Font().measure(col) + 10
        self.tree.column(col, anchor="center", width=max(min_width, max_width))
      self.tree.bind(
          "<Double-1>",
          lambda event: self.new_window(event, list, selected_table))
      entry_widgets = {}
      entry_frame = tk.Frame(self.root, bg='#E6E6FA')
      entry_frame.pack(pady=10)
      if selected_table == "flight":  # Xscrollbar will hide the last information for no reason
        xscrollbar = Scrollbar(self.tree, orient=tk.HORIZONTAL)
        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=xscrollbar.set)
      yscrollbar = Scrollbar(self.tree)
      yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      yscrollbar.config(command=self.tree.yview)
      self.tree.configure(yscrollcommand=yscrollbar.set)
      count = 0
      for row in all_data:
        self.tree.insert("", "end", values=row)
      self.tree.pack(expand=True, fill='both')
      return_button = tk.Button(
          self.root,
          text="Return",
          width=8,
          height=1,
          command=lambda: self.table_page(selected_function),
          bg='white')
      return_button.pack(side=tk.RIGHT, pady=5)
    #Operation for Query--------------------------------------------------------------
    if selected_function == "Query":
      all_data = self.cursor.execute(
          f"select * from {selected_table}").fetchall()
      list = [
          desc[1] for desc in self.cursor.execute(
              f"pragma table_info({selected_table})").fetchall()
      ]
      selected_list = tk.StringVar(self.root)
      selected_list.set(list[0])
      list_dropdown = ttk.Combobox(self.root,
                                   width=20,
                                   height=len(list),
                                   textvariable=selected_list,
                                   state="readonly")
      list_dropdown["values"] = list
      list_dropdown.pack(pady=10)
      input_entry = tk.Entry(self.root, width=22)
      input_entry.pack(pady=10)
      confirm_button = tk.Button(
          self.root,
          text="Comfirm",
          width=8,
          height=1,
          command=lambda: self.query(selected_table, selected_list.get(
          ), input_entry.get()),
          bg='white')
      confirm_button.pack(pady=5)
      return_button = tk.Button(
          self.root,
          text="Return",
          width=8,
          height=1,
          command=lambda: self.table_page(selected_function),
          bg='white')
      return_button.pack(pady=5)
      self.tree = ttk.Treeview(self.root, columns=list, show="headings")
      for row in all_data:
        self.tree.insert("", "end", values=row)
      for col in list:
        self.tree.heading(col, anchor="center", text=col)
        max_width = max(tkFont.Font().measure(str(row[list.index(col)]))
                        for row in all_data)
        min_width = tkFont.Font().measure(col) + 10
        self.tree.column(col, anchor="center", width=max(min_width, max_width))
      self.tree.pack(expand=True, fill='both')
      yscrollbar = Scrollbar(self.tree)
      yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
      yscrollbar.config(command=self.tree.yview)
      self.tree.configure(yscrollcommand=yscrollbar.set)
#Add Function------------------------------------------------------------------
  def add(self, table, entry_widgets, tree):
    data_values = [
        entry_widgets[list_name].get() for list_name in entry_widgets
    ]
    pilot_num = self.cursor.execute(
      "select count(*) from pilot").fetchone()[0]
    flight_num = self.cursor.execute(
      "select count(*) from flight").fetchone()[0]
    aircraft_num = self.cursor.execute(
      "select count(*) from aircraft").fetchone()[0]
    if len(entry_widgets["flight_id"].get())>flight_num:
      messagebox.showerror("Error",
                           f"Invalid Number for flight_id ")
      return
    elif len(entry_widgets["aircraft_id"].get())>aircraft_num:
      messagebox.showerror("Error",
                           f"Invalid Number for aircraft_id ")
      return
    elif len(entry_widgets["pilot_id"].get())>pilot_num:
      messagebox.showerror("Error",
                           f"Invalid Number for pilot_id ")
      return
    for list_name in ["start_time", "end_time"]:
      if list_name in entry_widgets:
        time_value = entry_widgets[list_name].get()
        try:
          datetime.strptime(time_value, "%H:%M")
          return True
        except ValueError:
          messagebox.showerror("Error",
                               f"Invalid {list_name} format. Please use hh:mm.")
          return
    if not all(data_values):
      messagebox.showerror("Error", "Please Input All the Data.")
      return
    try:
      self.cursor.execute(
          f"insert into {table} values({','.join(['?']*len(data_values))})",
          tuple(data_values))
      self.connection.commit()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Operation Failed: {e}.")
      return
    else:
      for entry_widget in entry_widgets.values():  # Clear entry widgets
        entry_widget.delete(0, tk.END)
      messagebox.showinfo("Operation Successful",
                          f"Data {data_values} has been Added into {table} Successful.")
    self.refresh_treedata(table, tree)
    return # For use this function again
#Delete Function-----------------------------------------------------------------
  def get_selected_row(self):
    selected = self.tree.selection()
    print(f"Selected Item: {selected}")
    if selected:
      return self.tree.item(selected)['values'][0]
    else:
      return None
  def delete(self, selected_table, selected_row, tree):
    if not selected_row:
      messagebox.showerror("Error",
                           "Please Choose the Row needed to be Deleted.")
      return
    try:
      deleted_data = self.cursor.execute(
          f"select * from {selected_table} where rowid = ?",
          (selected_row, )).fetchone()
      self.backup[selected_table] = deleted_data
      self.cursor.execute(f"delete from {selected_table} where rowid = ?",
                          (selected_row, ))
      self.connection.commit()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Delete Failed：{e}")
      return
    else:
      messagebox.showinfo(
          "Operation Successful",
          f"You Have Deleted flight_id = {selected_row} Successful.")
      self.refresh_treedata(selected_table, tree)
    return # For use this function again
  def restore_button_clicked(self, selected_table, tree):  # Debug test
    self.restore_operation(selected_table, tree)
    print("Restore button clicked.")
  def restore_operation(self, selected_table,
                        tree):  # This function is not working
    selected_row = self.get_selected_row()
    if selected_row is None:
      messagebox.showerror("Error",
                           "There is no Row to be Restored.")
      return
    if selected_table not in self.backup:
      messagebox.showerror("Error", "There is no Data to Restore.")
      return
    print(f"Restored Data: {self.backup[selected_table]}")
    try:
      restored_data = self.backup[selected_table]
      self.cursor.execute(
          f"insert into {selected_table} values {restored_data}")
      self.connection.commit()
    except sqlite3.Error as e:
      messagebox.showerror("Error", f"Restore Failed：{e}")
      return
    else:
      messagebox.showinfo("Operation Successful",
                          f"flight_id = {selected_row} Has Been Restored.")
    self.refresh_treedata(selected_table, tree)
#Alter Function------------------------------------------------------------------
  def new_window(self, event, list, selected_table):
    selected_item = self.tree.selection()[0]
    edit_window = tk.Toplevel(self.root)
    edit_window.title("Edit Data")
    edit_window.geometry("300x350")
    edit_window.configure(bg='#E6E6FA')
    entry_widgets = {}
    for i, list_name in enumerate(list):
      label = tk.Label(edit_window, bg='#E6E6FA', text=f"{list_name}:")
      label.grid(row=i, column=0, pady=5)
      entry_widget = tk.Entry(edit_window)
      entry_widget.insert(0, self.tree.item(selected_item)['values'][i])
      entry_widget.grid(row=i, column=1, pady=5)
      if list_name == "start_date":  # This is not working
        entry_widgets[list_name] = DateEntry(edit_window,
                                 bg='#E6E6FA',
                                 foreground='white',
                                 borderwidth=3,
                                 date_pattern="yyyy-mm-dd")
      else:
        entry_widgets[list_name] = entry_widget
    confirm_button = tk.Button(
        edit_window,
        text="Confirm",
        bg="white",
        command=lambda: self.
        update_data(selected_table, selected_item, entry_widgets, self.tree,
                    edit_window),
    )
    confirm_button.grid(row=i + 1, column=0, pady=5)
    cancel_button = tk.Button(edit_window,
                              bg="white",
                              text="Cancel",
                              command=edit_window.destroy)
    cancel_button.grid(row=i + 1, column=1, pady=5)

  def primary_key(self, table):
    if table != "who_drove_plane":
      return self.cursor.execute(f"pragma table_info({table})").fetchone()[1]
    else:
      return "your_primary_key_list_name"

  def update_data(self, selected_table, selected_item, entry_widgets, tree,
                  edit_window):
    try:
      new_values = [
          entry_widgets[list_name].get() for list_name in entry_widgets
      ]
      if not self.is_valid(selected_table, new_values, entry_widgets):
        raise ValueError("Data Invaild.")
      primary_key = self.primary_key(selected_table)
      condition = f"{primary_key}='{tree.item(selected_item)['values'][0]}'"
      update_query = f"update {selected_table} set {', '.join([f'{col}=?' for col in entry_widgets])} where {condition}"
      self.connection.execute("BEGIN")  # Transaction handling start
      try:
        self.cursor.execute(update_query, new_values)
        self.connection.commit()
        edit_window.destroy()  # Close window if update successful
        self.refresh_treedata(selected_table, tree)
        messagebox.showinfo("Update Successful",
                            "Data has been updated successfully.")
      except sqlite3.Error as e:
        self.connection.rollback(
        )  # Rollback the transaction and undo the update operation
        messagebox.showerror("Error", f"Update failed: {e}")
      finally:
        self.connection.execute("END")  # Transaction handling end
    except ValueError as e:
      messagebox.showerror("Error", str(e))
  def is_valid(self, selected_table, new_values, entry_widgets):
    for list_name, new_value in zip(entry_widgets.keys(), new_values):
      if list_name == "start_date":
        format_str = "%Y-%m-%d"
      elif list_name in ["start_time", "end_time"]:
        format_str = "%H:%M"
      else:
        continue
      try:
        datetime.strptime(new_value, format_str)
      except ValueError:
        return False
    return True
#Query Function------------------------------------------------------------------
  def query(self, selected_table, selected_list, search_value):
    if search_value is None: # This is not working
      messagebox.showerror("Error", f"There is no input in {selected_list}.")
      return
    else:
      query_statement = f"select * from {selected_table} where {selected_list} like ?"
      search_pattern = f"%{search_value}%"  # Fuzzy query
      try:
        query_result = self.cursor.execute(query_statement,
                                           (search_pattern, )).fetchall()
        if not query_result:
          messagebox.showerror(
              "Error",
              f"There is no such Data in Table {selected_table}.")
      except Exception as e:
        return
      self.treelist_width()
      self.tree.delete(*self.tree.get_children()) # Clear Original Tree Data
      for row in query_result:
        self.tree.insert("", "end", values=row)
    return # For use this function again
  def treelist_width(self):
    list = self.tree['columns']
    for col in list:
      self.tree.column(col,
                       anchor="center",
                       minwidth=0,
                       width=tkFont.Font().measure(col))
    for item in self.tree.get_children():
      values = self.tree.item(item, 'values')
      for idx, value in enumerate(values):
        col_width = tkFont.Font().measure(value)
        if col_width > self.tree.column(list[idx], width=None):
          self.tree.column(list[idx], width=col_width)
#Statistics Function------------------------------------------------------------------
  def query_flights_date(self, start_date, end_date):
    if start_date is None or end_date is None:
      messagebox.showerror("Date Error", "Please choose proper Date.")
      return
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date_str = end_date.strftime("%Y-%m-%d")
    query = f"select *, count(*) as flight_count from flight where flight_date between ? and ? group by flight_date"
    list = [
        desc[1] for desc in self.cursor.execute(
            f"pragma table_info(flight)").fetchall()
    ]
    date_range = self.cursor.execute(
        query, (start_date_str, end_date_str)).fetchall()
    self.tree = ttk.Treeview(self.root, columns=list, show="headings")
    for col in list:
      self.tree.heading(col, text=col)
    self.tree.grid(row=5, column=0, columnspan=6, sticky="nsew")
    self.root.grid_rowconfigure(5, weight=1)
    self.root.grid_columnconfigure(1, weight=1)
    yscrollbar = ttk.Scrollbar(self.tree, command=self.tree.yview)
    yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    xscrollbar = ttk.Scrollbar(self.root,
                               orient="horizontal",
                               command=self.tree.xview)
    xscrollbar.grid(row=6, column=0, columnspan=6, sticky="ew")
    self.tree.configure(yscrollcommand=yscrollbar.set,
                        xscrollcommand=xscrollbar.set)
    for row in date_range:
      self.tree.insert("", "end", values=row)
    total_flights = sum(row[1] for row in date_range)
    total_label = tk.Label(
        self.root,
        text=
        f"Between {start_date_str} and {end_date_str} we have {total_flights} flights",
        bg='#E6E6FA')
    total_label.grid(row=1, column=2, pady=5)
    return # For use this function again
#Additional Function - Navigtor------------------------------------------------------
  def query_flight_location(self, tree, start_place, end_place):
    start_place = start_place.replace(" ", "") # Delete space front and back
    end_place = end_place.replace(" ", "")
    if not start_place:
        messagebox.showerror("Error", "Please choose your Departure.")
        return
    query_statement = f"select * from flight where start_place like ?"
    search_pattern = f"%{start_place}%" # Fuzzy query
    try:
        query_result = self.cursor.execute(query_statement, (search_pattern,)).fetchall()
        if not query_result:
            messagebox.showinfo("No Data", f"No flights found for Departure: {start_place}")
            return
    except Exception as e:
        messagebox.showerror("Error", f"{e}")
        return
    self.tree.delete(*tree.get_children()) # Clear Original Tree Data
    if end_place: # row[7] is end_place query result row
      exact_match = [row for row in query_result if row[7] == end_place] 
      fuzzy_match = [row for row in query_result if end_place in row[7]]
      final_result = exact_match + fuzzy_match
    else:
      final_result = query_result
    try:
      if not final_result:
        messagebox.showinfo("No Data", f"No flights found from {start_place} to {end_place}")
        return
    except Exception as e:
      messagebox.showerror("Error", f"{e}")
      return
    for row in final_result:
      self.tree.insert("", "end", values=row)
    return # For use this function again
#Other Function------------------------------------------------------------------
  def refresh_treedata(self, table, tree):
    all_data = self.cursor.execute(f"select * from {table}").fetchall()
    tree.delete(*tree.get_children()) # Clear Original Tree Data
    for row in all_data:
      tree.insert("", "end", values=row)
  def clear_screen(self):
    for widget in self.root.winfo_children():
      widget.destroy()
if __name__ == "__main__":
  root = tk.Tk()
  app = GUI(root)
  root.mainloop()
