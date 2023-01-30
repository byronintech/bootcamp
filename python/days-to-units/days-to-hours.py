calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # Conversion for positive integers only
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
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
    user_input = input(f"Hey {username}, please enter a number of days and I will convert it to hours!\n"
                       "(Example: 1, 2, 3)\n")
    list_of_days = user_input.split(", ")
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
