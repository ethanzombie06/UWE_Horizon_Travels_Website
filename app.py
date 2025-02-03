from flask import Flask, render_template, redirect, request, flash, url_for
from forms import SignInForm, SignUpForm

f = open("demofile2.txt", "a")
f.write("\n--------------------\n")
f.close()

app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template('home.html') 

@app.route('/timetable')
def Timetable():
    return render_template('timetable.html')

@app.route('/sign_in', methods=['GET','POST'])
def Sign_In():

    #using class defined in forms.py to use wtforms as it has compatibility with flask
    form = SignInForm(request.form)
    if request.method == 'POST' and form.validate():

        #user = (form.username.data, form.email.data, form.password.data)

        #need to check how flash is going to work here might need to style in html/css
        flash('Thanks for Signing in!')
        return redirect(url_for('Homepage'))
    
    #if form doesnt validate return normal page
    return render_template('sign_in.html', form=form)


@app.route('/sign_up')
def Sign_Up():
    #using class defined in forms.py to use wtforms as it has compatibility with flask
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():

        #dodge way of storing info just for debugging
        f = open("demofile2.txt", "a")
        f.write(f"Username:\n{form.username.data}\nEmail:\n{form.email.data}\nPassword:\n{form.password.data}")
        f.close()

        #need to check how flash is going to work here might need to style in html/css
        flash('Thanks for registering! Please now sign in.')
        return redirect(url_for('Sign_in'))

    return render_template('home.html') 

if __name__ == '__main__':
    app.run(debug=True)