from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def play_the_game():
  return render_template("index.html")

app.run(debug=True)