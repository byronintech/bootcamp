

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])

        # Conversion for positive integers only
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("Error: You entered a 0, please enter a valid positive number")
        else:
            print("Error: You entered a negative number, no conversion for you!")
    except ValueError:
        print("Error: Your input is not a valid number.Don't ruin my program.")


user_input = ""
username = input("Hey, what's your name?\n")

while user_input != "exit":
    print('-' * 60)
    user_input = input(f"Hey {username}, please enter a number of days and conversion unit(minutes or hours)!\n"
                       "Example: 19:minutes\n")
    # user_input = input("Hey user, please enter a number of days and conversion unit(minutes or hours)!\n")
    days_to_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_to_unit[0], "unit": days_to_unit[1]}
    validate_and_execute()

