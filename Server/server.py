#!flask webserver
from flask import Flask, render_template, request, redirect, url_for
from threading import Timer
app = Flask(__name__, template_folder='public')

   
@app.route('/index')
@app.route('/')
def index():
      return render_template('index.html')

@app.route('/story')
def story():
   return render_template('story.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      print("Coin Box Open")
      t = Timer(10.0, timer)
      t.start()
      return render_template("thank.html", result = result)

def timer():
      print("Coin Box Close")


if __name__ == '__main__':
   app.run(debug = True)