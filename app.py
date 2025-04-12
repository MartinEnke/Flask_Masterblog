from flask import Flask, request, render_template, redirect, url_for
import json

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the home page with all blog posts."""
    with open("blog_posts.json") as file:
        blog_posts = json.load(file)
    return render_template("index.html", posts=blog_posts)


@app.route("/show")
def show():
    """Renders the page displaying all blog posts."""
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)
    return render_template("show.html", posts=blog_posts)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Handles form for adding a new blog post."""
    if request.method == "POST":
        new_post = {
            "id": int(request.form["id"]),
            "author": request.form["author"],
            "title": request.form["title"],
            "content": request.form["content"]
        }
        with open("blog_posts.json", "r") as file:
            posts = json.load(file)

        posts.append(new_post)

        with open("blog_posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_blog(post_id):
    """Deletes a blog post by ID."""
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    new_blog_posts = [post for post in blog_posts if post["id"] != post_id]

    with open("blog_posts.json", "w") as file:
        json.dump(new_blog_posts, file, indent=4)

    return redirect(url_for("show"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Updates an existing blog post by ID."""
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    post_to_update = None
    for post in blog_posts:
        if post is None:
            return "Post not found", 404
        if post["id"] == post_id:
            post_to_update = post
            break

    if request.method == "POST":
        post_to_update["title"] = request.form["title"]
        post_to_update["author"] = request.form["author"]
        post_to_update["content"] = request.form["content"]

        with open("blog_posts.json", "w") as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for("show"))

    return render_template("update.html", post=post_to_update)


@app.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    """Increments like counts for the blog posts."""
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1
            break

    with open("blog_posts.json", "w") as file:
        json.dump(blog_posts, file, indent=4)

    return redirect(url_for("show") + f"#post-{post_id}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=True)
