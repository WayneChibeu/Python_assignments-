def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Example modification: Add line numbers
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"Successfully modified '{input_filename}' and saved as '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    modify_file("input.txt", "output.txt")
