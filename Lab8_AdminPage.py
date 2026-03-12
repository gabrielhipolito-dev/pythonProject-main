from Lab8_Class import *
import sqlite3
OD = OopDesign()
quit_code = 1


def main(user):
    global quit_code
    quit_code = 1
    # ------------------------------------- Window Initialization with Scrollbar:------------------------------------ #
    window, sub_frame = window_startup("Lab8_AdminPage", "1366x768")

    # ----------------------------------------- Frame Initialization: ----------------------------------------------- #
    heading_frame, content_frame, data_frame = frame_startup_admin(sub_frame)
    # ------------------------------------------------ Page Header: ------------------------------------------------- #
    
    # Edited by cieloromo
    OD.new_frame(heading_frame, 0, 10, 1166, 15, "#FFA27F")
    OD.new_frame(heading_frame, 50, 30, 1066, 15, "#FFA27F")
    OD.new_frame(heading_frame, 50, 230, 1066, 15, "#FFA27F")
    OD.new_frame(heading_frame, 0, 250, 1166, 15, "#FFA27F")
    OD.new_label_title(heading_frame, "ORATRICE MECANIQUE \nD'ANALYSE CARDINALE", 583, 130)
    
    #   Edited by Jamez0529
    OD.new_label_title(heading_frame, "GIT PULL \nN PUSH", 583, 130)

    # ------------------ Basic Info ------------------ #
    def close():
        window.destroy()

    def info():
        clear_widget(data_frame)

        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Personal_InfoTbl")
        rows = cur.fetchall()

        column_list = ["first_name", "middle_name", "last_name", "suffix", "DOB", "gender", "nationality",
                       "civil_status", "department", "designation", "dept_status", "employee_status", "paydate",
                       "employee_number", "contact_no", "email", "social_media", "social_media_no", "address1",
                       "address2", "city", "state", "country", "zip_code", "filepath"]
        # prints the heading of the table
        for i in range(len(column_list)):
            grid_cell_1(data_frame, column_list[i], 0, i, "center")

        # prints the contents of the table
        row = 1
        for data in rows:
            for i in range(len(data)):
                grid_cell_1(data_frame, data[i], row, i, "left")
            row += 1

        con.close()

    def payroll():
        clear_widget(data_frame)

        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Payroll")
        rows = cur.fetchall()

        column_list = ["employee_number", "basic_income", "honorarium_income", "other_income", "gross_income",
                       "regular_deduction", "other_deduction", "total_deduction", "net_income"]
        # prints the heading of the table
        for i in range(len(column_list)):
            grid_cell_2(data_frame, column_list[i], 0, i, "center")

        # prints the contents of the table
        row = 1
        for data in rows:
            for i in range(len(data)):
                grid_cell_2(data_frame, data[i], row, i, "left")
            row += 1

        con.close()

    def account():
        clear_widget(data_frame)

        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM User_Info")
        rows = cur.fetchall()

        column_list = ["employee_number", "username", "password", "confirm_password", "user_type", "user_status"]
        # prints the heading of the table
        for i in range(len(column_list)):
            grid_cell_2(data_frame, column_list[i], 0, i, "center")

        # prints the contents of the table
        row = 1
        for data in rows:
            for i in range(len(data)):
                grid_cell_2(data_frame, data[i], row, i, "left")
            row += 1

        con.close()

    def add_info():
        global quit_code
        quit_code = "info"
        window.destroy()

    def add_payroll():
        global quit_code
        quit_code = "payroll"
        window.destroy()

    def add_account():
        global quit_code
        quit_code = "account"
        window.destroy()

    OD.new_command_button(content_frame, "INFO", 50, 70, "WHITE", "#38688F", 15, 2, info)
    OD.new_command_button(content_frame, "PAYROLL", 200, 70, "WHITE", "#38688F", 15, 2, payroll)
    OD.new_command_button(content_frame, "ACCOUNT", 350, 70, "WHITE", "#38688F", 15, 2, account)

    OD.new_command_button(content_frame, "ADD INFO", 550, 70, "WHITE", "#DCB04F", 15, 2, add_info)
    OD.new_command_button(content_frame, "ADD PAYROLL", 700, 70, "WHITE", "#DCB04F", 15, 2, add_payroll)
    OD.new_command_button(content_frame, "ADD ACCOUNT", 850, 70, "WHITE", "#DCB04F", 15, 2, add_account)

    OD.new_command_button(content_frame, "LOGOUT", 1000, 70, "WHITE", "GRAY", 15, 2, close)

    # ------------------ Return Main Loop ------------------ #
    #   prints the current user
    OD.new_label(content_frame, f"Logged in as: {user[1]} ({user[4]})", 900, 20)

    window.mainloop()


def main_call(user):
    main(user)
    return quit_code


if __name__ == "__main__":
    main(['', '', '', '', ''])

# Reference:
# https://www.plus2net.com/python/tkinter-sqlite.php
