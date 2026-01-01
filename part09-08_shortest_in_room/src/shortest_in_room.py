# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.occupants = []

    def add(self, person: Person):
        self.occupants.append(person)

    def is_empty(self):
        return not self.occupants

    def shortest(self):
        shortest = 500
        if self.occupants: 
            for person in self.occupants:
                if person.height < shortest:
                    shortest = person.height
                    shortest_person = person
            return shortest_person
        return None

    def remove_shortest(self):
        shortest = 500
        if self.occupants: 
            for index, person in enumerate(self.occupants):
                if person.height < shortest:
                    shortest = person.height
                    shortest_index = index
            removed = self.occupants.pop(shortest_index)
            return removed
        return None

    def print_contents(self):
        for person in self.occupants:
            print(person)


# TESTING

# room = Room()

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# room.add(Person("Lea", 183))
# room.add(Person("Kenya", 172))
# room.add(Person("Nina", 162))
# room.add(Person("Ally", 166))

# print("Is the room empty?", room.is_empty())
# print("Shortest:", room.shortest())

# room.print_contents()

# print()

# removed = room.remove_shortest()
# print(f"Removed from room: {removed.name}")

# print()

# room.print_contents()
