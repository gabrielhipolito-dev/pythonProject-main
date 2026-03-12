from Lab8_Class import *
import sqlite3
OD = OopDesign()


def main(user):
    # ------------------------------------- Window Initialization with Scrollbar:------------------------------------ #
    window, sub_frame = window_startup("Lab8_B", "1366x768")

    # ----------------------------------------- Frame Initialization: ----------------------------------------------- #
    (heading_frame, info_frame, dept_frame, contact_info, contact_frame, address,
     address_frame, bot_frame) = frame_startup_b(sub_frame)

    # ------------------ Heading ------------------ #
    OD.new_frame(heading_frame, 0, 10, 1166, 15, "#28f7ce")
    OD.new_frame(heading_frame, 50, 30, 1066, 15, "#185448")
    OD.new_frame(heading_frame, 50, 230, 1066, 15, "#185448")
    OD.new_frame(heading_frame, 0, 250, 1166, 15, "#7eccbc")
    OD.new_label_title(heading_frame, "Bank Information", 583, 130)

    # ------------------ Basic Info ------------------ #
    OD.new_frame(info_frame, 50, 30, 200, 200, "#555555")
    OD.new_image(info_frame, "Resources/Dark Furina.png", 53, 33, 190, 190)

    first_name_entry = OD.new_label_entry(info_frame, "First Name", 280, 70, 22)
    middle_name_entry = OD.new_label_entry(info_frame, "Middle Name", 550, 70, 15)
    last_name_entry = OD.new_label_entry(info_frame, "Last Name", 750, 70, 20)
    suffix_entry = OD.new_label_entry(info_frame, "Suffix", 1000, 80, 8)

    date_of_birth_calendar = OD.new_label_calendar(info_frame, "Date of Birth", 280, 170, 25)
    gender_option, go_var = OD.new_label_option(window, info_frame, "Gender", 600, 170, 15,
                                                ["Male", "Female", "Prefer not to say"])
    nationality_option, no_var = OD.new_label_option(window, info_frame, "Nationality", 800, 170, 10,
                                                     ["Filipino", "Non-Filipino"])
    civil_status_option, cso_var = OD.new_label_option(window, info_frame, "Civil Status", 950, 170, 12,
                                                       ["Single", "Married", "Divorced", "Widowed"])

    # ------------------ Department ------------------ #
    department_entry = OD.new_label_entry(dept_frame, "Department", 50, 10, 50)
    designation_entry = OD.new_label_entry(dept_frame, "Designation", 625, 10, 25)
    dept_status_option, dso_var = OD.new_label_option(window, dept_frame, "Qualified Dept. Status", 925, 10, 15,
                                                      ["Accredited", "Non-Accredited"])
    employee_status_entry = OD.new_label_entry(dept_frame, "Employee Status", 50, 70, 60)
    pay_date_calendar = OD.new_label_calendar(dept_frame, "Pay Date", 725, 70, 13)
    employee_number_entry = OD.new_label_entry(dept_frame, "Employee Number", 900, 70, 18)

    # ------------------ Contact Info ------------------ #
    contact_no_entry = OD.new_label_entry(contact_frame, "Contact No.", 50, 10, 42)
    email_entry = OD.new_label_entry(contact_frame, "Email", 550, 10, 50)

    social_media_option, sem_var = OD.new_label_option(window, contact_frame, "Other (Social Media)", 50, 70, 47,
                                                       ["Facebook", "Twitter", "Instagram", "Others"])
    social_media_no_entry = OD.new_label_entry(contact_frame, "Social Media Account ID/No.", 550, 70, 50)

    # ------------------ Address ------------------ #
    address1_entry = OD.new_label_entry(address_frame, "Address Line 1", 50, 10, 95)
    address2_entry = OD.new_label_entry(address_frame, "Address Line 2", 50, 70, 95)
    city_entry = OD.new_label_entry(address_frame, "City/Municipality", 50, 130, 50)
    state_entry = OD.new_label_entry(address_frame, "State/Province", 625, 130, 43)
    country_option, co_var = OD.new_label_option(window, address_frame, "Country", 50, 190, 57,
                                                 ["Philippines","Singapore", "Japan", "Thailand", "Others"])
    zip_code_entry = OD.new_label_entry(address_frame, "Zip Code", 625, 190, 43)
    path_entry = OD.new_label_entry(address_frame, "Picture path", 50, 250, 95)

    # ------------------ Button Commands ------------------ #

    #   a list containing the variables of entries / combo boxes / option menus / calendars
    entry_list = [first_name_entry, middle_name_entry, last_name_entry, suffix_entry, date_of_birth_calendar,
                  go_var, no_var, cso_var, department_entry, designation_entry, dso_var, employee_status_entry,
                  pay_date_calendar, employee_number_entry, contact_no_entry, email_entry, sem_var,
                  social_media_no_entry, address1_entry, address2_entry, city_entry, state_entry, co_var,
                  zip_code_entry, path_entry]

    def search():
        filepath = open_pic()
        change_data(path_entry, filepath)
        OD.new_image(info_frame, filepath, 53, 33, 190, 190)

    # creating command to obtain entry input and upload to database
    def upload_to_db():
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        query = f"INSERT INTO Personal_InfoTbl VALUES ("
        #   creating query for database
        for items in entry_list:
            query += f"'{str(items.get())}',"
        query1 = query[:-1]
        query1 += ")"

        #   executing, committing and closing the database
        try:
            con.execute(query1)
            popup_box(f"User {employee_number_entry.get()} Saved Successfully!")
            clear()
        #   gives an error if the inputted employee number is already taken
        except sqlite3.IntegrityError:
            popup_box("Employee Number already exists!")

        con.commit()
        con.close()

    # creating command to clear entries
    def clear():
        OD.new_image(info_frame, "Resources/Dark Furina.png", 53, 33, 190, 190)
        for items in entry_list:
            try:
                #  deleting OptionMenu widgets
                items.set("")
            except AttributeError:
                #   deleting Entry widgets
                clear_data(items)

    # ------------------ Buttons ------------------ #
    OD.new_command_button(bot_frame, "Save", 0, 10, "WHITE", "#f53864", 15, 2, upload_to_db)
    OD.new_command_button(bot_frame, "Cancel", 150, 10, "#8A6138", "#f53864", 15, 2, clear)
    OD.new_command_button(info_frame, "Search Image", 148, 235, "#f53864", "#C83B48", 12, 1, search)

    # ------------------ Return Main Loop ------------------ #
    #   prints the current user
    OD.new_label(info_frame, f"Logged in as: {user[1]} ({user[4]})", 900, 20)

    window.mainloop()


def main_call(user):
    main(user)
    return


if __name__ == "__main__":
    main(['', '', '', '', ''])

# References:
# https://www.youtube.com/watch?v=0WafQCaok6g
