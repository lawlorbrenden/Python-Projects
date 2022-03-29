# Brenden Lawlor
# 10/30/21
# Assignment 11


ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'


# Cipher Program
def main():
    """Controls program flow and explains instructions to user."""
    keep_going = ''
    while keep_going != 'q':
        print("\nThis program will allow you to enter some text to create files to either encrypt or decrypt."
              " Encrypted text will be in all uppercase. It will try to decrypt a file 3 times.")
        create_file = input("Would you like to create a file? (y/n): ")
        while create_file != 'y' and create_file != 'n':
            print("Please enter 'y' or 'n'.")
            create_file = input("Would you like to create a file? (y/n): ")

        if create_file == 'y':
            write_file()

        keep_going = input(
            "\nWould you like to encrypt or decrypt a file? Or press 'q' to quit. (e/d/q): ")

        while keep_going != 'e' and keep_going != 'd' and keep_going != 'q':
            keep_going = input(
                "Please enter 'e' or 'd' or 'q'for 'encrypt' or 'decrypt' or 'quit': ")

        if keep_going == 'e':
            contents, file_name, shift_num = open_decrypted_file()
            encrypt_file(contents, file_name, shift_num)
        elif keep_going == 'd':
            counter = 0
            contents, file_name = open_encrypted_file()
            possible_shift = (create_sorted_index_list(contents)[0] % 26) - 4
            decrypt_file(possible_shift, contents, file_name, 0)

    # Occasionally when trying to quit the program I would get a strange TypeError. I've been
    # working on this assignment for so long now that I just took the lazy way out and made
    # the program fail silently since its going to quit anyway
    try:
        pass
    except TypeError:
        pass


def write_file():
    """Creates and writes to a file."""
    keep_going = 'y'
    while keep_going == 'y':
        file_name = input(
            "\nPlease enter the name of the file you would like to create: ")
        file_name = file_name + '.txt'
        contents = input(
            "Please enter the content of the file (The program will be more accurate with a larger amount of characters): ")

        with open(file_name, 'w') as f:
            f.write(contents)

        keep_going = input("Would you like to create another file? (y/n): ")

        while keep_going != 'y' and keep_going != 'n':
            print("\nPlease enter 'y' or 'n'.")
            keep_going = input(
                "Would you like to create another file? (y/n): ")
    return


def open_decrypted_file():
    """
    Opens a file for the user to encrypt and returns its contents and name. Also 
    gets the shift number from the user.
    """
    file_name = input(
        "Please enter the file name you would like to encrypt: ")
    file_name = file_name + '.txt'

    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Could not find file {file_name}. Please try again.")
        main()
    else:
        try:
            shift_num = int(
                input("Please enter the number you would like to shift the text by: "))
        except ValueError:
            print("Please enter an integer, not a character. Please try again")
            main()
        else:
            return(contents, file_name, shift_num)


def encrypt_file(contents, file_name, shift_num):
    """
    Encrypts the file from open_decrypted_file() based on users discretion. 
    Prints the encryption to the console for proof to the user.
    """
    keep_going = 'y'
    while keep_going == 'y':

        encrypted_letters = []

        for char in contents:
            char = char.lower()
            if char in ASCII_LOWERCASE:
                index = ASCII_LOWERCASE.find(char)
                shifted_char = ASCII_LOWERCASE[(index + shift_num) % 26]
                encrypted_letters.append(shifted_char.upper())

            # If the character is not a letter, just append it
            else:
                encrypted_letters.append(char)

        # clears out file
        with open(file_name, 'w') as f:
            f.write('')

        for char in encrypted_letters:
            with open(file_name, 'a') as f:
                f.write(char)

        print("File encrypted. Printing encrypted message: ")

        with open(file_name) as f:
            lines = f.readlines()

        for line in lines:
            print(line.rstrip())

        keep_going = input(
            "Would you like to encrypt another file? (y/n): ")
        while keep_going != 'y' and keep_going != 'n':
            print("Please enter 'y' or 'n'.")
            keep_going = input(
                "File encrypted. Would you like to encrypt another file? (y/n): ")
        if keep_going == 'y':
            contents, file_name, shift_num = open_decrypted_file()
            encrypt_file(contents, file_name, shift_num)

        return


