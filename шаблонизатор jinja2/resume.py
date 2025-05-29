from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_resume():
    resume_data = {
        'name': 'Гагарин Алексей',
        'job': 'Веб-программист',
        'about': 'Хочу развиться в сфере it',
        'skills': ['disign'],
    }
    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)