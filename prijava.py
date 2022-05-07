#!python.exe

import cgi
import os
import session
from http import cookies
import authentication

params = cgi.FieldStorage()
if(os.environ["REQUEST_METHOD"].upper() =="POST"):
  user = params.getvalue("Ime")
  lozinka = params.getvalue("loz1")
  boolean, user_id = authentication.login(user,lozinka)
  if(boolean == True):
    session_id = session.create_session()
    session.add_user_to_session({"user_id": user_id, "ime" : user}, session_id)
    cookies_object = cookies.SimpleCookie()
    cookies_object["ime"] = user
    print(cookies_object.output())
    print("Location: base.py")
print()  

def start_html():
  print('''
    <!DOCTYPE html>
    <html>
    <head>''')


def main_html():
  print('''
    <style>
      body{background-color: black;}
      h1{text-align: center;
        margin:200px auto auto auto;
        width:500px;
        font-weight: bold;
        font-size: 50px;
        border-top-left-radius:20px;
        border-top-right-radius:20px;
        background-color:#252525;
        color:#ccad00;
        text-decoration:underline;
        font-family: sans-serif;
        border:2px solid #ccad00;
        border-bottom:0;
        padding:20px;
        }
      .prijava{
        padding:20px;
        padding-bottom:0;
        background-color:#252525;
        color:#ccad00;
        border:2px solid #ccad00;
        border-bottom-left-radius:20px;
        border-bottom-right-radius:20px;
        text-align: center;
        font-weight:bold;
        font-size: 18px;
        width: 500px;
        margin: auto;
      }
      .botun{
        cursor:pointer;
        border-radius: 5px;
        font-size: 18px;
        transition-duration: 0.4s;
      }
      .botun:hover{
        background-color: #ccad00;
        color: black;
      }
      
    </style>
    </head>
    <body>
    <h1>Prijava</h1>
    <form method="POST">
    <div class="prijava">
    Ime:
    <input type="text" name="Ime" value="" placeholder="Unesite svoje ime..."><br><br>
    Lozinka:
    <input type="password" name="loz1" value="" placeholder="Unesite lozinku..."><br><br>
    <input type="submit" class="botun" name="prij" value="Prijavi se"> <br><br>
    Ili napravite novi racun klikom na:
    <a href="registracija.py">Registriraj se<br><br>
    </div>
    </form>''')


def end_html():
  print('''
    
    </body>
    </html>
  ''')


start_html()
main_html()
end_html()
