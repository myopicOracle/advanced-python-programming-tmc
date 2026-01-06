# WRITE YOUR SOLUTION HERE:

def begin_with_vowel(words: list) -> list:
    return [word for word in words if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]


# word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
# for vowelled in begin_with_vowel(word_list):
#     print(vowelled)    