to_seconds = 24 * 60 * 60
to_minute = 24 * 60
to_hour = 24
second = "seconds"
n = 31
my_var = "PyCharm and Python"


def day_unit(number, unit):
    """
    print("Awesome!")
    print("Result is below : ")
    """
    if unit == "Hour":
        return f"{number} days are {number * to_seconds} {unit}"
    elif unit == "Minute":
        return f"{number} days are {number * to_minute} {unit}"
    else:
        return "Unsupported Unit"


def scope_check():
    print(my_var)


"""
seconds_unit(n)
seconds_unit(n - 1)
seconds_unit(n - 2)
seconds_unit(n - 3)
"""


def validate_and_execute(days_and_unit_dictionary):
    try:
        days_and_units = int(days_and_unit_dictionary["days"])
        # we want to do conversion only for positive integers
        if days_and_units > 0:
            days_units = day_unit(days_and_units, days_and_unit_dictionary["unit"])
            print(days_units)
        elif days_and_units == 0:
            print("You entered 0. Please enter a valid number.")
        else:
            print("You entered a negative value, no conversion for you!")

    except ValueError:
        print("Ouch! You entered a wrong input and you mustn't ruin me!")
