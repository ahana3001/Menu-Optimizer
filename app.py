from flask import Flask, render_template, jsonify
from ga import run_ga

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run")
def run():
    return jsonify(run_ga())

if __name__ == "__main__":
    app.run(debug=True)