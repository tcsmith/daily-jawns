from dataclasses import dataclass

@dataclass
class Student:
    first_name: str
    last_name: str
    gpa: float
    grade_level: int

def print_students(students: list[Student]) -> None:
    for s in students:
        print(s)

def main() -> None:
    students = [
        Student("todd", "smith", 3.7, 12),
        Student("erin", "keltz", 4.0, 12),
        Student("nutty", "mcnutterson", 1.8, 6),
        Student("noodles", "keltz", 2.0, 8),
    ]

    print("Unsorted")
    print_students(students)

    print("\nSorted by GPA")
    by_gpa = students[:]
    by_gpa.sort(key=lambda s: (s.gpa), reverse=True)
    print_students(by_gpa)

    print("\nSorted By Grade Level")
    by_grade_level = students[:]
    by_grade_level.sort(key=lambda s: (s.grade_level), reverse=True)
    print_students(by_grade_level)

    print("\nSorted By Last Name")
    by_last_name = students[:]
    by_last_name.sort(key=lambda s: (s.last_name))
    print_students(by_last_name)

    print("\nSorted By First Name")
    by_first_name = students[:]
    by_first_name.sort(key=lambda s: (s.first_name))
    print_students(by_first_name)

    print("\nUnsorted")
    print_students(students)


if __name__ == "__main__":
    main()