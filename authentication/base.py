#!python.exe

import cgi
import os
import session
import subjects
import db
from http import cookies

params = cgi.FieldStorage()
d=session.get_session_data()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)

if not get_all_cookies_object.get("ime"):
    print("Location: prijava.py")
else:
    data = session.get_session_data()
    for key, value in data.items():
        if key=='ime':
            name=value 


def start_html():
    print("""
    <!DOCTYPE html>
    <html>
    <style>
    .link{text-decoration:none;
    color: black;}
    </style>
    <head></head>
    <body>
    <form method ="POST">
    """)

def nav():
        print("""
                <button type="submit" name="botun" value="1st Year">1st Year</button>
                <button type="submit" name="botun" value="2nd Year">2nd Year</button>
                <button type="submit" name="botun" value="3rd Year">3rd Year</button>
                <button type="submit" name ="botun" value="Upisni List">Upisni List</button>
                <button type="submit" name ="botun" value="Promjena lozinke"> <a href="promjena_lozinke.py" class="link">Promjena lozinke</a></button>
                <button type="submit" name ="botun" value="Odjava"> <a href="logout.py" class="link">Odjava</a></button>
                <br><br>
        """)



def end_html():
    print("""
    
    </form>
    </body>
    </html>
    """)
def main_body():
        button = params.getvalue('botun')

        if button == None:
                button = '1st Year'

        def check(key, value):
                if key in d and d[key] == value:
                        return "checked"
                return ""

        suma = 0
        suma1 = 0
        for k,v in subjects.subjects.items():
                if button=='Upisni List':
                        print(v.get('name'))
                        print("--ECTS: ")
                        print(v.get('ects'))
                        for a, b in d.items():
                                if b == 'not' and a == k:
                                        print("-------------->" + 'Not selected')

                                elif b == 'enr' and a == k:
                                        print("-------------->" + 'Enrolled')
                                        suma += v.get('ects')
                                        suma1 += 1

                                elif b == 'pass' and a == k:
                                        print("-------------->" + 'Passed')

                        print("<br><br>")
                        
                
                

                
                
                elif (v.get('year') == 1) and button =='1st Year':
                        print(v.get('name'))
                        print("--ECTS: ")
                        print(v.get('ects'))
                        for a, b in subjects.status_names.items():
                                print("""
                                <input type="radio" name='"""+k+"""' value='"""+a+"""' """+check(k,a)+"""> """+b+"""</input>
                                """)
                                
                        print("<br><br>")
                        
                elif((v.get('year') == 2) and (button =='2nd Year')):
                        print(v.get('name'))
                        print("--ECTS: ")
                        print(v.get('ects'))
                        for a, b in subjects.status_names.items():
                                print("""
                                <input type="radio" name='"""+k+"""' value='"""+a+"""'  """+check(k,a)+"""> """+b+"""</input>
                                """)
                        print("<br><br>")  
                
                elif((v.get('year') == 3) and (button == '3rd Year')):
                        print(v.get('name'))
                        print("--ECTS: ")
                        print(v.get('ects'))
                        for a, b in subjects.status_names.items():
                                print("""
                                <input type="radio" name='"""+k+"""' value='"""+a+"""' """+check(k,a)+"""> """+b+"""</input>
                                """)
                        print("<br><br>")
        if(button=='Upisni List'):
                print("UKUPNO UPISANIH PREDMETA-------------->" + str(suma1) + "<br>")
                print("UKUPNO ECTS BODOVA-------------->" + str(suma))
        


start_html()
nav()
main_body()
end_html()
#print(params)
#print(os.environ)