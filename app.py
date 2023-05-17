from flask import Flask,render_template
from postsdata import posts

app = Flask(__name__)

# Page Routes
@app.route("/")
def homePagex():
   return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')
        

@app.route("/contact")
def contact():
    return render_template('contact.html')



@app.route("/reqres-data")
def reqresData():
    return render_template('recqrst-data.html')

@app.route("/posts")
def home():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    if post_id < len(posts):
       p = posts[post_id]
       return render_template('postsingle.html',
       title= f"Post#{post_id}", p = p )
    else:
        return render_template('404.html'), 404

    
#to get favicon working on layout instead of html page
import os
from flask import send_from_directory
from json import dumps



#Implementing flask to the second form of the contact us page
@app.route('/contact-us', methods=['POST'])
def contact_us():
    name = request.form['Contact-Name']
    email = request.form['Contact-Email']
    message = request.form['Contact-Message']

    # Send email using Flask-Mail
    msg = Message('Contact Us Form Submission',
                  sender='noreply@demo.com',
                  recipients=['ubttester1@gmail.com'])
    msg.body = f'''
        Name: {name}
        Email: {email}
        Message: {message}
    '''
    mail.send(msg)

    # Return a success message to the user
    return 'Thank you for your message!'\
        '<a href="/contact"> Click here to submit another message.'\
        '</a> <br> Or click <a href="/index">Home</a> to return to the main page'

#debug tool
if __name__ == '__main__':
	app.run( debug=True )

