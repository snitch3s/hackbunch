import requests
import json
import collections
import re 

from secret import accessToken

from flask import Flask, render_template,request
app= Flask(__name__)

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

@app.errorhandler(500)
def not_found(e):
  nouser={
      "id":"None"
  }
  return render_template('prs.html',nouser=nouser), 500



def getpullRequests(username):
    topic_query = """
    query ($name:String!){
    repositoryOwner(login:$name){
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
    variables=dict({
        "name":str(username)
    })    
    request = requests.post('https://api.github.com/graphql', json={'query': topic_query,"variables":variables},headers=headers)
    if request.status_code == 200:
        result = request.json()
        prsdata = {}
        prcount=0
        for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
            prdata = {}
            if re.match(r'^2019-10', pr['createdAt']):
                prcount+=1
                prdata['createdAt'] = pr['createdAt']
                prdata['additions'] = pr['additions']
                prdata['deletions'] = pr['deletions']
                prsdata[pr['id']] = prdata
        if prsdata:
            #print(prsdata)
            return render_template('prs.html', prs=prsdata,prcount=prcount)
        else:
            print("No PRs made in Hacktoberfest")
            return render_template('prs.html',prcount=prcount)

if __name__ == "__main__":
    app.run()

