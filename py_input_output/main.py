#!/usr/bin/python3
"""This is a simple module that does the following:
1. Add data to a file in json format
2. View the files
3. Edit/Update a specific data in the file
4. Delete a specific data in the file
"""


def clear_screen() -> None:
    """Function that clears the screen"""
    from sys import platform as p
    from os import system as s
    os_platform = p
    if os_platform == "win32":
        s("cls")
    elif os_platform == "linux":
        s("clear")
    return

def prompter():
    """This is function that gives a prompt for the task to be carried out."""
    prompt = """
                 Welcome to Sampul-CodeMine Space.
    =========================================================

    1. Add Data
    2. View Data
    3. Edit/Update Data
    4. Delete Data
    5. Exit
    """
    print(prompt)

def accept_int(prompt: str) -> int | None:
    """This is function that accepts integer input from a user.
    Args:
        prompt (str): Prompt to specify the datatype to input.

    Return:
        int | None: if input is of type int, return int else None.

    Raises:
        TypeError: if the data is not of type `int`
        ValueError: if no data is provided
        Exception: if data is empty
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    while True:
        try:
            data = input(f"Enter {prompt}: ")
            if data == '':
                raise Exception("Data is required")
            if data.isdigit():
                data = int(data)
                if type(data) == int:
                    return data
                else:
                    raise ValueError("Numeric data is required.")
            else:
                raise TypeError("Numeric data is required.")
        except ValueError as err:
            print(err)
        except (Exception, TypeError) as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            exit()
    return

def accept_str(prompt: str) -> str | None:
    """This is function that accepts String input from a user.

    Args:
        prompt (str): Prompt to specify the datatype to input.

    Return:
        str | None: string type else None.

    Raises:
        ValueError: if there is no data provided or string is empty
        TypeError: if the data procided is all digits
        Exception: if data is empty
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    while True:
        try:
            data = input(f"Enter {prompt}: ")
            if data == '':
                raise ValueError("Data is required.")
            if data.isdigit():
                raise TypeError("Data must not be numeric.")
            return data
        except (ValueError, TypeError, Exception) as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram interrupted.")
            exit()
    return

def get_user_data() -> dict | None:
    """Function to get data from a user.
    Data to get includes the firstname, lastname, age, gender, and email

    Returns:
        dict | None: A dictionary if data collection was successful else None.
    Raises:
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    data = {}
    try:
        data["firstname"] = accept_str("First Name").capitalize()
        data["lastname"] = accept_str("Last Name").capitalize()
        data["email"] = accept_str("Email ID").lower()
        data["gender"] = accept_str("Gender").upper()
        data["age"] = accept_int("Age")
        return data
    except (KeyboardInterrupt, EOFError):
        print("\nProgram halted")
    return

def read_from_json_file(fn) -> list | None:
    """This is a function that reads data from a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        ValueError: if filename is empty
        TypeError: if the data procided is all digits
        FileNotFoundError: if specified file is not found
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    from os import path
    try:
        if fn == "":
            raise ValueError("Filename is required")
        if path.getsize(fn) == 0:
            return []
        with open(fn, mode="r") as f:
            data = json.load(f)
            return data
    except ValueError as err:
        print(err)
    except FileNotFoundError as err:
        print(f"The file '{fn}' was not found.")
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted.")
        exit()
    return

