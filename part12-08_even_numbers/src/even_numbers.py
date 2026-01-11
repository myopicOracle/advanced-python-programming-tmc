# Write your solution here

def even_numbers(beginning: int, maximum: int) -> int: 
    counter = beginning
    while counter <= maximum: 
        if counter % 2 == 0: 
            yield counter
        counter += 1


if __name__ == "__main__":

    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)