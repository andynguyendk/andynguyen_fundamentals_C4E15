from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    data = {
    "Andy" : {
                "name":"Andy",
                "age":"30",
                "gender": "male",
                "hobbies":["pingpong", "movie"],
    }
    }
    if username in data:
        user = data[username]
    return render_template('user.html', user = user)

@app.route('/blog')
def blog():
    article_name = 'Thơ con cóc'
    posts = [
        {
        "content" :"1234",
        "author" : "abc",
        },
        {
        "content" : "12345",
        "author": "abcd",
        },
        {
        "content": "123456",
        "author": "tada",
        }
    ]
    return render_template('blog.html', article_title=article_name, posts = posts)

@app.route('/hello')
def hello():
    return "C4E15"

@app.route('/sayhi/<name>')
def sayhi(name):
    return "hello " + name
@app.route('/sum/<int:a>/<int:b>')
def sum(a,b):
    c = a + b
    return str(a) + "+" + str(b) + "=" + str(c)
@app.route('/html')
def heading():
    return "<h1> GCĐ </h1>"

if __name__ == '__main__':
  app.run(debug=True)
