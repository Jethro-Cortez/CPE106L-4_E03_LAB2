import os.path

fileName = input("Enter the filename: ")

if os.path.exists(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    
    print(f"The file contains {len(lines)} lines.")

    while True:
        try:
            line_number = int(input(f"Enter a line number (1 to {len(lines)}) or 0 to quit: "))
            
            if line_number == 0:
                print("Exiting the program.")
                break
            elif 1 <= line_number <= len(lines):
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
else:
    print(f"The file {fileName} does not exist.")
