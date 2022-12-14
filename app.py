
from models.school import School
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/error", methods = ["POST"])
def error():
    data = request.json
    return f"{data['name']}"

@app.route("/student/<STUDENT_ID>/grades/add", methods = ["POST"])
def add_grade(STUDENT_ID):
    school = School("bcit.json")
    data = request.json

    if 'grade' not in data.keys():
        return 'not in here', 400

    if school.get_student(STUDENT_ID):
        student = school.get_student(STUDENT_ID)
        if student.add_grade(data['grade']):
            return 'graded', 400
        else:
            student.add_grade(data['grade'])
            school.save()
            return 'graded', 200
    else:
        return 'big oopsie', 404

@app.route("/student/add", methods=["POST"])
def add_student():
    school = School("bcit.json")
    data = request.json
    if 'name' not in data.keys() or 'student_id' not in data.keys():
        return 'oh no', 400
    if data['name'] == '' or data['student_id'] == '':
        return 'oopsie', 400
    if school.add_student(data['name'],data['student_id']):
        school.save()
        return 'it works', 200
    else:
        return 'aw man', 409

@app.route("/")
def home(): 
    school = School("bcit.json")
    return render_template("list.html", school=school)

@app.route("/student/<string:student_id>/")
def student(student_id):
    student = School("bcit.json").get_student(student_id)
    return render_template("student.html", student=student)

if __name__ == "__main__": 
    app.run(debug=True)
 




