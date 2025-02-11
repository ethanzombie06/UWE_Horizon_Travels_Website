import mysql.connector

cnx = mysql.connector.connect(user = 'root', password='sql1',
                              host = '127.0.0.1',
                              database = 'Horizion_travles_database')
cursor = cnx.cursor()

def add_user(fname,lname,age,email,password):
    add_employee = ("INSERT INTO user_info"
                   "(LastName, FirstName, Age, Email, birth_date) "
                   f"VALUES ({lname}, {fname}, {age}, {email}, {password})")
    cursor.execute(add_employee)
    cnx.commit()
