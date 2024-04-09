def preprocess_list(filename):
    try:
        data = []
        with open(filename, 'r') as file:
            for index, line in enumerate(file, start=1):
                # Remove leading and trailing whitespace, and store the line in the list
                data.append((index, line.strip()))
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def overwrite_file(filename, processed_data):
    try:
        with open(filename, 'w') as file:
            for index, line in processed_data:
                file.write(f"{index}: {line}\n")  # Write line number and line to the file
        print(f"File '{filename}' overwritten successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    filename = "surnames.txt"  # Replace "female_names.txt" with the path to your input file
    processed_data = preprocess_list(filename)
    if processed_data:
        overwrite_file(filename, processed_data)

if __name__ == "__main__":
    main()
