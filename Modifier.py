def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content has been successfully modified and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print(f"Error: There was an issue reading the file {input_filename} or writing to {output_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_filename_from_user():
    filename = input("Enter the filename to read from: ")
    return filename

def main():
    input_filename = get_filename_from_user()
    output_filename = "modified_" + input_filename  # New filename with "modified_" prefix
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
