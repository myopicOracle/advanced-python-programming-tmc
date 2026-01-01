# Write your solution here:

# """PART 1"""

class Item: 
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


# """PART 2"""

# class Suitcase:
#     def __init__(self, max_weight: int):
#         self.__max_weight = max_weight
#         self.__contents = []

#     def total_weight(self):
#         total_weight = 0
#         for item in self.__contents:
#             total_weight += item.weight()
#         return total_weight

#     def add_item(self, item: Item):
#         if item.weight() + self.total_weight() <= self.__max_weight:
#             self.__contents.append(item)
#         # else:
#         #     raise ValueError("Suitcase max weight has been reached. Cannot add.")

#     def __str__(self):
#         return f"{len(self.__contents)} items ({self.total_weight()} kg)"


# """PART 3""" """PART 4""" """PART 5"""

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__contents = []

    def weight(self):
        weight = 0
        for item in self.__contents:
            weight += item.weight()
        return weight

    def add_item(self, item: Item):
        if item.weight() + self.weight() <= self.__max_weight:
            self.__contents.append(item)

    def heaviest_item(self):
        if self.__contents:
            current_highest = 0
            for item in self.__contents:
                if item.weight() > current_highest:
                    current_highest = item.weight()
                    item_ref = item
            return item_ref
        else:
            return None

    def print_items(self):
        for item in self.__contents:
            print(f"{item.name()} ({item.weight()} kg)")

    def __str__(self):
        items_string = "item" if len(self.__contents) == 1 else "items"
        return f"{len(self.__contents)} {items_string} ({self.weight()} kg)"


# """PART 6""" """PART 7"""

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__contents = []

    def weight(self):
        weight = 0
        for item in self.__contents:
            weight += item.weight()
        return weight

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() < self.__max_weight:
            self.__contents.append(suitcase)

    def print_items(self):
        for suitcase in self.__contents:
            suitcase.print_items()

    def __str__(self):
        plural_string = "suitcase" if len(self.__contents) == 1 else "suitcases"
        return f"{len(self.__contents)} {plural_string}, space for {self.__max_weight - self.weight()} kg"



# """PART 1"""

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)

# print("Name of the book:", book.name())
# print("Weight of the book:", book.weight())

# print("Book:", book)
# print("Phone:", phone)


# """PART 2"""

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# suitcase = Suitcase(5)
# print(suitcase)

# suitcase.add_item(book)
# print(suitcase)

# suitcase.add_item(phone)
# print(suitcase)

# suitcase.add_item(brick)
# print(suitcase)


# """PART 3""" """PART 4""" """PART 5"""

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# suitcase = Suitcase(10)
# suitcase.add_item(book)
# suitcase.add_item(phone)
# suitcase.add_item(brick)

# print("The suitcase contains the following items:")
# suitcase.print_items()
# combined_weight = suitcase.weight()
# print(f"Combined weight: {combined_weight} kg")

# heaviest = suitcase.heaviest_item()
# print(f"The heaviest item: {heaviest}")


# """PART 6"""

# cargo_hold = CargoHold(1000)
# print(cargo_hold)

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold.add_suitcase(adas_suitcase)
# print(cargo_hold)

# cargo_hold.add_suitcase(peters_suitcase)
# print(cargo_hold)


# """PART 7"""

# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold = CargoHold(1000)
# cargo_hold.add_suitcase(adas_suitcase)
# cargo_hold.add_suitcase(peters_suitcase)

# print("The suitcases in the cargo hold contain the following items:")
# cargo_hold.print_items()
