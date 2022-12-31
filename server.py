from flask import Flask,render_template, url_for ,request,redirect
import csv
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/<string:pageName>")
def html(pageName):
    return render_template(pageName)
