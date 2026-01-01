# WRITE YOUR SOLUTION HERE:

class ListHelper:
    def __init__(self, my_list: list):
        self.my_list = my_list

    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest_count = 0
        greatest_num = ''

        for unique in set(my_list):
            counter = 0

            for num in my_list:
                if num == unique:
                    counter += 1

            if counter > greatest_count:
                greatest_count = counter
                greatest_num = unique 

        return greatest_num

    @classmethod
    def doubles(cls, my_list: list):
        threshold = 1
        qualified_list = []

        for unique in set(my_list):
            counter = 0

            for num in my_list:
                if num == unique:
                    counter += 1

            if counter > threshold:
                qualified_list.append(unique)

        return len(qualified_list)


# numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
# print(ListHelper.greatest_frequency(numbers))
# print(ListHelper.doubles(numbers))
