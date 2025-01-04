def file_line_navigator():
    filename = input("Enter the filename: ")
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        while True:
            print(f"Number of lines in the file: {len(lines)}")
            line_number = int(input("Enter a line number (0 to quit): "))
            
            if line_number == 0:
                break
            elif 1 <= line_number <= len(lines):
                print(lines[line_number - 1].strip())
            else:
                print("Invalid line number. Please try again.")
    
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

file_line_navigator()
