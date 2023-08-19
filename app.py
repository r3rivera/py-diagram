from myproject import app
from flask import render_template

@app.route('/')
def index():
    welcome_message = 'Hello and Welcome!'
    return render_template('home.html',welcome_message=welcome_message)

if __name__ == '__main__':
    app.run(debug=True)