from flask import Flask

app = Flask(__name__)

students = [
    {"name": "jaykumar", "roll": 1, "mark": 85},
    {"name": "jaykumar", "roll": 4, "mark": 90},
    {"name": "jaykumar", "roll": 5, "mark": 95}
]

@app.route('/')
def home():
    html = "<h1>Wcollage portal - students</h1>"
    html += "<ul>"
    for student in students:
        html += f"<li>{student['name']} - Roll: {student['roll']} - Mark: {student['mark']}</li>"
    html += "</ul>"
    return html

@app.route('/about')
def about():
    return "<h1>this is about page</h1>"

@app.route('/contact')
def contact():
    return "<h1>this is contact page</h1>"

@app.route('/services')
def services():
    return "<h1>this is services page</h1>"

if __name__ == '__main__':
    app.run(debug=True)

