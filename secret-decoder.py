letters = ['abscdefghijklmnopqrstuvwxyz']

secret = [1, 0, 3] # "bad"

# give your functions "verb" names
def decode(number_list, master_list):
    # configuation came in as arguments
    result = ''
    count = 0

    # do the translation
    # for esch item in number_list...
    for item in number_list:

    # find that index in master_list...
        letter = master_list[item]
    
    # put that character in result
    #result = result + letter
    result += letter

    #return the result
    return result

    decoded_message = decode(secret, letters)
    print(decoded_message)