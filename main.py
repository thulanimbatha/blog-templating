from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    blog_posts = response.json()
    return render_template("index.html", posts=blog_posts)

if __name__ == "__main__":
    app.run(debug=True)
