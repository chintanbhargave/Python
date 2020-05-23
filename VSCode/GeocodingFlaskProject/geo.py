from flask import Flask, render_template, request, send_file
import pandas
from geopy.geocoders import ArcGIS
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("project.html")

@app.route('/success', methods= ['POST'])
def success():
    global filename
    if request.method=="POST":
        file = request.files['myfile']
        try:
            df = pandas.read_csv(file)
            gc = ArcGIS(scheme='http')
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x!= None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x!= None else None)
            df=df.drop("coordinates",1)
            filename = datetime.datetime.now().strftime("uploads/%Y-%m-%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename,index=None)
            return render_template("project.html", text=df.to_html(), btn = 'download.html')   
        except :
            return render_template("project.html", text="Please make sure you have an address column in your csv file!!")

@app.route('/download-file/')
def download():
    return send_file(filename, attachment_filename='yourfile.csv',as_attachment=True)

if __name__ == "__main__":
    app.debug = True
    app.run()