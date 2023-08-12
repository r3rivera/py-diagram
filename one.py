from flask import Flask, render_template, request


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error404.html")


@app.route('/')
def index():
    '''
    index page 
    '''
    return render_template("index.html", welcome_message='Welcome to my page')


@app.route('/signup')
def sign_up():
    '''
    Sign up Page
    '''
    return render_template("signup.html", signup_message='Please provide your details')

@app.route('/home')
def signup_submit():
    first_name = request.args.get('firstname')
    last_name = request.args.get('lastname')
    return render_template("home.html", user = f"{last_name}, {first_name}")


@app.route('/health')
def health():
    '''
    Health page 
    '''
    return '<h1>Running</h1>'


@app.route('/user/<user_id>')
def user(user_id):
    return f"<h1>{user_id}</h1>"





if __name__ == '__main__':
    app.run(debug=True)