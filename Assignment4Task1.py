def read_and_display_file(filename="sample.txt"):
    print("Reading file content:")
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line.strip()}")
                line_number += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
read_and_display_file()
