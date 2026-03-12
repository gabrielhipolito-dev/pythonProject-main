from Lab8_Login import main_call as login
from Lab8_B import main_call as lab_b
from Lab8_C import main_call as lab_c
from Lab8_D import main_call as lab_d
from Lab8_AdminPage import main_call as admin
#   This comment was added to test GitHub Push Feature
#   This comment was added to test Github Pull


def admin_loop(info):
    while True:
        #   opens respective gui based on button pressed
        match admin(info):
            case 1:
                break
            case "info":
                lab_b(info)
            case "payroll":
                lab_c(info)
            case "account":
                lab_d(info)


def main():
    while True:
        info = login()
        #   opens login gui, then opens respective gui based on user account type
        match info[4]:
            case "Quit":
                break
            case "HR":
                lab_b(info)
            case "Accounting":
                lab_c(info)
            case "Employee":
                lab_d(info)
            case "Admin":
                admin_loop(info)


if __name__ == "__main__":
    main()
