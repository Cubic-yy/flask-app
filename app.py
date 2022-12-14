from flask import Flask, render_template
import stbldiff, word_api

app = Flask(__name__)

@app.route("/")
def hello_world():
    word, sentences = word_api.word_gen()
    images_str = stbldiff.img_gen(sentences)
    return render_template("hello.html", word=word, sentence=sentences[0], image_str=images_str[0])