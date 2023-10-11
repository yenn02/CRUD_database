from application import app
from flask import render_template, request, redirect, flash, url_for, session

from bson import ObjectId

from .forms import SignIn, Profile, Credit
from application import db
from datetime import datetime


@app.route("/", methods = ['POST', 'GET'])
def sign_in():
    if request.method == "POST":
        form = SignIn(request.form)
        student_name = form.student_name.data
        student_id = form.student_id.data
        credit = form.credit.data
        session['student_id'] = student_id
        if (db.students.count_documents({'student_id': student_id}, limit = 1)):
            flash("ID already exist, log-in successfully")
            return redirect("/get_course")

        else:
            db.students.insert_one({
                "student_name": student_name,
                "student_id": student_id,
                "total_credit": credit,
            
            })

            flash("Student successfully added", "success")
            return redirect("/get_course")
       
    else:
        form = SignIn()
    return render_template("sign_in.html", form = form)

@app.route("/get_course")
def get_course():
    # instructors = []
    courses = []
    instructor = []
    for course in db.courses.find().sort("course_name", -1):
        course["_id"] = str(course["_id"])
        courses.append(course)
    for person in db.instructor.find():
        person["_id"] = str(person["_id"])
        instructor.append(person)

    return render_template("view_courses.html", courses = courses, instructor = instructor)

@app.route("/get_enrolled")
def get_enrolled():
    courses = []
    instructor = []
    enrollment = []
    student_id = session['student_id']
    for course in db.courses.find().sort("course_name", -1):
        course["_id"] = str(course["_id"])
        courses.append(course)
    for person in db.instructor.find():
        person["_id"] = str(person["_id"])
        instructor.append(person)
    for enroll in db.enrollment.find():
        enroll["_id"] = str(enroll["_id"])
        enrollment.append(enroll)
    return render_template("drop_course.html", courses = courses, instructor = instructor, enrollment = enrollment, student_id = student_id)

@app.route("/add_course/<id>", methods = ['POST', 'GET'])
def add_course(id):
    enroll = []
    for course in db.courses.find().sort("course_name", -1):
        if course["_id"] == ObjectId(id):
            enroll.append(course["course_id"])
   
    if (db.enrollment.count_documents({'course_id': enroll[0], 'student_id': session['student_id']}, limit = 1)):
        flash("Course already added!")
    else:
        db.enrollment.insert_one({
            "course_id": enroll[0],
            "student_id":session['student_id'],
        })
        
        flash("Course successfully added", "success")
        # return redirect("/")
  
    return redirect("/get_course")


@app.route("/delete_course/<id>")
def delete_course(id):
    db.enrollment.find_one_and_delete({"_id": ObjectId(id)})
    flash("Course successfully deleted", "success")
    return redirect("/get_enrolled")

@app.route("/profile")
def profile():
    students = []
    student_id = session['student_id']
    courses = []
    instructor = []
    enrollment = []
    for course in db.courses.find().sort("course_name", -1):
        course["_id"] = str(course["_id"])
        courses.append(course)
    for person in db.instructor.find():
        person["_id"] = str(person["_id"])
        instructor.append(person)
    for enroll in db.enrollment.find():
        enroll["_id"] = str(enroll["_id"])
        enrollment.append(enroll)
    for student in db.students.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    
    return render_template("view_profile.html", students = students, student_id = student_id, courses = courses, instructor = instructor, enrollment = enrollment)    

@app.route("/update_profile/<id>", methods = ['POST', 'GET'])
def update_profile(id):
    if request.method == "POST":
        form = Profile(request.form)
        student_name = form.student_name.data
        credit = form.credit.data
       
    
        db.students.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "student_name": student_name,
            "total_credit": credit,
        }})
        flash("Successfully updated profile", "success")
        return redirect("/profile")
    else:
        form = Profile()

       
    return render_template("update_profile.html", form = form)
@app.route("/update_credit/<id>", methods = ['POST', 'GET'])
def update_credit(id):
    if request.method == "POST":
        form = Profile(request.form)
        credit = form.credit.data
       
    
        db.enrollment.find_one_and_update({"_id": ObjectId(id)}, {"$set": {
            "credit": credit,
        }})
        flash("Successfully updated grade", "success")
        return redirect("/profile")
    else:
        form = Profile()

    return render_template("update_credit.html", form = form)