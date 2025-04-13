from flask import Flask, request, render_template, redirect, url_for
import json
from datetime import datetime
from translations import translations

app = Flask(__name__)


@app.route('/')
def index():
    lang = request.args.get("lang", "en")
    """Renders the home page with all blog posts."""
    with open("blog_posts.json") as file:
        blog_posts = json.load(file)
    return render_template("index.html", posts=blog_posts, t=translations[lang], lang=lang)



@app.route("/show")
def show():
    """Renders the page displaying all blog posts with sorting."""
    sort_by = request.args.get("sort", "likes")
    lang = request.args.get("lang", "en")  # default to English

    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    if sort_by == "latest":
        blog_posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    elif sort_by == "oldest":
        blog_posts.sort(key=lambda x: x.get("date", ""))
    elif sort_by == "likes":
        blog_posts.sort(key=lambda x: x.get("likes", 0), reverse=True)

    return render_template("show.html", posts=blog_posts, sort=sort_by, t=translations[lang], lang=lang)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Handles form for adding a new blog post."""
    lang = request.args.get("lang", "en")
    if request.method == "POST":
        new_post = {
            "id": int(request.form["id"]),
            "author": request.form["author"],
            "title": request.form["title"],
            "content": request.form["content"],
            "date": datetime.now().strftime("%B %d, %Y")

        }
        with open("blog_posts.json", "r") as file:
            posts = json.load(file)

        posts.append(new_post)

        with open("blog_posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        return redirect(url_for("index"))

    return render_template("add.html", t=translations[lang], lang=lang)


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
    lang = request.args.get("lang", "en")  # get current language

    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    post_to_update = None
    for post in blog_posts:
        if post["id"] == post_id:
            post_to_update = post
            break

    if not post_to_update:
        return "Post not found", 404

    if request.method == "POST":
        post_to_update["title"][lang] = request.form["title"]
        post_to_update["author"] = request.form["author"]
        post_to_update["content"][lang] = request.form["content"]
        post_to_update["updated"] = datetime.now().strftime("%B %d, %Y")

        with open("blog_posts.json", "w") as file:
            json.dump(blog_posts, file, indent=4)

        return redirect(url_for("show", lang=lang))

    return render_template("update.html", post=post_to_update, lang=lang, t=translations[lang])



@app.route("/like/<int:post_id>", methods=["POST"])
def like_post(post_id):
    """Increments like counts for the blog posts."""
    with open("blog_posts.json", "r") as file:
        blog_posts = json.load(file)

    for post in blog_posts:
        if post["id"] == post_id:
            post["likes"] = post.get("likes", 0) + 1
            updated_likes = post["likes"]
            break

    with open("blog_posts.json", "w") as file:
        json.dump(blog_posts, file, indent=4)

    return {"likes": updated_likes}, 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=True)
