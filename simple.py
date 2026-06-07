from flask import Flask,url_for
from app1 import students

# HTML - HARDCODED HTML CONTENT 
'<a href=" ' + url_for('studentd') + '">view students<a/>'