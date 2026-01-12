class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here


def names_of_students(attempts: list) -> list: 
    new_map = map(lambda x : x.student_name, attempts)
    new_list = list(new_map)
    return new_list


def course_names(attempts: list) -> list: 
    new_map = map(lambda x : x.course_name, attempts)
    new_list = list(new_map)
    unique = set(new_list)
    alphabetized = sorted(unique)
    return list(alphabetized)


if __name__ == "__main__":

    # Part 1
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    # Part 2
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)