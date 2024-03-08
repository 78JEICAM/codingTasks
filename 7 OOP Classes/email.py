# Define the Email class
class Email:
    # Constructor to initialize email attributes
    def __init__(self, email_address, subject_line, email_content):
        # Initialize email attributes
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Default value for has_been_read attribute

    # Method to mark email as read
    def mark_as_read(self):
        # Set has_been_read attribute to True
        self.has_been_read = True

# Define the EmailSimulator class
class EmailSimulator:
    # Constructor to initialize the inbox as an empty list
    def __init__(self):
        # Initialize inbox as an empty list
        self.inbox = []

    # Method to populate inbox with sample emails
    def populate_inbox(self):
        # Sample emails data
        sample_emails = [
            {"email_address": "sender1@example.com", "subject_line": "Welcome to HyperionDev!", "email_content": "Welcome to our platform."},
            {"email_address": "sender2@example.com", "subject_line": "Great work on the bootcamp!", "email_content": "Keep up the good work!"},
            {"email_address": "sender3@example.com", "subject_line": "Your excellent marks!", "email_content": "Congratulations on your achievements."}
        ]
        # Loop through sample emails and create Email objects
        for email_data in sample_emails:
            # Create an Email object with email data
            email = Email(email_data["email_address"], email_data["subject_line"], email_data["email_content"])
            # Add the created Email object to inbox list
            self.inbox.append(email)

    # Method to list emails in the inbox
    def list_emails(self):
        # Print inbox header
        print("Inbox:")
        # Loop through inbox and print subject lines with indexes
        for index, email in enumerate(self.inbox):
            # Print email subject line with corresponding index
            print(f"{index} {email.subject_line}")

    # Method to read an email and mark it as read
    def read_email(self, index):
        # Check if the given index is within the range of inbox
        if 0 <= index < len(self.inbox):
            # Get the email object at the given index
            email = self.inbox[index]
            # Print email details
            print(f"\nEmail from {email.email_address} with subject '{email.subject_line}':\n")
            print(email.email_content)
            # Mark the email as read
            email.mark_as_read()
            # Print confirmation message
            print(f"\nEmail marked as read.\n")
        else:
            # Print error message for invalid index
            print("\nInvalid index.\n")

# Main function to run the program
def main():
    # Create an instance of EmailSimulator
    email_simulator = EmailSimulator()
    # Populate the inbox with sample emails
    email_simulator.populate_inbox()

    # Main program loop
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Execute corresponding actions based on user's choice
        if choice == '1':
            # List emails in inbox
            email_simulator.list_emails()
            # Get index of the email to read from user
            index = int(input("Enter the index of the email you want to read: "))
            # Read the email at given index
            email_simulator.read_email(index)
        elif choice == '2':
            # Get unread emails from inbox
            unread_emails = [email for email in email_simulator.inbox if not email.has_been_read]
            # Print subject lines of unread emails
            print("\nUnread emails:")
            for email in unread_emails:
                print(email.subject_line)
        elif choice == '3':
            # Quit the application
            print("Quitting application...")
            break
        else:
            # Print error message for invalid choice
            print("Invalid choice. Please enter a valid option.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
