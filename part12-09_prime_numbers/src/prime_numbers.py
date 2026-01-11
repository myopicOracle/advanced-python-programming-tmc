# Write your solution here

def prime_numbers():
    counter = 2
    while True: 
        if check_prime(counter):
            yield counter
        counter += 1


def check_prime(target: int):
    condition = True
    for counter in range(2, target):
        if target % counter == 0 and counter != target:
            return False 
    return condition


if __name__ == "__main__":

    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))