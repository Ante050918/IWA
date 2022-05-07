import mysql.connector
import json
import password_utils

db_conf = {
    "host":"localhost",
    "db_name": "vjezba4",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        password=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),) ##pretvara objekt u json string
    mydb = get_DB_connection()
    cursor = mydb.cursor() ##izvrsava query i dohvaca zapise
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid ###vraca novoumetnutu vrijednost za stupac koji je auto inkrement

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone() ###vraca sljdeci red skupa rezultata upita ili ništa ko nema vise retka, po defaultu vraca tuple
    return myresult[0], json.loads(myresult[1]) ##loads se koristi za rasclanjivanje niza i vraca rjecnik

def replace_session(session_id, data):#replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id,data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit() ###izvrsava izmjene

def destroy_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    query = 'DELETE FROM sessions WHERE session_id= (%s)'
    values = (session_id, )
    cursor.execute(query, values)
    mydb.commit()


def create_user(username, email, password):
    query = "INSERT INTO users (ime, email, password) VALUES (%s, %s, %s)"
    hashed_password = password_utils.hash_password(password)
    values = (username, email, hashed_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    try:
        cursor.execute(query, values)
        mydb.commit()
    except:
        return None
    return cursor.lastrowid

def get_user(ime):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE ime='" + str(ime) + "'")
    myresult = cursor.fetchone()
    return myresult

def change_user_password(name, password):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    hashed_password = password_utils.hash_password(password)
    query = "UPDATE users SET password=%s WHERE ime=%s"
    values = (hashed_password, name)
    try:
        cursor.execute(query, values)
        mydb.commit()
        return True
    except:
        return False
