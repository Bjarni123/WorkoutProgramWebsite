from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Do something with the form data (e.g. store it in a database)
    
    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
