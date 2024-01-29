import os                   #from the standard python library
import json
from flask import Flask, render_template

app = Flask(__name__)       #single built in python variable

@app.route("/")             #route decorator, also called a pie notion, a decorator is a way of wrapping funtions
def index():
    return render_template("index.html")            #seeks the index.html

@app.route("/about")
def about():
    data = []        
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)            #seeks the about.html

@app.route("/contact")            
def contact():
    return render_template("contact.html", page_title="Contact")            #seeks the about.html

@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__ == "__main__":                          #__main__ is the default module in python, is the first module to be run so if its not imported 
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),       #use to os module to get the IP variable if it exists but set a default if it is not found
        port=int(os.environ.get("PORT", "5000")),   #5000 is a common port used by flask
        debug=True)