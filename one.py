from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def index():
    '''
    Main page 
    '''
    
    name_var = "Some Variable1"
    return render_template("home.html", name_var=name_var, sum=list(name_var) )


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