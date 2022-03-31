from flask import Flask, render_template, request
import regexMemo as re


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


@app.route('/')
def home():
    return render_template('memoindex.html')



@app.route("/submit", methods=['GET', 'POST'])
def form_submit():

    msg = []
    if request.method == 'POST':
        name=request.form['name']

        if (re.match_regex_inp(name)):
            msg = ["Successfully added",name]
        else:
            msg = ["Invalid name",name]
    return render_template('memoindex.html',msg=msg)




if __name__ == '__main__':
    app.run(port=5001)