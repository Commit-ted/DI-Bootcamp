class Student:
    def __init__(self, name):
        # Initialize the name and grades attributes
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        # Add or update the grade for the subject
        self.grades[subject] = grade

    def calculate_average(self):
        # Calculate and return the average grade
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        # Customize the string representation to display name and grades
        grades_str = ", ".join(f"{subject}: {grade}" for subject, grade in self.grades.items())
        return f"Student: {self.name}\nGrades: {grades_str}\n"

    def remove_grade(self, subject):
        # Remove the grade for the subject if it exists
        if subject in self.grades:
            del self.grades[subject]
        else:
            print(f"Error: {self.name} does not have a grade for {subject}.")

# Example usage of Student class:
alice = Student("Alice")
alice.add_grade("Math", 90)
alice.add_grade("Science", 85)
print(alice)

