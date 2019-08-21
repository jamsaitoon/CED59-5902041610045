from flask import Flask,render_template , request
from wtforms import StringField,PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

class OKRegister(FlaskForm):
    Fname = StringField("FirstName", validators=[InputRequired()])
    Lname = StringField("Lastname", validators=[InputRequired()])
    mail = StringField("E-mail",  validators=[InputRequired("Please enter your email."), Email("Please enter your email again.")])
    Uname = StringField("Username", validators=[InputRequired()])
    Pass = PasswordField("Password", validators=[InputRequired(), Length(min=8, message="Please enter password 8 character.")])

@app.route('/')
def student():
    form = OKRegister()
    return render_template('Register.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = OKRegister()
    if form.validate_on_submit():
        return "Sumbit OK"
    return render_template('Register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)