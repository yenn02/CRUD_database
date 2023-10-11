from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange

class SignIn(FlaskForm):
    student_name = StringField('Student Name:', validators=[DataRequired()])
    student_id =   StringField('Student ID',validators=[DataRequired(), Length(min=3, max=3, message='Student ID must be 3 characters')])
    credit =    IntegerField('Total Credit:', validators=[InputRequired(), NumberRange(0,200, message="Credit must be in range of 0 - 200") ])
    submit_sign = SubmitField("Sign In")

class Profile(FlaskForm):
    student_name = StringField('Student Name:', validators=[DataRequired()])
    credit = IntegerField('Total Credit:', validators=[InputRequired(), NumberRange(0,200, message="Credit must be in range of 0 - 200")])
    submit = SubmitField("Update")

class Credit(FlaskForm):
    
    credit = IntegerField('Credit:', validators=[InputRequired(), NumberRange(0,4, message="Credit must be in range of 0 - 4")])
    submit = SubmitField("Update")