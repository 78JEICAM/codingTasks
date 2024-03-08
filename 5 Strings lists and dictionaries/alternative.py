# Define the function to alternate characters
def alternate_characters(string):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character and its index in the string
    for index, character in enumerate(string):
        # Check if the index is even
        if index % 2 == 0:
            # Append the uppercased character to the result string
            result += character.upper()
        else:
            # Append the lowercased character to the result string
            result += character.lower()
    
    # Return the result string
    return result

# Define the function to alternate words
def alternate_words(string):
    # Split the string into words by space
    words = string.split()
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate through each word and its index in the list of words
    for index, word in enumerate(words):
        # Check if the index is even
        if index % 2 == 0:
            # Append the lowercased word to the result list
            result.append(word.lower())
        else:
            # Append the uppercased word to the result list
            result.append(word.upper())
    
    # Join the words in the result list with space
    # to form a single string
    return ' '.join(result)

# Main program
if __name__ == "__main__":
    # Get input string from the user
    input_string = input("Enter a string: ")
    
    # Call the alternate_characters function with the input string
    alternate_chars_result = alternate_characters(input_string)
    
    # Print the result of alternate_characters function
    print("Alternate characters:", alternate_chars_result)
    
    # Call the alternate_words function with the input string
    alternate_words_result = alternate_words(input_string)
    
    # Print the result of alternate_words function
    print("Alternate words:", alternate_words_result)

