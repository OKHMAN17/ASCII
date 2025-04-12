# ASCII Code Converter in Multiple Bases

## Overview

This project provides a simple command-line tool written in Python to convert the ASCII codes of characters in a given name into different numeral systems (or "bases"). The program allows the user to enter a name and display the ASCII values of each character in the name in the following bases:

- **Base 2 (Binary)**
- **Base 8 (Octal)**
- **Base 10 (Decimal)**
- **Base 16 (Hexadecimal)**

The goal of this project is to help users understand how text is represented in different numeral systems and how data can be encoded and decoded using different bases.

## Features

- **Base 2 (Binary)**: Displays the binary (base-2) representation of the ASCII values of characters in the input name.
- **Base 8 (Octal)**: Converts and displays the ASCII values in the octal (base-8) numeral system.
- **Base 10 (Decimal)**: Displays the ASCII values in the standard decimal (base-10) format.
- **Base 16 (Hexadecimal)**: Converts and displays the ASCII values in the hexadecimal (base-16) numeral system.

Users can choose one of the four numeral systems (binary, octal, decimal, hexadecimal) to display the ASCII codes of each character in the entered name.

## How to Use

### Running the Program:

1. **Run the Python script** from the command line:
   ```bash
   python word_to_ascii.py
   ```
2. **Select an option from the menu** to convert ASCII codes to one of the following bases:
   - Option 1: Display ASCII codes in **Base 2 (Binary)**
   - Option 2: Display ASCII codes in **Base 8 (Octal)**
   - Option 3: Display ASCII codes in **Base 10 (Decimal)**
   - Option 4: Display ASCII codes in **Base 16 (Hexadecimal)**
   - Option 5: Exit the program.
3. After selecting the desired option, **enter a name** when prompted. The program will then display the ASCII codes of each character in the name in the chosen base.

### Example:

- If you enter the name "Alice" and choose **Base 2 (Binary)**, the output will look like this:

```
ASCII codes of the name 'Alice' in base 2:
A: 1000001
l: 1101100
i: 1101001
c: 1100011
e: 1100101
```

- If you choose **Base 16 (Hexadecimal)**, the output will be:

```
ASCII codes of the name 'Alice' in base 16:
A: 41
l: 6C
i: 69
c: 63
e: 65
```

## Features in Detail

1. **Base 2 (Binary)**:
   - This option converts each character in the input name to its ASCII value and then displays that value in **binary** form.
   - Example:
     - 'A' → 1000001
     - 'l' → 1101100

2. **Base 8 (Octal)**:
   - This option converts the ASCII value of each character to **octal** format.
   - Example:
     - 'A' → 101
     - 'l' → 154

3. **Base 10 (Decimal)**:
   - This option displays the **decimal** ASCII value of each character.
   - Example:
     - 'A' → 65
     - 'l' → 108

4. **Base 16 (Hexadecimal)**:
   - This option converts the ASCII value of each character to **hexadecimal** format.
   - Example:
     - 'A' → 41
     - 'l' → 6C

## Requirements

- **Python 3.x**: The program is written in Python and requires Python 3 or higher to run. You can download Python from [python.org](https://www.python.org/).

No additional libraries or dependencies are required.

## Installation

To run this project, follow these steps:

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/word_to_ascii.git
   ```

2. **Navigate to the project folder**:
   ```bash
   cd word_to_ascii
   ```

3. **Run the program**:
   ```bash
   python word_to_ascii.py
   ```

4. **Follow the on-screen instructions** to convert ASCII codes to the desired base.

## License

This project is open-source and available under the MIT License. You can freely modify, use, and distribute the code.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Any contributions to improve the program are welcome!

---

### Additional Notes

- **How ASCII Works**: ASCII (American Standard Code for Information Interchange) represents characters as numeric codes. The most common codes include values like 65 for 'A', 66 for 'B', and so on. ASCII codes are used in various systems and can be represented in different bases, such as binary, octal, decimal, and hexadecimal.
  
- **Why Convert Between Bases**: Understanding how to convert between numeral systems is an essential skill in computer science and programming. It allows for easier representation of data in different formats, as different systems use different bases to store and manipulate data efficiently.
```
