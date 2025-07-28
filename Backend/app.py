from flask import Flask, render_template, redirect
import json

with open("config.json") as config_file:
    config_data = json.load(config_file)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("./Frontend/HomePage/index.html")

if __name__ == "__main__" :
    app.run(debug=True)