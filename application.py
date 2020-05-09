from flask import Flask, render_template
import datetime

app=Flask(__name__)

@app.route("/")
def index():
    names=["Alice","Charlie","Bob"]
    return render_template("index.html",names=names)

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/newyear")
def newyear():
    now=datetime.datetime.now()
    new_year=now.month==5 and now.day==9
    return render_template("index.html",new_year=new_year)

@app.route("/bye")
def bye():
    headline="Goodbye!"
    return render_template("index.html",headline=headline)
