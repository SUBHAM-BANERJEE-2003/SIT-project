from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def submit():
    form_data = request.json
    print(form_data)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
