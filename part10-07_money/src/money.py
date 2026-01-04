# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    # @property
    # def euros(self):
    #     return self.__euros

    # @property
    # def cents(self):
    #     return self.__cents

    @staticmethod
    def _rainman(dollas: int, sense: int):
        return dollas + (sense / 100)

    @staticmethod
    def _reverse_rainman(amount: int):
        dollas = int(amount)
        # print(f"dollas: {dollas}") # debug
        sense = int(round((amount - dollas) * 100))
        # print(f"sense: {sense}") # debug
        return (dollas, sense)

    def __eq__(self, another: "Money"):
        return self.__euros == another.__euros and self.__cents == another.__cents

    def __gt__(self, another: "Money"):
        return self.__euros > another.__euros or self.__cents > another.__cents

    def __lt__(self, another: "Money"):
        return self.__euros < another.__euros or self.__cents < another.__cents

    def __ne__(self, another: "Money"):
        return self.__euros != another.__euros or self.__cents != another.__cents

    def __add__(self, another: "Money"):
        result = self._rainman(self.__euros, self.__cents) + self._rainman(another.__euros, another.__cents)
        # print(result) # debug
        if result < 0: 
            raise ValueError("a negative result is not allowed")
        else:
            euros, cents = self._reverse_rainman(result)
            new_instance = Money(euros, cents)
            return new_instance

    def __sub__(self, another: "Money"):
        result = self._rainman(self.__euros, self.__cents) - self._rainman(another.__euros, another.__cents)
        # print(result) # debug
        if result < 0: 
            raise ValueError("a negative result is not allowed")
        else:
            euros, cents = self._reverse_rainman(result)
            new_instance = Money(euros, cents)
            return new_instance


# e1 = Money(4, 10)
# e2 = Money(2, 5)
# e3 = Money(4, 10)

# # Part 1
# print(e1)
# print(e2)
# print(e3)

# # Part 2
# print(e1 == e2)
# print(e1 == e3)

# # Part 3
# print(e1 != e2)
# print(e1 < e2)
# print(e1 > e2)

# # Part 4
# e1 = Money(4, 5)
# e2 = Money(2, 95)

# e3 = e1 + e2
# e4 = e1 - e2

# print(e3)
# print(e4)

# e5 = e2-e1

# # Part 5

# print(e1)
# e1.__euros = 1000
# print(e1)
