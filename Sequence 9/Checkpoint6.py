# Try to open and read a file that does not exist
try:
    # Open the file in read mode
    file = open("missing_data.txt", "r")

    # Read and print the file contents
    print(file.read())

    # Close the file
    file.close()

# Catch the error if the file is not found
except FileNotFoundError:
    print("Error: The file 'missing_data.txt' was not found. Please check the file name or location.")

# This block always executes whether an error occurs or not
finally:
    print("File cleanup processes finished.")