from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)



@app.route('/')
def index():
    with open("blog_posts.json") as file:
        blog_posts = json.load(file)

    return render_template('index.html', posts=blog_posts)


@app.route("/show")
def show():
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    return render_template('show.html', posts=blog_posts)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        new_post = {
            "id": int(request.form['id']),
            "author": request.form['author'],
            "title": request.form['title'],
            "content": request.form['content']
        }
        # Load existing posts
        with open("blog_posts.json", "r") as file:
            posts = json.load(file)
        # Add the new post
        posts.append(new_post)
        # Save updated posts
        with open("blog_posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        return redirect(url_for('index'))

    return render_template("add.html")



@app.route("/delete/<int:post_id>")
def delete_blog(post_id):
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    new_blog_posts = [post for post in blog_posts if post["id"] != post_id]

    with open("blog_posts.json", "w") as file:
        json.dump(new_blog_posts, file, indent=4)

    return redirect(url_for("index"))






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=True)