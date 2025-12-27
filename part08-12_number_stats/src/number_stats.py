# Write your solution here!

# Class Definition

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.sum 

    def average(self):
        if self.numbers > 0:
            return self.sum / self.numbers


# Main Program 

all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:

    user_input = int(input("Enter number; -1 to exit: "))

    if user_input == -1:
        break

    else:
        all_stats.add_number(user_input)

        if user_input % 2 == 0:
            even_stats.add_number(user_input)
        else:
            odd_stats.add_number(user_input)

print(f"Sum of numbers: {all_stats.get_sum()}")
print(f"Mean of numbers: {all_stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")
