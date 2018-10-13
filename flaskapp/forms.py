from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskapp.models import User

# Registration
class RegistrationForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    confirm_password = PasswordField('Passwort erneut eingeben', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

    # Überprüft, ob Username in der Datenbank bereits existiert
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Dieser Benutzername ist leider bereits vergeben. Bitte suche dir einen neuen Name aus.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Diese Email ist leider bereits vergeben. Bitte suche dir eine neue Email aus.')

# Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Passwort speichern')
    submit = SubmitField('Anmelden')

# Ändern des eigenen Profils
class UpdateAccountForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Aktualisieren')

    # Überprüft, ob Username in der Datenbank bereits existiert
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Dieser Benutzername ist leider bereits vergeben. Bitte suche dir einen neuen Name aus.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Diese Email ist leider bereits vergeben. Bitte suche dir eine neue Email aus.')
