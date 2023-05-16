from datetime import datetime
from app import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Define the configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'

# Define the mail object for sending emails
mail = Mail(app)

# Define the route for the home page
@app.route("/")
def index():
    return render_template("home.html")

# Define the route for the posts page
@app.route("/posts")
def posts():
    return render_template("posts-all.html", posts=posts)

# Define the route for a single post page
@app.route("/posts/<int:id>")
def post(id):
    post = next((p for p in posts if p["id"] == id), None)
    if post:
        return render_template("post-single.html", post=post)
    else:
        return render_template("404.html"), 404

# Define the route for the contact us page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

    @app.route('/send_email', methods=['POST'])
    def send_reset_email():
        user_email = request.form['user_email']
    msg = Message('title of  email',
                  sender='noreply@demo.com',
                  recipients=['Ubtalubt@gmail.com'])
    msg.body = f'''
        Hello {'Ubtalubt@gmail.com'},
    '''
    mail.send(msg)
    return 'success!'

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

if __name__ == '__main__':
    app.run(debug=True)
