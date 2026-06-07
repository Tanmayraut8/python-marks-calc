from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "autofill_secret"

project_info = {
    "name": "autofromfillup",
    "description": "Secure client-side browser assistant that auto-fills Indian government job application forms using user's own DigiLocker data legally."
}

jobs_list = [
    {"title": "MPSC State Service Exam", "dept": "Revenue Department", "status": "Active", "badge_class": "bg-success"}
]

@app.route('/')
def home():
    return render_template('home.html', project=project_info, jobs=jobs_list)

@app.route('/records')
def records():
    return render_template('records.html', project=project_info, jobs=jobs_list)

@app.route('/add-job', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        title = request.form.get('title')
        dept = request.form.get('dept')
        status = request.form.get('status')
        days_left = request.form.get('days_left')

        if not title or not dept or not status or not days_left:
            flash("All fields are required!", "danger")
            return redirect(url_for('add_job'))

        badge_class = "bg-success" if status == "Active" else "bg-warning text-dark"
        
        new_job = {
            "title": title,
            "dept": dept,
            "status": status,
            "badge_class": badge_class
        }
        
        jobs_list.append(new_job)
        flash("New Job Notification Added Successfully!", "success")
        return redirect(url_for('records'))

    return render_template('add_job.html', project=project_info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    