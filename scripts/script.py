import requests
import json
import collections
import re 

accessToken = "<--insert your accessToken here-->"
headers = {"Authorization": "bearer "+ accessToken }

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
        for pr in result['data']['repositoryOwner']['pullRequests']['nodes']:
            prdata = {}
            if re.match(r'^2019-10', pr['createdAt']):
                prdata['createdAt'] = pr['createdAt']
                prdata['additions'] = pr['additions']
                prdata['deletions'] = pr['deletions']
                prsdata[pr['id']] = prdata
        if prsdata:
            print(prsdata)
        else:
            print("No PRs made in Hacktoberfest")

if __name__ == "__main__":
    username = input("Enter the GitHub username: ")
    getpullRequests(username)