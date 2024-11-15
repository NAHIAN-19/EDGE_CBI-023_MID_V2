# Function to remove duplicates characters
def remove_duplicates(duplicated_string):
    # store unique characters in another string
    unique_string = ""
    # iterate through the duplicated string
    for character in duplicated_string:
        # check if current character is present in new string
        if character not in unique_string:
            # add the character if not present in new string
            unique_string+=character
            
    # return unique string
    return unique_string

# base function for i/o
def home():
    # duplicated string input from user
    duplicated_string = input("Enter a string to remove duplicates : ")
    # call the function to remove duplicates
    unique_string = remove_duplicates(duplicated_string)
    # print both strings
    print(f'Before removing duplicates : ',duplicated_string)
    print(f'After removing duplicates : ',unique_string)
    
# call the base function when code is executed
home()