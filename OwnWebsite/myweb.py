from flask import Flask,render_template

#  Instantiating
app = Flask(__name__)

#  decorator. return content of the fn will be mapped to the url specified in the decorator

@app.route('/')
def fn():
    return render_template("home.html")

@app.route('/content/')
def con():
    return render_template("content.html")

if __name__ == "__main__":
    app.run(debug=True)    

