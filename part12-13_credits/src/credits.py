from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution


def sum_of_all_credits(attempts: list) -> int: 
    return reduce(lambda first, next : first + next.credits, attempts, 0)


def filter_passed(attempts: list) -> list:
    return list(filter(lambda x : x.grade > 0, attempts))


def sum_of_passed_credits(attempts: list) -> int:
    return reduce(lambda total, item : total + item.credits, filter(lambda x : x.grade > 0, attempts), 0)


def average(attempts: list):
    passed_attempts = filter_passed(attempts)
    # print("passed_attempts:", passed_attempts) # debug
    sum_of = reduce(lambda total, item : total + item.grade, passed_attempts, 0)
    # print("sum_of:", sum_of) # debug
    number_of = len(list(passed_attempts))
    # print("number_of:", number_of) # debug
    return sum_of / number_of

    
if __name__ == "__main__":

    # Part 1
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    # Part 2
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    # Part 3
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)