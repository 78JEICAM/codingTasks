# Function to read data from the DOB.txt file and return lists of names and birthdates
def read_dob_file(file_path):
    names = []  # Initialize an empty list to store names
    birthdates = []  # Initialize an empty list to store birthdates
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:  # Iterate over each line in the file
            # Split the line by comma and unpack the values into name and birthdate
            splitted_text = line.strip().split(' ', 2)
            names.append(splitted_text[0] + ' ' + splitted_text[1])  # Add the name to the names list
            birthdates.append(splitted_text[2])
    return names, birthdates # Return the lists of names and birthdates
 
# Function to print the names and birthdates obtained from the file
def print_dob_data(names, birthdates):
    print("Name")  # Print a header for names
    for name in names:  # Iterate over each name in the names list
        print(name)  # Print the name
    print("\nBirthdate")  # Print a header for birthdates
    for birthdate in birthdates:  # Iterate over each birthdate in the birthdates list
        print(birthdate)  # Print the birthdate
 
# Main program
if __name__ == "__main__":
    file_path = "DOB.txt"  # Set the file path to "DOB.txt"
    names, birthdates = read_dob_file(file_path)  # Call the read_dob_file function to read data from the file
    print_dob_data(names, birthdates)  # Call the print_dob_data function to print the data
    # end data 