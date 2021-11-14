from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Robbin Mwangi',
        'title':'blog 1',
        'content':'fist blog content',
        'date_posted':'16/01/2020',
    },
    {
        'author':'Robbin Mwangi',
        'title':'blog 1',
        'content':'fist blog content',
        'date_posted':'16/01/2020',
    }
]



@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html', posts=posts)

@app.route("/about")
def about():

    return render_template('about.html', title='About')

if __name__  ==  '__main__':

    app.run(debug=TRUE)