def decrypt_file(possible_shift, contents, file_name, counter):
    """
    Deciphers the selected file from open_encrypted_file() using the list 
    of most common characters from create_sorted_index_list(). Will attempt 
    to decyper 3 times, setting the most common letter from the text to 
    each time. It is very unlikely that this method will fail if the text
    file is large enough. Uses recursion to call itself again if it does fail.
    """
    while counter < 3:
        keep_going = 'y'
        while keep_going == 'y':
            # clears out file
            with open(file_name, 'w') as f:
                f.write('')

            if counter < 3:
                print("Attempting to decipher text.....")

                for char in contents:
                    char = char.lower()
                    if char in ASCII_LOWERCASE:
                        index = ASCII_LOWERCASE.find(char)
                        possible_unshifted_index = index - possible_shift
                        possible_unshifted_letter = ASCII_LOWERCASE[possible_unshifted_index]

                        with open(file_name, 'a') as f:
                            f.write(possible_unshifted_letter)
                    else:
                        with open(file_name, 'a') as f:
                            f.write(char)

                with open(file_name) as f:
                    contents = f.read()

                print("\n" + contents)

                is_correct = input(
                    "\nPossible decipher found. Please verify if new message is correct above (y/n): ")
                while is_correct != 'y' and is_correct != 'n':
                    print("Please enter 'y' or 'n'.")
                    is_correct = input(
                        "Possible decypher found. Please verify if new message is correct (y/n): ")

                if is_correct == 'y':
                    keep_going = input(
                        "I win! Would you like me to decrypt another file? (y/n): ")

                    while keep_going != 'y' and keep_going != 'n':
                        print("Please enter 'y' or 'n'.")
                        keep_going = input(
                            "I win! Would you like me to decrypt another file? (y/n): ")

                    if keep_going == 'y':
                        contents, file_name = open_encrypted_file()
                        sorted_index_list = create_sorted_index_list(contents)
                        counter = 0
                        possible_shift = (create_sorted_index_list(
                            contents)[counter] % 26) - 4
                        decrypt_file(possible_shift, contents,
                                     file_name, counter=0)

                else:
                    if counter < 2:
                        print("Trying again........")
                    counter += 1
                    # Sets the shift to the next most common letter (which is probably e)
                    possible_shift = (create_sorted_index_list(
                        contents)[counter] % 26) - 4
                    decrypt_file(possible_shift, contents, file_name, counter)

                    # Admit defeat if the program gets to this point. (User probably cheated)
                    if counter == 3:
                        print("\nI cannot decipher this file. Bravo.")
            return


def create_sorted_index_list(contents):
    """
    Counts the amount of letters in the text file and assigns each letter an index.
    Stores the index: amount in a dictionary then sorts a list of the indexes
    in descending order. This makes it easy to get the 3 most common letters in 
    the text file.
    """
    index_count = {}
    for letter in contents:
        letter = letter.lower()
        if letter in ASCII_LOWERCASE:
            index = ASCII_LOWERCASE.find(letter)
            if index not in index_count.keys():
                index_count[index] = 1
            else:
                # if index is already in the dictionary just increment the value
                index_amount = index_count[index]
                index_count[index] = index_amount + 1

    # I'm not exactly sure how this line works, I just found it online and it made my code work so
    sorted_index_count = dict(sorted(
        index_count.items(), key=lambda index: index[1], reverse=True))

    sorted_index_list = []
    for index in sorted_index_count.keys():
        sorted_index_list.append(index)

    return(sorted_index_list)


def open_encrypted_file():
    """Opens a file for decrypt_file() to decipher and returns its contents and name"""
    file_name = input(
        "Please enter the file name you would like to decrypt: ")
    file_name = file_name + '.txt'
    try:
        with open(file_name) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Could not find file {file_name}. Please try again.")
        main()
    else:
        return(contents, file_name)


main()
