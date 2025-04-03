def open_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            print("File contents:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    open_file()