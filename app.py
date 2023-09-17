from flask import Flask, render_template, redirect, jsonify
from scrapper.comick import hot_managas, new_managas, top_mangas, details_manga, get_chapters, get_images, most_viewed

app = Flask(__name__)

@app.route("/")
def index_page():
    return redirect("/home")

@app.route("/home")
def home_page():
    hot = hot_managas(page=1)
    top = top_mangas()
    new = new_managas(page=1)
    views = most_viewed()
    return render_template("home.html", hot=hot, new=new, top=top, views=views)

@app.route("/details/<slug>")
def details_page(slug):
    details = details_manga(slug=slug)
    comic_hid = details["comic"]["hid"]
    chapter = get_chapters(hid=comic_hid)
    return render_template("details.html", manga=details, chapters=chapter)

@app.route("/read/<hid>")
def reading_page(hid):
    data = get_images(hid=hid)
    return render_template("read.html", data=data)

@app.route("/test")
def test_page():
    return most_viewed()    

app.run(host="0.0.0.0")