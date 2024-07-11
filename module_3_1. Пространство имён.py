# calls = 0
#
# def cout_call():
#     global calls
#     return calls

# def string_info(string =""):
#     return (len(string), string.upper(), string.lower())


# def is_contains(string="", list_to_search=[]):
#     if string == "".lower() and list_to_search[] == ''.lower()
#         print(True)
#     else:
#         print(False)
#
# is_contains("Urban", ['ban', 'BaNaN', 'urBAN'])

calls = 0


def count_calls():
    print(calls)


def string_info(string=""):
    global calls
    calls += 1
    return (len(string), string.upper(), string.lower())


def is_contains(string='', list_to_search=[]):
    global calls
    calls += 1
    if string.lower() == 'Urban'.lower():
        for i in list_to_search:
            if str(i).lower() == "URBAN".lower():
                return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




