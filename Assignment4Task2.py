initial_content = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(initial_content + "\n")
print("Data successfully written to output.txt.")
additional_content = input("Enter additional text to append: ")


with open("output.txt", "a") as file:
    file.write(additional_content + "\n")
print("Data successfully appended.")
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    final_content = file.read()
    print(final_content)