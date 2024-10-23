#Amany Hussein Mousa 20231026
#Asmaa Hussein Omar 20231021
#Roaa mohammed Sayed 20230142

#test1 bin to dec , input (10101), output(21)
#test2 oct to dec , input(12570), output(5496)
#test3 hex to dec , input (19FDE), output(106462)
#test4 dec to bin , input (29), output(11101)
#test5 dec to oct , input (35), output(43)
#test6 dec to hex , input (172), output(AC)
#test7 oct to bin , input (25), output(010101)
#test8 hex to bin , input (15), output(10101)
#test9 bin to hex , input (1101), output(D)
#test10 oct to hex , input (325), output(D5)
#test11 hex to oct , input (D5), output(325)
# Function to check if a given number is valid or not
def is_valid_number(num, base):
    valid_chars = "0123456789ABCDEF"
    if base == 'B':
        valid_chars = "01"
    elif base == 'O':
        valid_chars = "01234567"
    elif base == 'H':
        valid_chars = "0123456789ABCDEF"

    return all(char.upper() in valid_chars for char in num)

# Function to validate user input for a specific base
def validate_input(number, base):
    if not is_valid_number(number, base):
        print(f"Error: {number} is not a valid number in base {base}. Please insert a valid number.")
        return False
    return True

# Conversion functions
# dec to bin
def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary if binary else "0"
# dec to oct
def decimal_to_octal(num):
    octal = ""
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8
    return octal if octal else "0"
# dec to hex
def decimal_to_hexadecimal(num):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        hexadecimal = hex_chars[num % 16] + hexadecimal
        num //= 16
    return hexadecimal if hexadecimal else "0"
#bin to dec
def binary_to_decimal(num):
    decimal = 0
    power = 0
    for digit in reversed(num):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal
#oct to dec
def octal_to_decimal(num):
    decimal = 0
    power = 0
    for digit in reversed(num):
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal
#hex to dec
def hexadecimal_to_decimal(num):
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    power = 0
    for digit in reversed(num):
        decimal += hex_chars.index(digit.upper()) * (16 ** power)
        power += 1
    return decimal

# Main function for the numbering system converter
def number_converter():
    while True:
        print("** numbering system converter **")
        print("A) Insert a new number")
        print("B) Exit program")

        # User choice for inserting a new number or exiting
        choice_menu_1 = input("Please select your choice (A/B): ").upper()

        if choice_menu_1 == 'A':
            # Get user input for the number
            number = input("Please insert a number: ")

            print("** Please select the base you want to convert a number from **")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")

            # User choice for the source base
            choice_menu_2 = input("Please select your choice (A/B/C/D): ").upper()

            if choice_menu_2 in ['A', 'B', 'C', 'D']:
                # Validate the entered number for the source base
                if not validate_input(number, choice_menu_2):
                    continue

                print("** Please select the base you want to convert a number to **")
                print("A) Decimal")
                print("B) Binary")
                print("C) Octal")
                print("D) Hexadecimal")

                # User choice for the target base
                choice_menu_3 = input("Please select your choice (A/B/C/D): ").upper()

                if choice_menu_3 in ['A', 'B', 'C', 'D']:
                    # Convert the number based on user choices
                    if choice_menu_2 == 'A':
                        num_decimal = int(number)
                    elif choice_menu_2 == 'B':
                        num_decimal = binary_to_decimal(number)
                    elif choice_menu_2 == 'C':
                        num_decimal = octal_to_decimal(number)
                    else:
                        num_decimal = hexadecimal_to_decimal(number)

                    if choice_menu_3 == 'A':
                        result = num_decimal
                    elif choice_menu_3 == 'B':
                        result = decimal_to_binary(num_decimal)
                    elif choice_menu_3 == 'C':
                        result = decimal_to_octal(num_decimal)
                    else:
                        result = decimal_to_hexadecimal(num_decimal)

                    # Display the result to the user
                    print("Result:", result)

                else:
                    print("Please select a valid choice.")

            else:
                print("Please select a valid choice.")

        elif choice_menu_1 == 'B':
            print("Exiting program.")
            break

        else:
            print("Please select a valid choice.")

# Run the numbering system converter
number_converter()
