from flask import Flask, render_template, redirect,  url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf

app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisisasecret!"

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=5, max=10, message='Must be from 5 to 10 symbols')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), AnyOf(values=['password', 'secret'])])

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Дані занесені успішно!')
        flash('The username is ' + form.username.data + ". The password is " + form.password.name + "!")
        return redirect(url_for('form'))
    return render_template('form.html', form=form)

if __name__ == '__name__':
    app.run(debug=True)