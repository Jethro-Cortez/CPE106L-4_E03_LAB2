def LR2_2():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
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
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

LR2_2()
