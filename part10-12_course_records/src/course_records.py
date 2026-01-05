# tee ratkaisusi tänne

class Transcript:
    def __init__(self):
        self.__transcript = {}

    def __str__(self):
        num_of_courses, total_credits, mean, grades = self.__calculate_stats()

        string = ""
        string += f"{num_of_courses} completed courses, a total of {total_credits} credits\n"
        string += f"mean {mean:.1f}\n"
        string += f"grade distribution\n"
        string += f"5: {grades.count(5) * 'x'}\n"
        string += f"4: {grades.count(4) * 'x'}\n"
        string += f"3: {grades.count(3) * 'x'}\n"
        string += f"2: {grades.count(2) * 'x'}\n"
        string += f"1: {grades.count(1) * 'x'}"

        return string

    @property
    def transcript(self):
        return self.__transcript

    def add_course(self, name: str, grade: str, credits: str):
        course = self.__transcript.get(name)
        if course: 
            course.grade = grade
        else: 
            course = Course(name, grade, credits)
            self.__transcript[name] = course

    def get_course(self, name: str):
        course = self.__transcript.get(name)
        if course: 
            return course
        else:
            return "no entry for this course"

    def __calculate_stats(self):
        grades = []
        credits = []

        for course in self.transcript.values():
            grades.append(int(course.grade))
            credits.append(int(course.credits))

        num_of_courses = len(self.transcript)
        total_credits = sum(credits)
        mean = sum(grades) / num_of_courses

        return num_of_courses, total_credits, mean, grades


class Course:
    def __init__(self, name: str, grade: str, credits: str):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def __str__(self):
        return f"{self.name} ({self.credits} cr) grade {self.grade}"

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade

    @property
    def credits(self):
        return self.__credits

    @grade.setter
    def grade(self, new_grade: str):
        if int(new_grade) > int(self.grade):
            self.__grade = new_grade


class ApplicationInterface:
    def __init__(self):
        self.transcript = Transcript()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        self.transcript.add_course(course, grade, credits)

    def get_course(self):
        course = input("course: ")
        print(self.transcript.get_course(course))

    def print_stats(self):
        print(self.transcript)

    def execute(self):
        self.help()
        print()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1: 
                self.add_course()
                print()
            elif command == 2: 
                self.get_course()
                print()
            elif command == 3: 
                self.print_stats()
                print()
            else:
                print("invalid command")
                self.help()
                print()


app = ApplicationInterface()
app.execute()
