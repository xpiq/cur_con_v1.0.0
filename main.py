# calculation formula for one dollar
som_rate = 11140

# names

base_currency_unit_name = 'dollar'
result_currency_unit_name = 'som'


# calculate


def base_to_result(user_input):
    return f"there are {som_rate * user_input} {result_currency_unit_name}"


# check is input is digit


def validate_input_print_result():
    try:
        user_input_number = int(usd_values_list)
        if user_input_number > 0:
            calculated_value = base_to_result(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("your value is zero!")
        else:
            print("you entered value below zero")
    except ValueError:
        print("ValueError!!!")

# waiting for user input


user_input = ""

while user_input != "exit":
    user_input = input('enter amount in usd or type exit for quit\n')
    for usd_values_list in user_input.split(","):
        validate_input_print_result()
