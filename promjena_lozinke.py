#!python.exe

import cgi
import os
import db
import authentication
from http import cookies

params = cgi.FieldStorage()
http_cookies_str = os.environ.get('HTTP_COOKIE', '')
get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
username = get_all_cookies_object.get("ime").value
user = db.get_user(username)


if os.environ["REQUEST_METHOD"].upper() == "POST":
    old = params.getvalue("oldp")
    new = params.getvalue("newp1")
    new2 = params.getvalue("newp2")
    suc = authentication.change_password(
                str(username), old, new, new2)
    if suc:
        print('Location: prijava.py')

    
def start_html():
    print('''
      <!DOCTYPE html>
      <html>
      <head>
      <body>
      <h1>Promjena lozinke</h1><br>
      <form method="POST">
      Stara lozinka:
      <input type="password" name="oldp" value="" placeholder="Unesite staru lozinku..."><br><br>
      Nova lozinka:
      <input type="password" name="newp1" value="" placeholder="Unesite novu lozinku..."><br><br>
      Ponovi novu lozinku:
      <input type="password" name="newp2" value="" placeholder="Ponovite novu lozinku..."><br><br>
      <input type="submit" name="botun" value="Promjeni"></input>
      ''')

def end_html():
  print('''
    </form>
    </body>
    </html>
  ''')

start_html()
end_html()
print(params)