import flask

app = flask(__name__)

@app.route('/')
def hello_word():
    return "<p>hello word<p>"