def write_to_json_file(data: list, fn: str) -> bool | None:
    """This is a function that writes `data` to a JSON file `fn`.

    Args:
        data (list): the data (list of dictionaries) to be written to the
    JSON file
        fn (str): the file to write JSON object to

    Returns:
        bool | None: If successful, returns True else return None.

    Raises:
        TypeError - if `data` is not of type list
        Exception - if specified file is not found
        (KeyboardInterrupt, EOFError) - if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        if type(data) is not list:
            raise TypeError("Invalid data cannot be added.")
        if fn == "" or fn is None:
            raise Exception("Filename is required.")
        with open(fn, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=3, sort_keys=True)
            return True
    except TypeError as err:
        print(err)
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return

def add_data_to_db(fn: str) -> bool | None:
    """Function to collect data from the user and append collected data to
    the already existing data in the database.

    Args:
        fn (str): The file to append data to.

    Raises:
        Exception: if `fn` is empty or data read from the JSON file is None
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.

    Returns:
        bool | None: Returns True if successful else None
    """
    try:
        if fn == "" or fn is None:
            raise Exception("Filename is required.")
        try:
            raw_data = read_from_json_file(fn)
        except Exception:
            raw_data = []
        data = get_user_data()
        if data is not None:
            raw_data.append(data)
            write_to_json_file(raw_data, fn)
            return True
        else:
            raise Exception("We could not add data at this time. Please try\
                            again")
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return

def view_data_from_db(fn: str) -> list | None:
    """This is a function that views the data in a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        ValueError: if filename is empty
        TypeError: if the data procided is all digits
        FileNotFoundError: if specified file is not found
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        if fn == "" or fn is None:
            raise Exception("Filename is required.")
        data = read_from_json_file(fn)
        count = 1
        for item in data:
            print(f"Data #{count}")
            print(f"\tFirstname : {item['firstname']}")
            print(f"\tLastname  : {item['lastname']}")
            print(f"\tEmail ID  : {item['email']}")
            print(f"\tGender    : {item['gender']}")
            print(f"\tAge       : {item['age']}")
            count += 1
            print("")
        return data
    except TypeError as err:
        print(err)
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return

def edit_data_in_db(fn: str) -> bool | None:
    """This is a function that edits and updates data in a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        Exception: if `fn` is empty or data read from the JSON file is None
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        data = view_data_from_db(fn)
        data_len = len(data)
        edit_opt = accept_int("Record Number to Edit")
        if edit_opt < 0 or edit_opt > data_len:
            raise Exception(f"\nData {edit_opt} not found.\n")
        new_data = []
        count = 0
        for item in data:
            if count == (edit_opt - 1):
                nw_dict = get_user_data()
                new_data.append(nw_dict)
                count += 1
            else:
                new_data.append(item)
                count += 1
        write_to_json_file(new_data, fn)
        return True
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return

def delete_data_from_db(fn: str) -> bool | None:
    """This is a function that removes and updates data in a JSON file

    Args:
        fn (str): The file to read json object from

    Return:
        list | None: List object if True or file empty else None.

    Raises:
        Exception: if `fn` is empty or data read from the JSON file is None
        (KeyboardInterrupt, EOFError): if [CTRL+C]/[CTRL+Z] keys are pressed.
    """
    try:
        data = view_data_from_db(fn)
        data_len = len(data)
        del_opt = accept_int("Record Number To Delete")
        if del_opt < 0 or del_opt > data_len:
            raise Exception(f"\nData {del_opt} not found.\n")
        new_data = []
        count = 0
        for item in data:
            if count == (del_opt - 1):
                count += 1
            else:
                new_data.append(item)
                count += 1
        write_to_json_file(new_data, fn)
        return True
    except Exception as err:
        print(err)
    except (KeyboardInterrupt, EOFError):
        print("\nProgram was halted.")
        exit()
    return


if __name__ == "__main__":
    import json
    filename = "persons.json"

    clear_screen()
    while True:
        try:
            prompter()
            choice = accept_int("Choice")
            if choice == 1:
                clear_screen()
                print("==== A D D I N G    D A T A ====\n")
                if add_data_to_db(filename) is not None:
                    print("\nData was successfully added to the database.\n")
                else:
                    print("\nUnable to save data to the database.\n")
            elif choice == 2:
                clear_screen()
                print("==== V I E W I N G    D A T A ====\n")
                if view_data_from_db(filename) is None:
                    print("\nUnable to view information in the database.\n")
            elif choice == 3:
                clear_screen()
                print("==== U P D A T I N G    A    R E C O R D ====\n")
                if edit_data_in_db(filename) is True:
                    print("\nData was successfully updated.\n")
                else:
                    print("\nUnable to update and save data to the database.")
            elif choice == 4:
                clear_screen()
                print("==== D E L E T I N G    A    R E C O R D ====\n")
                if delete_data_from_db(filename) is True:
                    print("\nData was successfully removed.\n")
                else:
                    print("\nUnable to remove and save data to the database.")
            elif choice == 5:
                clear_screen()
                print("==== E X I T I N G    A P P L I C A T I O N ====\n")
                print("\nThank you for dropping by. Do have a lovely day.")
                exit(1)
        except ValueError as err:
            print(err)
        except (KeyboardInterrupt, EOFError):
            print("\nProgram Interrupted\n")
            exit(1)
