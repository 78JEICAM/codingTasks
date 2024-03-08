# Display user's imput as a sentence and convert to variable

str_manip = input("Enter the sentence: ")

# Find the length of the input sentence

sentence_lengh = len(str_manip)

# Displays length of the sentence

print("\nSentence length: ", sentence_lengh)
 
# Display the last character

print("\nLast character: ", str_manip[sentence_lengh -1])
 
# Replaces all occurrences of that letter with the'@''

print("\nAfter replacing ocuurances of that letter to @: ", str_manip.replace(str_manip[sentence_lengh -1],"@"))
 
# The variable last stores the last three characters from backward 

last_three_characters = str_manip[::-1][0:3]

print("\nLast three characters in backward: ", last_three_characters)

# The variable five-characters stores first three characters and last two characters

five_characters = str_manip[:3]+str_manip[sentence_lengh-2]+str_manip[sentence_lengh-1]

print("\nFive characters word after modification: ", five_characters)