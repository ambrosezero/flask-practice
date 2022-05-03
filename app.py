from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home_page():
    html = """
    <html>
        <body>
            <h1>Welcome Home!</h1>
            <p>This is the home page</p>
            <a href='/hello'>Go to "hello" page</a>
        </body>
    </html>
    """
    return html


@app.route("/hello")
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p>This is the hello page</p>
        </body>
    </html>
    """
    return html


@app.route("/goodbye")
def say_bye():
    return "goodbye".capitalize()


@app.route("/search")
def search():
    term = request.args["term"]
    return f"<h1>Search Results For: {term}</h1>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "you made a post request"


@app.route("/add-comment")
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form>
        <input type='text' placeholder='comment'/>
        <button>Submit</button>
    </form>
    """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    return """
    <h1>SAVED YOUR COMMENT</h1>
    """
