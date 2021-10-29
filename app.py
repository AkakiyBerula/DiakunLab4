from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "Thisisasecret!"

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.</h1>'.format(form.username.data, form.password.data)
    return render_template('form.html', form=form)

if __name__ == '__name__':
    app.run(debug=True)