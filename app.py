from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template('home.html') 

@app.route('/timetable')
def Timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)