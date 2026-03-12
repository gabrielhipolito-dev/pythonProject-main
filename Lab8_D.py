from Lab8_Class import *
import sqlite3
OD = OopDesign()


def main(user):
    # ------------------------------------- Window Initialization with Scrollbar:------------------------------------ #
    window, sub_frame = window_startup("Lab8_D", "1366x768")

    # ----------------------------------------- Frame Initialization: ----------------------------------------------- #
    heading_frame, info_frame = frame_startup_d(sub_frame)

    # ------------------------------------------------ Page Header: ------------------------------------------------- #
    OD.new_frame(heading_frame, 0, 10, 1166, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 30, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 230, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 0, 250, 1166, 15, "#C8A079")
    OD.new_label_title(heading_frame, "ORATRICE MECANIQUE \nD'ANALYSE CARDINALE", 583, 130)

    # ----------- User Account Information ---------- #
    OD.new_frame(info_frame, 50, 30, 300, 300, "#555555")
    OD.new_image(info_frame, "Resources/Dark Furina.png", 53, 33, 290, 290)

    first_name = OD.new_label_entry_3(info_frame, "First Name:", 400, 50, 20)
    middle_name = OD.new_label_entry_3(info_frame, "Middle Name:", 635, 50, 13)
    last_name = OD.new_label_entry_3(info_frame, "Last Name:", 800, 50, 16)
    suffix = OD.new_label_entry_3(info_frame, "Suffix:", 1000, 50, 7)
    department = OD.new_label_entry_3(info_frame, "Department:", 400, 100, 35)
    designation = OD.new_label_entry_3(info_frame, "Designation:", 800, 100, 25)
    username = OD.new_label_entry_3(info_frame, "Username:", 400, 150, 35)
    password = OD.new_label_entry_pass(info_frame, "Password:", 400, 200, 35)
    confirm_password = OD.new_label_entry_pass(info_frame, "Confirm Password:", 400, 250, 35)
    user_type = OD.new_label_entry_3(info_frame, "User Type:", 400, 300, 35)
    user_status = OD.new_label_entry_3(info_frame, "User Status:", 800, 300, 25)
    employee_number = OD.new_label_entry_3(info_frame, "Employee Number:", 400, 350, 35)

    # ------------------ Button Commands ------------------ #
    entry_list = [first_name, middle_name, last_name, suffix, department, designation]
    user_info_list = [username, password, confirm_password, user_type, user_status]

    def search():
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        emp_num = employee_number.get()
        cur = con.cursor()
        #   retrieves the data from the row with a matching employee_number
        cur.execute(f"SELECT * FROM Personal_InfoTbl WHERE employee_number = {emp_num}")
        rows = cur.fetchone()
        con.close()

        try:
            data = [rows[0], rows[1], rows[2], rows[3], rows[8], rows[9]]
            #   inserts the retrieved data into the entries
            for i in range(len(entry_list)):
                change_data(entry_list[i], data[i])
            #   attaches the user's uploaded image into the GUI
            OD.new_image(info_frame, rows[-1], 53, 33, 290, 290)
        except TypeError:
            popup_box("User Not Found!")

    def update():
        #   checks if the password is correctly entered:
        if password.get() == confirm_password.get():
            con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM User_Info WHERE employee_number = {employee_number.get()}")
            data = [employee_number, username, password, confirm_password, user_type, user_status]
            retrieve_data = cur.fetchone()
            if retrieve_data is None:
                #   if user info does not exist, create a new row of data
                query = f"INSERT INTO User_Info VALUES ("
                #   creating query for database
                for items in data:
                    try:
                        query += f"'{str(items.get())}',"
                    except AttributeError:
                        query += f"'{str(items)}',"
                query1 = query[:-1]
                query1 += ")"
                con.execute(query1)
                con.commit()
                popup_box("Successfully Added New Data!")
            else:
                #   if user info already exists, check if username is already taken by different account
                cur.execute(f"SELECT * FROM User_Info WHERE username='{username.get()}'")
                retrieved2 = cur.fetchone()
                print(retrieved2)
                print(data[1].get())
                if retrieved2 is not None and str(retrieved2[0]) != data[0].get():
                    popup_box("Username already taken!")
                else:
                    columns = ["employee_number", "username", "password", "confirm_password", "user_type",
                               "user_status"]
                    query = f"UPDATE User_Info SET "
                    for i in range(len(columns)):
                        query += f"{columns[i]}='{data[i].get()}',"
                    query1 = query[:-1]
                    query1 += f"WHERE employee_number='{employee_number.get()}'"
                    popup_box("Successfully Updated Data!")

                    con.execute(query1)
                    con.commit()

            con.close()
        else:
            popup_box("Password does not match!")

    def delete():
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        query = f"DELETE FROM User_Info WHERE employee_number='{employee_number.get()}'"
        con.execute(query)
        con.commit()
        con.close()
        popup_box("Data successfully deleted!")
        cancel()

    def cancel():
        for items in entry_list:
            clear_data(items)
        for items in user_info_list:
            clear_data(items)
        clear_data(employee_number)
        OD.new_image(info_frame, "Resources/Dark Furina.png", 53, 33, 290, 290)
        if user[4] == "Employee":
            change_data(employee_number, user[0])

    OD.new_command_button(info_frame, "Search", 800, 375, "WHITE", "#C83B48", 10, 1, search)
    OD.new_command_button(info_frame, "UPDATE", 400, 430, "WHITE", "#38688F", 15, 2, update)
    OD.new_command_button(info_frame, "DELETE", 550, 430, "WHITE", "#DCB04F", 15, 2, delete)
    OD.new_command_button(info_frame, "CANCEL", 700, 430, "WHITE", "GRAY", 15, 2, cancel)

    # ------------------ Return Main Loop ------------------ #
    #   prints the current user
    OD.new_label(info_frame, f"Logged in as: {user[1]} ({user[4]})", 900, 20)
    #   if logged-in user is an employee, limit editing to own account
    if user[4] == "Employee":
        change_data(employee_number, user[0])
        search()
    window.mainloop()


def main_call(user):
    main(user)
    return


if __name__ == "__main__":
    main(['', '', '', '', ''])
