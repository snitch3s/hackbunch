import requests
import json
import collections
import re 

from flask import Flask, render_template,request
app= Flask(__name__)

accessToken = "<-Insert Access code here->"
headers = {"Authorization": "bearer "+ accessToken }


@app.route('/',methods = ['GET','POST'])
def index():    
	if request.method == 'POST': # basic Flask structure 
		username = request.form['github-username'] 
		# return in the browser
		while username!='':
			prsdata=getpullRequests(username)

			return '''{}'''.format(prsdata)
	return render_template('index.html')


def getpullRequests(username):
    topic_query = """
    query {
    repositoryOwner(login:""" + str(username) + """) {
        login 
        ... on User {
        name
        avatarUrl
        pullRequests(last: 100){
            nodes{
            id
            createdAt
            additions
            deletions
            }
        }
        } 
    }
    } 
    """
    request = requests.post('https://api.github.com/graphql', json={'query': topic_query}, headers=headers)
    if request.status_code == 200:
        result = request.json()
        prsdata = {}
        for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
            prdata = {}
            if re.match(r'^2019-10', pr['createdAt']):
                prdata['createdAt'] = pr['createdAt']
                prdata['additions'] = pr['additions']
                prdata['deletions'] = pr['deletions']
                prsdata[pr['id']] = prdata
        if prsdata:
            #print(prsdata)
            return prsdata
        else:
            print("No PRs made in Hacktoberfest")

if __name__ == "__main__":
	app.debug = True
	app.run()

