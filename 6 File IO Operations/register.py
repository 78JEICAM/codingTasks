# Function to register students for an exam venue
def register_students(num_students):
    # Open a file named "reg_form.txt" in write mode
    with open("reg_form.txt", "a") as file:
        # For each student in the range from 1 to num_students
        for i in range(num_students):
            # Prompt the user to enter the ID for the current student
            student_id = input(f"Enter ID for student {i+1}: ")
            # Write the student ID to the file
            file.write(f"{student_id}\n")
            # Write a dotted line to the file as a separator between IDs
            file.write('.' * 20 + '\n')

# If the script is run as the main program
if __name__ == "__main__":
        # Ask the user to enter the number of students registering
        num_students = int(input("How many students are registering? "))
        # Register students
        register_students(num_students)
        # Inform user about completion of registration
        print("Registration completed. Check reg_form.txt for the registration form.")
 
   