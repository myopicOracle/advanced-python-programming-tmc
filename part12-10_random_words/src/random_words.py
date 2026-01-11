# Write your solution here:

import random as rand

# def word_generator(characters: str, length: int, amount: int):
#     selection = characters[:length]
#     counter = 0
#     while counter < amount:
#         yield "".join(rand.choices(selection, k=length))
#         counter += 1


def word_generator(characters: str, length: int, amount: int):
    return ("".join(rand.choices(characters[:length], k=length)) for _ in range(amount) )


if __name__ == "__main__":

    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)