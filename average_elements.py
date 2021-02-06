import sys

def averageElements(listofElements):
    if not list:
        print("You provided a empty list.")
        return None
    elif (not isinstance(listofElements, list)):
        print("That is not a list.")
        return None
    elif (len(listofElements) == 0):
        print("You cannot divide by 0");
        return None
    else:
        average = (sum(listofElements) / len(listofElements))
        return average