from Lab8_Class import *
import sqlite3
OD = OopDesign()


def main(user):
    # ------------------------------------- Window Initialization with Scrollbar:------------------------------------ #
    window, sub_frame = window_startup("Lab8_C", "1366x768")

    # ----------------------------------------- Frame Initialization: ----------------------------------------------- #
    heading_frame, info_frame, income_frame, honor_frame, other_frame, summary_frame = frame_startup_c(sub_frame)

    # ------------------------------------------------ Page Header: ------------------------------------------------- #
    OD.new_frame(heading_frame, 0, 10, 1166, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 30, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 50, 230, 1066, 15, "#C8A079")
    OD.new_frame(heading_frame, 0, 250, 1166, 15, "#C8A079")
    OD.new_label_title(heading_frame, "ORATRICE'S \nCHOICE PAYROLL", 583, 130)

    # ------------------ Basic Info ------------------ #
    OD.new_frame(info_frame, 50, 30, 300, 300, "#555555")
    OD.new_image(info_frame, "Resources/Dark Furina.png", 53, 33, 290, 290)
    OD.new_label(info_frame, "Search Employee:", 50, 400)

    first_name = OD.new_label_entry_2(info_frame, "First Name:", 550, 50, 25)
    middle_name = OD.new_label_entry_2(info_frame, "Middle Name:", 550, 100, 25)
    surname = OD.new_label_entry_2(info_frame, "Surname:", 550, 150, 25)
    civil_status = OD.new_label_entry_2(info_frame, "Civil Status:", 550, 200, 25)
    dependents = OD.new_label_entry_2(info_frame, "Qualified Dependents\nStatus:", 550, 250, 25)
    pay_date = OD.new_label_entry_2(info_frame, "Pay Date:", 550, 300, 25)
    employee_number = OD.new_label_entry_2(info_frame, "Employee Number:", 50, 350, 20)
    employee_status = OD.new_label_entry_2(info_frame, "Employee Status:", 550, 350, 25)
    designation = OD.new_label_entry_2(info_frame, "Designation:", 550, 400, 25)
    department = OD.new_label_entry_2(info_frame, "Department:", 50, 450, 20)

    # ------------------ Basic Income ------------------ #
    rate_hour = OD.new_label_entry_2(income_frame, "Rate / Hour:", 50, 50, 20)
    hour_cutoff = OD.new_label_entry_2(income_frame, "No. of Hours / Cut Off:", 50, 100, 20)
    income_cutoff = OD.new_label_entry_2(income_frame, "Income / Cut Off:", 50, 150, 20)
    sss_contribution = OD.new_label_entry_2(income_frame, "SSS Contribution:", 550, 50, 25)
    philhealth_contribution = OD.new_label_entry_2(income_frame, "PhilHealth Contribution:", 550, 100, 25)
    pag_ibig_contribution = OD.new_label_entry_2(income_frame, "Pag-Ibig Contribution:", 550, 150, 25)
    income_tax_contribution = OD.new_label_entry_2(income_frame, "Income Tax Contribution:", 550, 200, 25)

    # ------------------ Honorarium ------------------ #
    honor_rate_hour = OD.new_label_entry_2(honor_frame, "Rate / Hour:", 50, 50, 20)
    honor_hour_cutoff = OD.new_label_entry_2(honor_frame, "No. of Hours / Cut Off:", 50, 100, 20)
    honor_income_cutoff = OD.new_label_entry_2(honor_frame, "Income / Cut Off:", 50, 150, 20)
    sss_loan = OD.new_label_entry_2(honor_frame, "SSS Loan:", 550, 50, 25)
    pag_ibig_loan = OD.new_label_entry_2(honor_frame, "Pag-ibig Loan:", 550, 100, 25)
    faculty_savings_deposit = OD.new_label_entry_2(honor_frame, "Faculty Savings Loan:", 550, 150, 25)
    faculty_savings_loan = OD.new_label_entry_2(honor_frame, "Faculty Savings Deposit:", 550, 200, 25)
    salary_loan = OD.new_label_entry_2(honor_frame, "Salary Loan:", 550, 250, 25)
    other_loan = OD.new_label_entry_2(honor_frame, "Other Loan:", 550, 300, 25)

    # ------------------ Others ------------------ #
    other_rate_hour = OD.new_label_entry_2(other_frame, "Rate / Hour:", 50, 50, 20)
    other_hour_cutoff = OD.new_label_entry_2(other_frame, "No. of Hours / Cut Off:", 50, 100, 20)
    other_income_cutoff = OD.new_label_entry_2(other_frame, "Income / Cut Off:", 50, 150, 20)
    total_deductions = OD.new_label_entry_2(other_frame, "Total Deductions:", 550, 50, 25)

    # ------------------ Summary ------------------ #
    gross_income = OD.new_label_entry_2(summary_frame, "Gross Income:", 50, 50, 20)
    net_income = OD.new_label_entry_2(summary_frame, "Net Income:", 50, 100, 20)

    # ------------------ Button Commands ------------------ #
    #   lists containing the variables of entries / combo boxes / option menus / calendars
    entry_list = [first_name, middle_name, surname, civil_status, dependents, pay_date, employee_number,
                  employee_status, designation, department]
    income_list = [rate_hour, hour_cutoff, income_cutoff, honor_rate_hour, honor_hour_cutoff, honor_income_cutoff,
                   other_rate_hour, other_hour_cutoff, other_income_cutoff]
    contribution_list = [sss_contribution, philhealth_contribution, pag_ibig_contribution, income_tax_contribution]
    loan_list = [sss_loan, pag_ibig_loan, faculty_savings_deposit, faculty_savings_loan, salary_loan,
                 other_loan]

    def search():
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        emp_num = employee_number.get()
        cur = con.cursor()
        #   retrieves the data from the row with a matching employee_number
        cur.execute(f"SELECT * FROM Personal_InfoTbl WHERE employee_number = {emp_num}")
        rows = cur.fetchone()

        try:
            data = [rows[0], rows[1], rows[2], rows[7], rows[10], rows[12], emp_num, rows[11], rows[9], rows[8]]
            #   inserts the retrieved data into the entries
            for i in range(len(entry_list)):
                change_data(entry_list[i], data[i])
            #   attaches the user's uploaded image into the GUI
            OD.new_image(info_frame, rows[-1], 53, 33, 290, 290)
            popup_box("Searched Successfully!")

            # uploading previously saved data:
            cur.execute(f"SELECT * FROM Payroll WHERE employee_number = {emp_num}")
            rows1 = cur.fetchone()
            update_list = [income_cutoff, honor_income_cutoff, other_income_cutoff, gross_income, total_deductions,
                           net_income]
            update_data = [rows1[1], rows1[2], rows1[3], rows1[4], rows1[7], rows1[8]]

            for j in range(len(update_data)):
                change_data(update_list[j], update_data[j])

        except TypeError:
            popup_box("User Not Found!")

        con.close()

    def compute_gross():
        try:
            inc = float(rate_hour.get()) * float(hour_cutoff.get())
        except ValueError:  # if entry has no input
            inc = 0
        change_data(income_cutoff, "%.2f" % inc)

        try:
            hinc = float(honor_rate_hour.get()) * float(honor_hour_cutoff.get())
        except ValueError:  # if entry has no input
            hinc = 0
        change_data(honor_income_cutoff, "%.2f" % hinc)

        try:
            oinc = float(other_rate_hour.get()) * float(other_hour_cutoff.get())
        except ValueError:  # if entry has no input
            oinc = 0
        change_data(other_income_cutoff, "%.2f" % oinc)

        change_data(gross_income, "%.2f" % (inc + hinc + oinc))

    def compute_net():
        gross = float(gross_income.get())

        # ---------- SSS Contribution Computation ---------- #
        sss_con, g_var = 180.00, gross

        while sss_con < 900.00 and g_var >= 4250:
            g_var -= 500.00
            sss_con += 22.50

        # ---------- PhilHealth contribution ---------- #
        s_co = pay_date.get().split("/")
        salary_cutoff_year = int(s_co[2]) + 2000

        if salary_cutoff_year == 2019:
            premium_rate, upper_value = 0.00, 50000
        elif salary_cutoff_year == 2020:
            premium_rate, upper_value = 0.03, 60000
        elif salary_cutoff_year == 2021:
            premium_rate, upper_value = 0.035, 70000
        elif salary_cutoff_year == 2022:
            premium_rate, upper_value = 0.04, 80000
        elif salary_cutoff_year == 2023:
            premium_rate, upper_value = 0.045, 90000
        else:  # for years 2024-2025
            premium_rate, upper_value = 0.05, 100000

        if gross <= 10000:
            philhealth_con = 10000 * premium_rate
            # if gross earnings is less than PhP 10,000, a fixed value is deducted
        elif 10000 > gross > upper_value:
            philhealth_con = gross * premium_rate
            # if gross earnings is more than 10k but less than the upper value,
            # the contribution is based on a percentage of the premium rate
        else:
            philhealth_con = upper_value * premium_rate
            #  if gross earnings is higher than year's upper value (e.g. year 2024 = 100,000),
            #  a fixed value is also deducted

        # ----------Withholding Tax ---------- #
        if 0.00 <= gross <= 10417.00:
            withholding_tax = 0
        elif 10417.00 < gross <= 16666.00:
            over = gross - 10417.00
            withholding_tax = 0 + (over * 0.15)
        elif 16666.00 < gross <= 33332.00:
            over = gross - 16667.00
            withholding_tax = 937.50 + (over * 0.2)
        elif 33332.00 < gross <= 83332.00:
            over = gross - 33333.00
            withholding_tax = 4270.70 + (over * 0.25)
        elif 83332.00 < gross <= 333332.00:
            over = gross - 83333.00
            withholding_tax = 16770.70 + (over * 0.3)
        else:  # for gross pay equal to 333,333 and above
            over = gross - 333333.00
            withholding_tax = 91770.70 + (over * 0.35)

        withholding_tax = round(withholding_tax, 2)

        change_data(sss_contribution, "%.2f" % sss_con)
        change_data(philhealth_contribution, "%.2f" % philhealth_con)
        change_data(pag_ibig_contribution, "%.2f" % 100)
        change_data(income_tax_contribution, "%.2f" % withholding_tax)

        deduction = float(sss_con + philhealth_con + withholding_tax + 100)

        for items in loan_list:
            try:
                deduction += float(items.get())
            except ValueError:
                # if entry is blank
                pass

        #   updating entries
        change_data(total_deductions, "%.2f" % deduction)
        change_data(net_income, "%.2f" % (gross - deduction))

    def save_to_db():
        reg_ded = float(sss_contribution.get()) + float(philhealth_contribution.get()) + \
                  float(pag_ibig_contribution.get()) + float(income_tax_contribution.get())
        other_deduction_list = [sss_loan, pag_ibig_loan, faculty_savings_loan, faculty_savings_deposit,
                                salary_loan, other_loan]
        other_ded = 0.00

        for items in other_deduction_list:
            try:
                other_ded += float(items.get())
            except ValueError:
                pass

        upload_list = [employee_number, income_cutoff, honor_income_cutoff, other_income_cutoff, gross_income,
                       reg_ded, other_ded, total_deductions, net_income]

        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        query = f"INSERT INTO Payroll VALUES ("
        #   creating query for database
        for items in upload_list:
            try:
                query += f"'{str(items.get())}',"
            except AttributeError:
                query += f"'{str(items)}',"

        query1 = query[:-1]
        query1 += ")"

        #   executing, committing and closing the database
        try:
            con.execute(query1)
            con.commit()
            popup_box("Saved Successfully!")
        except sqlite3.IntegrityError:
            popup_box("Data Already Exists in Database! \nConsider Updating Data Instead.")

        con.close()

    def update():
        con = sqlite3.connect("Resources\\OOP_Lab6_DB.db")
        #   check if user already has data in database
        emp_num = employee_number.get()
        cur = con.cursor()
        #   retrieves the data from the row with a matching employee_number
        cur.execute(f"SELECT * FROM Payroll WHERE employee_number = {emp_num}")

        if cur.fetchone() is None:
            #   cancels update if data does not exist
            popup_box("Data Does Not Exist in Database! \nConsider Saving Data Instead.")
        else:
            emp_num = employee_number.get()
            reg_ded = (float(sss_contribution.get()) + float(philhealth_contribution.get()) +
                       float(pag_ibig_contribution.get()) + float(income_tax_contribution.get()))
            other_deduction_list = [sss_loan, pag_ibig_loan, faculty_savings_loan, faculty_savings_deposit,
                                    salary_loan, other_loan]
            other_ded = 0.00

            for items in other_deduction_list:
                try:
                    other_ded += float(items.get())
                except ValueError:
                    pass

            column_list = ["employee_number", "basic_income", "honorarium_income", "other_income", "gross_income",
                           "regular_deduction", "other_deduction", "total_deduction", "net_income"]
            upload_list = [employee_number, income_cutoff, honor_income_cutoff, other_income_cutoff, gross_income,
                           reg_ded, other_ded, total_deductions, net_income]
            query = f"UPDATE Payroll SET "
            #   f"UPDATE Payroll SET employee_number='{employee_number.get()}', basic_income='{basic_income.get()}',
            #   .... WHERE employee_number='{employee_number.get()}'"
            for i in range(len(column_list)):
                query += f"{column_list[i]}='"
                try:
                    query += f"{upload_list[i].get()}',"
                except AttributeError:
                    query += f"{upload_list[i]}',"

            query1 = query[:-1]
            query1 += f" WHERE employee_number = '{emp_num}'"
            print(query1)
            con.execute(query1)
            con.commit()
            popup_box("Data Updated Successfully!")

        con.close()

    def clear():
        # deletes all entry input
        for items in entry_list:
            clear_data(items)
        for items in income_list:
            clear_data(items)
        for items in contribution_list:
            clear_data(items)
        for items in loan_list:
            clear_data(items)

        clear_data(total_deductions)
        clear_data(gross_income)
        clear_data(net_income)

    # ------------------ Buttons ------------------ #
    OD.new_command_button(info_frame, "Search", 300, 400, "WHITE", "#C83B48", 10, 1, search)

    OD.new_command_button(summary_frame, "GROSS INCOME", 550, 50, "WHITE", "#38688F", 15, 2, compute_gross)
    OD.new_command_button(summary_frame, "NET INCOME", 700, 50, "WHITE", "#38688F", 15, 2, compute_net)
    OD.new_command_button(summary_frame, "SAVE", 850, 50, "WHITE", "#72AAE3", 10, 2, save_to_db)
    OD.new_command_button(summary_frame, "UPDATE", 950, 50, "WHITE", "#72AAE3", 10, 2, update)
    OD.new_command_button(summary_frame, "NEW", 1050, 50, "WHITE", "#DCB04F", 10, 2, clear)

    # ------------------ Return Main Loop ------------------ #
    #   prints the current user
    OD.new_label(info_frame, f"Logged in as: {user[1]} ({user[4]})", 900, 20)

    window.mainloop()


def main_call(user):
    main(user)
    return


if __name__ == "__main__":
    main(['', '', '', '', ''])
