#function to split input string based on commas
def receive_input(message):
    inp_list = input(message)
    splitted_list = inp_list.split(',')
    return splitted_list

    