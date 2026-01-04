# WRITE YOUR SOLUTION HERE:

class SimpleDate: 
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __gt__(self, another: "SimpleDate"):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day > another.day:
            return True
        else: 
            return False

    def __lt__(self, another: "SimpleDate"):
        if self.year < another.year:
            return True
        elif self.year == another.year and self.month < another.month:
            return True
        elif self.year == another.year and self.month == another.month and self.day < another.day:
            return True
        else: 
            return False

    def __eq__(self, another: "SimpleDate"):
        return (self.day, self.month, self.year) == (another.day, another.month, another.year)

    def __ne__(self, another: "SimpleDate"):
        return (self.day, self.month, self.year) != (another.day, another.month, another.year)

    def __add__(self, new_days: int):
        total = self.year * 360 + (self.month - 1) * 30 + (self.day - 1)
        total += new_days

        year = total // 360
        remaining = total % 360

        month = remaining // 30 + 1
        day = remaining % 30 + 1

        return SimpleDate(day, month, year)

    def __sub__(self, another: "SimpleDate"):
        total_1 = self.year * 360 + (self.month - 1) * 30 + (self.day - 1)
        total_2 = another.year * 360 + (another.month - 1) * 30 + (another.day - 1)
        diff = abs(total_1 - total_2)

        return diff


# # Part 1
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)
# d3 = SimpleDate(28, 12, 1985)

# print(d1)
# print(d2)
# print(d1 == d2)
# print(d1 != d2)
# print(d1 == d3)
# print(d1 < d2)
# print(d1 > d2)

# # Part 2
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(28, 12, 1985)

# d3 = d1 + 3
# d4 = d2 + 400

# print(d1)
# print(d2)
# print(d3)
# print(d4)

# # Part 3
# d1 = SimpleDate(4, 10, 2020)
# d2 = SimpleDate(2, 11, 2020)
# d3 = SimpleDate(28, 12, 1985)

# print(d2-d1)
# print(d1-d2)
# print(d1-d3)
