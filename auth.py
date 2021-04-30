
import random
import database
from session import (delete_login_session, create_login_session)
import validation


def init():
    print("Welcome to Bank of Larry")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    global account1

    account1 = account_number_from_user

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = input("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)
        if user:
            create_login_session(account1)
            bank_operation(user)
        else:
            print("Invalid account or Password")

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation(user)
    elif selected_option == 2:

        withdrawal_operation(user)
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        delete_login_session(account1)
        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(user):
    current_balance = user[4]
    withdrawal_amount = int(input("Enter the amount you would like to withdraw. \n"))
    current_balance = int(current_balance) - withdrawal_amount
    user[4] = current_balance

    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    user_db_path = "data/user_record/"
    f = open(user_db_path + str(account1) + ".txt", "w")
    f.write(updated_user)
    f.close()

    print("You successfully withdrew {}".format(withdrawal_amount))
    print("Your current balance is now {}".format(current_balance))

    return bank_operation(user)


def deposit_operation(user):
    current_balance = user[4]
    deposit_amount = int(input("Enter the amount you would like to deposit. \n"))
    current_balance = int(current_balance) + deposit_amount
    user[4] = current_balance

    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    user_db_path = "data/user_record/"
    f = open(user_db_path + str(account1) + ".txt", "w")
    f.write(updated_user)
    f.close()

    print("You have successfully deposited {}".format(deposit_amount))
    print("Your current balance is now {}".format(current_balance))

    return bank_operation(user)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]


def logout():
    delete_login_session(account1)
    login()


init()
