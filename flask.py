from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)

# Define the post data
posts = [
    {
        "id": 1,
        "title": "My first blog post",
        "content": "This is the content of my first blog post.",
        "date_posted": datetime(2023, 4, 1),
        "author": "Ammar"
    },
    {
        "id": 2,
        "title": "My second blog post",
        "content": "This is the content of my second blog post.",
        "date_posted": datetime(2023, 4, 2),
        "author": "Shaker"
    },
    {
        "id": 3,
        "title": "My third blog post",
        "content": "This is the content of my third blog post.",
        "date_posted": datetime(2023, 4, 3),
        "author": "Amjad"
    }
]
# Define the route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Define the route for the posts page
@app.route("/posts")
def posts():
    return render_template("posts.html", posts=posts)

# Define the route for a single post page
@app.route("/posts/<int:id>")
def post(id):
    post = next((p for p in posts if p["id"] == id), None)
    if post:
        return render_template("post.html", post=post)
    else:
        return render_template("404.html"), 404

# Define the route for the contact us page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login("youremail@gmail.com", "yourpassword")
            subject = f"New message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\n{message}"
            smtp.sendmail("youremail@gmail.com", "recipientemail@example.com", f"Subject: {subject}\n\n{body}")

        return redirect(url_for("thankyou"))

    return render_template("contactus.html")

# Define the route for the thank you page
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

# Define the route for the 404 page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Define the route for the server error page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500
