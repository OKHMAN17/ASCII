def display_ascii_codes(name, base):
    # Function to display ASCII codes of the given name in the specified base.
    print(f"\nASCII codes of the name '{name}' in base {base}:")
    
    # Loop through each character in the name
    for char in name:
        ascii_value = ord(char)  # Get the ASCII value of the character
        
        # Display the ASCII value in the specified base
        if base == 2:
            print(f"{char}: {bin(ascii_value)[2:]}")  # Convert to binary (base 2)
        elif base == 8:
            print(f"{char}: {oct(ascii_value)[2:]}")  # Convert to octal (base 8)
        elif base == 10:
            print(f"{char}: {ascii_value}")  # Decimal (base 10)
        elif base == 16:
            print(f"{char}: {hex(ascii_value)[2:].upper()}")  # Convert to hexadecimal (base 16)

def main():
    # Main function to handle user interaction and menu options.
    while True:
        # Display the menu to the user
        print("\nMenu:")
        print("1. Enter a name and display ASCII codes in base 2 (binary)")
        print("2. Enter a name and display ASCII codes in base 8 (octal)")
        print("3. Enter a name and display ASCII codes in base 10 (decimal)")
        print("4. Enter a name and display ASCII codes in base 16 (hexadecimal)")
        print("5. Exit")

        # Ask the user to select an option
        choice = input("Please select an option (1-5): ")

        # Exit the program if the user selects option 5
        if choice == '5':
            print("Exiting the program.")
            break
        # If the user selects a valid option, process the name and show ASCII codes
        elif choice in ['1', '2', '3', '4']:
            name = input("Please enter your name: ")  # Ask the user to enter their name
            # Display ASCII codes based on the selected base
            if choice == '1':
                display_ascii_codes(name, 2)   # Base 2 (Binary)
            elif choice == '2':
                display_ascii_codes(name, 8)   # Base 8 (Octal)
            elif choice == '3':
                display_ascii_codes(name, 10)  # Base 10 (Decimal)
            elif choice == '4':
                display_ascii_codes(name, 16)  # Base 16 (Hexadecimal)
        else:
            # If the user enters an invalid option, show an error message
            print("Invalid option. Please try again.")

# Check if the script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
