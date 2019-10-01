from flask import Flask, render_template,request

app= Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	if request.method == 'POST': # basic Flask structure 
		username = request.form['github-username'] 

		# return in the browser
		while username!='':
			return '<p>github.com/{}</p>'.format(str(username)) # insert content in img tag

	return render_template('index.html')

if __name__=='__main__':
	app.run()
