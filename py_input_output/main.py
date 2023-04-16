#!/usr/bin/python3

def write_to_json(data, fn):
    with open(fn, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=3)
        return True
    return


def read_from_json(fn):
    with open(fn, mode="r") as f:
        data = json.load(f)
        return data
    return

def prompt():
    prmpt = """Program Sample
    =====================================
    1. Add Data
    2. View Data
    3. Edit/Update Data
    4. Delete Data
    5. Exit
    """
    print(prmpt)

def get_data():
    fname = input("First Name: ")
    lname = input("Last Name: ")
    age = input("Age: ")
    data = {"firstname": fname, "lastname": lname, "age    ":age}
    return data

def add_data(fn):
    try:
        rawdata = read_from_json(fn)
    except Exception:
        rawdata = []
    data = get_data()
    rawdata.append(data)
    write_to_json(rawdata, fn)

def view_data(fn):
    data = read_from_json(fn)
    count = 1
    for item in data:
        print(f"Data {count}:")
        for key, val in item.items():
            print(f"{key.capitalize()}: {val}")
        print("")
        count += 1
    return data

def delete_data(fn):
    data = view_data(fn)
    d_len = len(data)
    resp = int(input("Delete Data #: ? "))
    if resp < 0 or resp > d_len:
        print(f"\nData {resp} not found.\n")
    else:
        newdata = []
        count = 0
        for item in data:
            if count == (resp - 1):
                ...
                count += 1
            else:
                newdata.append(item)
                count += 1
        write_to_json(newdata, fn)
    return True

def edit_data(fn):
    data = view_data(fn)
    d_len = len(data)
    resp = int(input("Edit Data #: ? "))
    if resp < 0 or resp > d_len:
        print(f"\nData {resp} not found.\n")
    else:
        newdata = []
        count = 0
        for item in data:
            if count == (resp - 1):
                data = get_data()
                newdata.append(data)
                count += 1
            else:
                newdata.append(item)
                count += 1
        write_to_json(newdata, fn)
    return True


if __name__ == "__main__":
    import json
    filename = "persons.json"
    while True:
        try:
            prompt()
            choice = input("Choose: ")
            if choice == "1":
                add_data(filename)
                print("\nAdded Successfully.\n\n")
            elif choice == "2":
                print("\nViewing Data\n")
                view_data(filename)
                print("")
            elif choice == "3":
                print("\nEditing/Updating Data\n")
                if edit_data(filename):
                    print("\nData updated successfully.\n")
            elif choice == "4":
                print("\nDeleting Data\n")
                if delete_data(filename):
                    print("\nData deleted successfully.\n")
            elif choice == "5":
                print("Exiting")
                exit()
            else:
                print("Invalid option. choose again.")
        except (KeyboardInterrupt, EOFError):
            print("Program suspended.")
