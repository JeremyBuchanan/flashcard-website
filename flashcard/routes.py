from flask import render_template, url_for, flash, redirect
from flashcard import app
from flashcard.forms import RegistrationForm, LoginForm
from flashcard.models import User, Flashcard


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@site.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/profile')
def profile():
    return render_template('profile.html')
