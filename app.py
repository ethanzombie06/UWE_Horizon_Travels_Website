from flask import Flask, render_template, redirect, request, flash, url_for
from forms import SignInForm, SignUpForm
from sql_commands import add_user_sql
import sql_commands
import mysql.connector

cnx = mysql.connector.connect(user = 'root', password='sql1',
                              host = '127.0.0.1',
                              database = 'Horizion_travles_database')

cursor = cnx.cursor()


f = open("demofile2.txt", "a")
f.write("\n--------------------\n")
f.close()

app = Flask(__name__)

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

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


@app.route('/sign_up', methods = ['GET','POST'])
def Sign_Up():
    #using class defined in forms.py to use wtforms as it has compatibility with flask
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():


        # saving to database
        sql = add_user_sql(
                fname = form.fname.data,
                lname =form.lname.data,
                age=form.age.data,
                email=form.email.data,
                password=form.password.data) # need to add encryption)
        sql =  ("INSERT INTO user_info (last_name, first_name, age, email, hashed_password) VALUES (%s,%s,%s,%s,%s)")
        data = (form.lname.data, form.fname.data, form.age.data, form.email.data, form.password.data)
        cursor.execute(sql,data)
        cnx.commit()

        #need to check how flash is going to work here might need to style in html/css
        flash('Thanks for registering! Please now sign in.')
        return redirect(url_for('Sign_In'))

    return render_template('sign_up.html', form=form) 

if __name__ == '__main__':
    app.run(debug=True)