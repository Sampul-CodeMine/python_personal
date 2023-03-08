import datetime as dt


class Member:
    # Constructor for the Member class
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.date_joined = dt.date.today()
        self.is_active = True

    def show_date_joined(self):
        # function to return a string
        string = f"{self.fullname} joined on {self.date_joined: %m/%d/%y}."
        return string

    def activate(self, yesno):
        self.is_active = yesno


# create a new member
new_member = Member("ROBOT", "Test User")
# Member's active state
print(new_member.is_active)

# Activate the new member
new_member.activate(False)

# is the new member still alive?
print(new_member.is_active)

print(new_member.show_date_joined())


