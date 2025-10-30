from flask import Flask, render_template, url_for


# set up application
app = Flask(__name__)

#creation of index route(url) through app route decorator 
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)