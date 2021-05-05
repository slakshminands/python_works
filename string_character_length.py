#function to find the characters in a string including spaces
def character_length(enter):
    inp_string = input(enter)
    count = 0
    for i in inp_string:
        count = count + 1
    print(count)

character_length("Enter a string: ")
    