# WRITE YOUR SOLUTION HERE:

import string

def most_common_words(filename: str, lower_limit: int) -> dict: 
    temp_dict = {}

    with open(filename) as f: 
        text = f.read()
        cleaned_text = "".join([char for char in text if char not in string.punctuation])

        for word in cleaned_text.split():
            if word not in temp_dict:
                temp_dict[word] = 1
            else: 
                temp_dict[word] += 1

        filtered_dict = { key : value for key, value in temp_dict.items() if value >= lower_limit }
        return filtered_dict
