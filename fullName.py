import sys

def fullName(firstName, lastName):
    if (not firstName or not lastName):
        print("Please include both first name and last name.")
        return None
    elif (not isinstance(firstName, str) or not isinstance(lastName, str) or not firstName.isalnum() or not lastName.isalnum()):
        print("That is not a valid name.")
        return None
    else:
        full_name = firstName + " " + lastName
        return full_name