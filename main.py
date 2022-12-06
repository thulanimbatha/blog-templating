from flask import Flask, render_template
import requests

blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
blog_posts = response.json()    # list

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/post/<int:index>')
def show_post(index):
    wanted_post = None
    for post in blog_posts:
        if post['id'] == index:
            wanted_post = post
    return render_template("post.html", post=wanted_post)

if __name__ == "__main__":
    app.run(debug=True)
