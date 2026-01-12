# Write your solution here
import re

def regex(pattern: str, string: str):
    return bool(re.search(pattern, string))

def is_dotw(my_string: str) -> bool: 
    pattern = "Mon.*|Tue.*|Wed.*|Thu.*|Fri.*|Sat.*|Sun.*"
    return regex(pattern, my_string)

def all_vowels(my_string: str) -> bool:
    pattern = "^[aeiou]+$"
    return regex(pattern, my_string)

def time_of_day(my_string: str) -> bool: 
    pattern = "^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
    return regex(pattern, my_string)


if __name__ == "__main__":

    # Part 1
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    # Part 2
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    # Part 3
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    