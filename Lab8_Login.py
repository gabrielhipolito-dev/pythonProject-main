from Lab8_Class import *
import sqlite3
OD = OopDesign()
user_credential = ['', '', '', '', "Quit"]


def main():
    global user_credential
    user_credential = ['', '', '', '', "Quit"]
    # ------------------------------------- Window Initialization with Scrollbar:------------------------------------ #
    window, sub_frame = window_startup("Lab8_Login", "1366x600")

    # ----------------------------------------- Frame Initialization: ----------------------------------------------- #
    heading_frame, content_frame = frame_startup_login(sub_frame)
    # ------------------------------------------------ Page Header: ------------------------------------------------- #
    OD.new_frame(heading_frame, 0, 10, 1166, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 30, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 230, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 0, 250, 1166, 15, "#C8A079")
    OD.new_label_title(heading_frame, "FOCALOR RESEARCH \nINSTITUTE", 583, 130)

    # ------------------ Basic Info ------------------ #
    username = OD.new_label_entry_3(content_frame, "Username:", 400, 50, 35)
    password = OD.new_label_entry_pass(content_frame, "Password:", 400, 100, 35)

    def login():
        global user_credential
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM User_Info WHERE username='{username.get()}' AND password='{password.get()}' ")
        rows = cur.fetchone()
        if rows is None:
            # if user is not found in User_Info table
            popup_box("User Not Found!")
        else:
            window.destroy()
            user_credential = rows
        con.close()

    def close():
        window.destroy()

    OD.new_command_button(content_frame, "LOGIN", 400, 200, "WHITE", "#38688F", 15, 2, login)
    OD.new_command_button(content_frame, "EXIT", 660, 200, "WHITE", "GRAY", 15, 2, close)
    # ------------------ Return Main Loop ------------------ #
    window.mainloop()


def main_call():
    main()
    return user_credential


if __name__ == "__main__":
    main()
