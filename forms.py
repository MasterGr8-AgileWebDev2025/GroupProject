from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, SelectField, MultipleFileField, HiddenField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already in use. Please use a different one or login.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class MatchUploadForm(FlaskForm):
    title = StringField('Match Title', validators=[DataRequired()])
    date = DateField('Match Date', validators=[DataRequired()])
    opponent = StringField('Opponent')
    location = StringField('Location')
    description = TextAreaField('Description')
    user_score = StringField('Your Score', validators=[DataRequired()])
    opponent_score = StringField('Opponent Score', validators=[DataRequired()])
    match_result = SelectField('Match Result', 
                              choices=[('win', 'Win'), ('loss', 'Loss'), ('draw', 'Draw')],
                              validators=[DataRequired()])
    files = MultipleFileField('Upload Match Data')
    submit = SubmitField('Upload Match')

class ExcelUploadForm(FlaskForm):
    title = StringField('Match Title', validators=[DataRequired()])
    excel_file = FileField('Excel File', validators=[
        DataRequired(),
        FileAllowed(['xlsx', 'xls'], 'Excel files only (.xlsx or .xls)')
    ])
    submit = SubmitField('Upload and Process')

class MatchShareForm(FlaskForm):
    username = StringField('Username to share with', validators=[DataRequired()])
    match_id = HiddenField('Match ID', validators=[DataRequired()])
    submit = SubmitField('Share Match Analysis')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if not user:
            raise ValidationError('Username does not exist.')

class ProfileUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm New Password', validators=[EqualTo('new_password')])
    submit = SubmitField('Update Profile')
