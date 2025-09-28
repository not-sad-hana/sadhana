from flask import Flask, render_template, request

app = Flask(__name__)
users = {"test@example.com": "1234"}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email in users and users[email] == password:
            return redirect(url_for("budget"))  # go to budget planner
        else:
            return "Invalid credentials! Try again."
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        users[email] = password  # save new user
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/budget", methods=["GET", "POST"])
def budget():
    if request.method == "POST":
        income = float(request.form["income"])
        expense = float(request.form["expense"])
        savings = income - expense
        return render_template("result.html", income=income, expense=expense, savings=savings)
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def home2():
    if request.method == "POST":
        income = float(request.form["income"])
        expense = float(request.form["expense"])
        savings = income - expense
        return render_template("result.html", income=income, expense=expense, savings=savings)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
