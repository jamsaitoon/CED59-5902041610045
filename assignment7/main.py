from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def member():
    return render_template('Register.html')

@app.route('/',methods=["post"])
def index():
    return 'xyz'

if __name__ == "__main__":
    app.run(debug=True)