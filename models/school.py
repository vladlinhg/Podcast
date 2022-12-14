import json
from models.student import Student
import operator


class School():
    def __init__(self, filename):
        self.filename = filename
        self.load_from_json()
        
    def load_from_json(self):
        self._students = []
        f = open(self.filename)
        data  = json.load(f)
        self.name = data['name']
        for student in data['students']:
            self._students.append(Student(student['name'], student['student_id'], student['grades']))

    def get_students(self, sorted_by = "name"):
        if sorted_by == "name":
            new_list = sorted(self._students, key=operator.attrgetter('name'))
        else:
            new_list = sorted(self._students, key=operator.attrgetter('gpa'), reverse=True)
        return new_list
    
    def __len__(self):
        return len(self._students)

    def get_student(self, student_id):
        retrieve_student = None
        for student in self._students:
            if student.student_id == student_id:
                retrieve_student = student
        return retrieve_student
    
    def to_dict(self):
        list = []
        for student in self._students:
            list.append(student.to_dict())
        return {"name": self.name, 'students': list}

    def save(self):
        with open(self.filename, 'w') as outfile:
            json.dump(self.to_dict(), outfile)

    def add_student(self, name, student_id):
        if name == '' or student_id == '':
            raise ValueError

        for student in self._students:
            if student_id ==  student.student_id:
                return False

        self._students.append(Student(name, student_id))
        return True