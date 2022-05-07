#!python.exe

import authentication
import cgi
import os

params = cgi.FieldStorage()
if(os.environ["REQUEST_METHOD"].upper() == "POST"):
  ime = params.getvalue("ime")
  email = params.getvalue("mail")
  password = params.getvalue("loz2")
  password2 = params.getvalue("loz1")
  if(password == password2):
    suc = authentication.register(ime,email,password)
    if(suc == True):
      print('Location: prijava.py')
  else:
    print("Incorrect passwords!")
print()

def start_html():
    print('''
      <!DOCTYPE html>
      <html>
      <head>''')

def main_html():
  print('''
    <style>
      body{background-color: black}
      h1{text-align: center;
        margin:150px auto auto auto;
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
      .registracija{
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
    <h1>Registracija</h1>
      <div class="registracija">
      <form method="POST">
      Ime:
      <input type="text" name="ime" value="" placeholder="Unesite svoje ime..."><br><br>
      Email:
      <input type="email" name="mail" value="" placeholder="Unesite e-mail..."><br><br>
      Lozinka:
      <input type="password" name="loz2" value="" placeholder="Unesite lozinku..."><br><br>
      Ponovite lozinku:
      <input type="password" name="loz1" value="" placeholder="Ponovite lozinku..."><br><br>
      <input type="submit" class="botun" name="reg" value="Registiriraj se"> <br><br>
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