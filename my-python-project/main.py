from helper import validate_and_execute
import os
print(os.name)
guineas = ["Guinea", "Guinea Bissau", "Guinea Equatoriale"]
for guinea_in_africa in guineas:
    print(guinea_in_africa)
guineas.append("Papua Nuova Guinea")
print("-----------------------\nAdded another Guinea\n-----------------------")
for guinea_in_world in guineas:
    print(guinea_in_world)

srilanka = ["Sri Lanka", "Colombo", "Sri Jayawardanapura Kotte"]
for sri_lanka in srilanka:
    print(sri_lanka)
srilanka.append(1948)
print("-----------------------\nAdded another detail\n-----------------------")
for sri_lanka in srilanka:
    print(sri_lanka)
print("List vs Set")
my_list = ["List", "String", "No other datatype", "Index", "[]", "Order: Normal", "ON"]
my_set = {"Set", "String", 12, "No indexes", "{}", "Order: Random", "OR"}
print(my_list)
print(my_set)
my_list.remove("ON")
my_set.remove("OR")
print(my_list)
print(my_set)
name = "Sithila";
print(f"My name is {name}")
print("Hey user, enter a number of days and conversion unit!")
day = ""
while day != "exit":
    day = input("Enter here : ")
    day_and_unit = day.split(":")
    days_and_unit_dictionary = {
        "days": day_and_unit[0],
        "unit": day_and_unit[1]
    }
    validate_and_execute(days_and_unit_dictionary)

