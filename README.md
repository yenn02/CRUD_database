# CRUD_database
A simple web application that interacts with the MongoDB database

1) **How to run the web application**
  a) run the web application in a virtual environment by **python run.py**
  b) install the following libraries if needed:
    i) install flask: **python -m pip install flask**
    ii) install pyMongo in the flask: **$ pip install Flask-PyMongo**
2)**Navigating through the web**
   a) **Sign-In page**: Students must enter their names, ID, and total credit. The program will check if data exists, if not, the program creates new student data
   b) **Add Course**: Students can add the courses from the provided list. The program creates new enrollment data for each enrollment.
   c) **Drop Course**: Students can drop the courses from the enrolled list. The program deletes selected courses from the enrollment collection.
   d) **Profile**:  Students can check their profile and enrolled classes, and update their Name, Total credit, or GPA in separate enrolled courses.  
   
