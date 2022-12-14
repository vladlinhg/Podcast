class Student():
    def __init__(self, name, student_id, grades = None):
        if grades is None:
            grades = []
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def to_dict(self):
        return {
            "name": self.name, 
            "student_id": self.student_id, 
            "grades": self.grades
        }

    @property
    def gpa(self):
        if len(self.grades) == 0:
            gpa = 0
        else:
            gpa = sum(self.grades)/len(self.grades)
        return round(gpa, 2)

    def add_grade(self, grade):

        if not int(grade):
            raise ValueError

        if 0 < int(grade) < 100:
            self.grades.append(int(grade))
        else:
            return True
