from flask import Flask

#  Instantiating
app = Flask(__name__)

#  decorator. return content of the fn will be mapped to the url specified in the decorator

@app.route('/')
def fn():
    return " This is Homepage"

@app.route('/content/')
def con():
    return " Hello, This is content page"    

if __name__ == "__main__":
    app.run(debug=True)    

