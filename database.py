

import os
import validation

user_db_path = "data/user_record/"


def create(account_number, first_name, last_name, email, password):
    

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(account_number):
        return False

    if does_email_exist(email):
        print("user already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(account_number) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(account_number) + ".txt")
        if not does_file_contain_data:
            delete(account_number)

    else:

        f.write(str(user_data))
        completion_state = True

    finally:

        f.close()
        return completion_state


def read(user_account_number):
    # find user with account number
    # fetch content of the file

    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number + "r")

    except FileNotFoundError:

        print("user not found")

    except FileExistsError:

        print("user doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(account_number):
    print("update user record")
    


def delete(account_number):
    
    is_delete_successful = False

    if os.path.exists(user_db_path + str(account_number) + ".txt"):

        try:
            os.remove(user_db_path + str(account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful


def does_email_exist(email):
    all_users = (os.listdir(user_db_path))

    for user in all_users:
        if email in all_users:
            return True
    return False


def does_account_number_exist(account_number):
    all_users = (os.listdir(user_db_path))

    for user in all_users:

        if user == str(account_number) + ".txt":
            return True

    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ",")

        if password == user[3]:
            return user

    return False
