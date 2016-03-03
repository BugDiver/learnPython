from flask import Flask, url_for, render_template ,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comment',methods = ['GET','POST'])
def giveCommentResponse():
	if request.method == 'POST':
		return 'we got your comment <h3>'+request.form['comment']+'</h3>'

if __name__ == '__main__':
    app.run()
