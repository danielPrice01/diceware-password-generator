import secrets
secrets_generator = secrets.SystemRandom()

# num_words = int(input("How many words would you like in your password? \n"))
num_words = 5
list_words = open("list_words", "r")
content_list_words = list_words.readlines()


def rand_five_fig_number():
    # Makes a 5-figure random number

    random_num = 0

    for i in range(5):
        random_num += secrets_generator.randint(1, 6) * (10 ** i)

    return random_num


def num_of_words():
    # Adds the requested number of randomly generated numbers to numbered_password list

    number_pass = []

    for num in range(num_words):
        rand_five_fig_number()
        number_pass.append(rand_five_fig_number())

    return number_pass


numbered_password = num_of_words()


def find_and_add_lines():
    # Finds which line in "list_words" each randomly generated number appears in.
    # Adds the word from that line to worded list, removing whitespace and the random number corresponding to that word

    word_pass = []
    line_number = []

    for p in range(len(numbered_password)):
        number = numbered_password[p]
        for i in range(len(content_list_words)):
            if (str(number)) in content_list_words[i]:
                t = True
                line_number.append(i)
                if t:
                    word_pass.append((content_list_words[i].strip(str(number) + "\t" + "\n")))
    return word_pass


worded_password = ' '.join(find_and_add_lines())

print(f"Your numbered password is: \n{numbered_password}")
print(f"Your worded password is: \n{worded_password}")
