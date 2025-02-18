import mysql.connector

def add_user_sql(fname,lname,age,email,password):
    return (f"INSERT INTO user_info (last_name, first_name, age, email, hashed_password) VALUES ({lname}, {fname}, {age}, {email}, {password})")