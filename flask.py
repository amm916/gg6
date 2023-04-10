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
