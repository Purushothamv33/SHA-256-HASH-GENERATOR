from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def generate_sha256_hash(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_string = request.form["input_string"]
        hashed_value = generate_sha256_hash(input_string)
        return render_template("index.html", hashed_value=hashed_value, input_string=input_string)
    return render_template("index.html", hashed_value=None)

if __name__ == "__main__":
    app.run(debug=True)
