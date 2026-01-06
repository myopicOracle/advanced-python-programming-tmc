
def balanced_brackets(string: str):
    my_string = ''.join([char for char in string if char in '()[]'])
    # print('cleaned string:', my_string) # debug

    if len(my_string) == 0:
        return True
    if not ((my_string[0] == '(' and my_string[-1] == ')') or (my_string[0] == '[' and my_string[-1] == ']')):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


# ok = balanced_brackets("([([])])")
# print(ok)

# ok = balanced_brackets("(python version [3.7]) please use this one!")
# print(ok)

# ok = balanced_brackets("(()]")
# print(ok)

# ok = balanced_brackets("([bad egg)]")
# print(ok)